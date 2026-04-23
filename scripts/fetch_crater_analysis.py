#!/usr/bin/env python3
"""Fetch and process fontc_crater data for the gfonts_agents dashboard.

Downloads results from the googlefonts/fontc_crater GitHub repo,
analyzes per-target diffs, and produces a processed JSON file
for the dashboard's "fontc Crater Analysis" page.
"""

import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

BASE_URL = "https://raw.githubusercontent.com/googlefonts/fontc_crater/main"
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "fontc_crater_analysis.json"

# Path to an out-of-tree file listing upstream repos that must not be surfaced
# on the public dashboard. The file is intentionally NOT part of this repo —
# listing slugs inside a committed file would itself leak the names. Override
# with the GFONTS_PRIVATE_REPOS_FILE env var if you keep the file elsewhere.
PRIVATE_REPOS_FILE = Path(os.environ.get(
    "GFONTS_PRIVATE_REPOS_FILE",
    Path.home() / ".config" / "gfonts-agents" / "private_repos.txt",
))


def load_private_repo_slugs() -> list:
    """Read the non-public repo slug list from PRIVATE_REPOS_FILE.

    Format: one slug substring per line, lowercase. Blank lines and `#`
    comments are ignored. Returns an empty list if the file is missing,
    printing a warning — callers should decide whether that is acceptable.
    """
    if not PRIVATE_REPOS_FILE.exists():
        print(
            f"WARNING: {PRIVATE_REPOS_FILE} not found — no upstream repos will "
            "be filtered. Create the file (one slug per line) to enable "
            "filtering of non-public repos.",
            file=sys.stderr,
        )
        return []
    slugs = []
    for line in PRIVATE_REPOS_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        slugs.append(line.lower())
    return slugs


def _make_private_matcher(slugs: list):
    """Return a predicate that matches tokens containing any denylist slug
    as a whole repo name (not a prefix of a hyphenated name). Left
    boundary: start-of-string or "/". Right boundary: end-of-string, "/",
    or "_" — the latter handles crater source keys of the form
    "owner/slug_commithash". Crucially, "-" is NOT a boundary, so a
    denylist entry "foo" does not match "owner/foo-bar" — hyphenated
    variants must be listed explicitly in the denylist file."""
    if not slugs:
        return lambda token: False
    parts = "|".join(re.escape(s) for s in slugs)
    pattern = re.compile(rf"(?:^|/)(?:{parts})(?=$|[/_])")

    def match(token):
        if not token:
            return False
        return bool(pattern.search(token.lower()))

    return match


PRIVATE_REPO_SLUGS = load_private_repo_slugs()
is_private_repo_token = _make_private_matcher(PRIVATE_REPO_SLUGS)


def normalize_repo_url(url: str) -> str:
    """Normalize a repo URL for set comparison against gfonts_library_sources.

    Returns a string like "owner/repo" (lowercase, no scheme, no .git suffix,
    no trailing slash). Returns empty string for falsy input.
    """
    if not url:
        return ""
    u = url.strip().rstrip("/").lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.sub(r"^github\.com/", "", u)
    u = re.sub(r"\.git$", "", u)
    return u


def build_crater_sources_index(sources: dict) -> dict:
    """Turn crater's sources.json into a repo-keyed index.

    sources.json maps "owner/repo_commithash (config)" -> "https://github.com/owner/repo"
    We produce: {norm_url: [{"key": <source_key>, "url": <original_url>}, ...]}
    so clients can quickly ask "is this family's repo consumed by crater?".
    """
    index = defaultdict(list)
    for source_key, url in sources.items():
        norm = normalize_repo_url(url)
        if not norm:
            continue
        if is_private_repo_token(norm) or is_private_repo_token(source_key) or is_private_repo_token(url):
            continue
        index[norm].append({"key": source_key, "url": url})
    return dict(index)


def build_crater_targets_index(targets: dict) -> dict:
    """Turn crater's targets.json into a repo-keyed index.

    targets.json at the repo root is the *intended* target list (declared via
    PRs to fontc_crater), while results/sources.json reflects what was actually
    consumed on the most recent run. They differ when a target is queued but
    silently dropped, or when upstream source/config resolution fails.

    Input format (v1.1):
      {
        "version": "1.1",
        "fonts_repo_sha": "<sha>",
        "sources": [
          {"repo_url": "...", "rev": "...", "config": "...",
           "config_is_external": true|false, "has_rev_conflict": true|false},
          ...
        ]
      }

    `config_is_external` means google-fonts-sources found an override
    config.yaml in google/fonts (path is relative to the google/fonts repo
    root, e.g. "google/fonts/ofl/mingzat/config.yaml"). When false, the
    config path is relative to the upstream repo root.

    Output: {norm_url: [{"url", "rev", "config", "config_is_external",
                         "has_rev_conflict"}, ...]}
    """
    index = defaultdict(list)
    for entry in targets.get("sources", []) if isinstance(targets, dict) else []:
        url = entry.get("repo_url")
        norm = normalize_repo_url(url)
        if not norm:
            continue
        if is_private_repo_token(norm) or is_private_repo_token(url or ""):
            continue
        index[norm].append({
            "url": url,
            "rev": entry.get("rev"),
            "config": entry.get("config"),
            "config_is_external": bool(entry.get("config_is_external")),
            "has_rev_conflict": bool(entry.get("has_rev_conflict")),
        })
    return dict(index)


def build_failed_repos_index(failed_repos) -> dict:
    """Normalize results/failed_repos.json to a repo-keyed index.

    Crater stores it as {"https://github.com/owner/repo": "<reason>"}. We key
    by normalized owner/repo so lookups align with the other indexes.

    Output: {norm_url: {"url", "reason"}}
    """
    index = {}
    if not isinstance(failed_repos, dict):
        return index
    for url, reason in failed_repos.items():
        norm = normalize_repo_url(url)
        if not norm:
            continue
        if is_private_repo_token(norm) or is_private_repo_token(url):
            continue
        index[norm] = {"url": url, "reason": reason}
    return index


def fetch_json(path: str) -> dict | list:
    url = f"{BASE_URL}/{path}"
    print(f"  Fetching {url} ...")
    req = Request(url, headers={"User-Agent": "gfonts-agents-dashboard"})
    with urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def is_table_key(key: str) -> bool:
    """Return True if this diffs key is an actual OpenType table (not metadata)."""
    if key == "total":
        return False
    if key.startswith("sizeof("):
        return False
    return True


def process_latest_run(run_data: dict, annotations: dict, sources: dict):
    """Process the latest per-run results file."""
    # The run file has a "success" key with per-target results,
    # and may have failure keys
    success = run_data.get("success", run_data)
    if isinstance(success, dict) and "success" in success:
        success = success["success"]

    # Strip non-public targets before any further processing so nothing
    # downstream (table stats, diff profiles, annotations, failure lists)
    # can carry a reference through.
    success = {k: v for k, v in success.items() if not is_private_repo_token(k)}
    annotations = {k: v for k, v in annotations.items() if not is_private_repo_token(k)}

    # Categorize targets
    identical_targets = []
    diff_targets = {}  # target_id -> diffs dict
    fontc_failed = []
    fontmake_failed = []
    both_failed = []

    for target_id, result in success.items():
        if result == "identical":
            identical_targets.append(target_id)
        elif isinstance(result, dict) and "diffs" in result:
            diff_targets[target_id] = result["diffs"]
        elif isinstance(result, str):
            # Could be a failure string
            if "fontc" in result.lower() and "fontmake" in result.lower():
                both_failed.append(target_id)
            elif "fontc" in result.lower():
                fontc_failed.append(target_id)
            elif "fontmake" in result.lower():
                fontmake_failed.append(target_id)

    # Also check for separate failure keys in the run data
    for key in ("fontc_failed", "fontmake_failed", "both_failed"):
        if key in run_data and isinstance(run_data[key], dict):
            targets = [t for t in run_data[key].keys() if not is_private_repo_token(t)]
            if key == "fontc_failed":
                fontc_failed.extend(targets)
            elif key == "fontmake_failed":
                fontmake_failed.extend(targets)
            elif key == "both_failed":
                both_failed.extend(targets)

    total = len(identical_targets) + len(diff_targets) + len(fontc_failed) + len(fontmake_failed) + len(both_failed)

    # --- Table frequency analysis ---
    table_stats = defaultdict(lambda: {
        "affected_count": 0,
        "similarities": [],
        "fontc_only": 0,
        "fontmake_only": 0,
    })

    for target_id, diffs in diff_targets.items():
        for table, value in diffs.items():
            if not is_table_key(table):
                continue
            stats = table_stats[table]
            stats["affected_count"] += 1
            if isinstance(value, (int, float)):
                stats["similarities"].append(value)
            elif value == "fontc":
                stats["fontc_only"] += 1
            elif value == "fontmake":
                stats["fontmake_only"] += 1

    # Compute impact score: targets that would become identical if this table's diff were resolved
    # A target would become identical if this is the ONLY table with a meaningful diff
    for table in table_stats:
        impact = 0
        for target_id, diffs in diff_targets.items():
            meaningful_tables = []
            for t, v in diffs.items():
                if not is_table_key(t):
                    continue
                if isinstance(v, (int, float)) and v >= 0.9999:
                    continue  # effectively identical
                meaningful_tables.append(t)
            if meaningful_tables == [table]:
                impact += 1
        table_stats[table]["impact_score"] = impact

    table_analysis = []
    for table, stats in sorted(table_stats.items(), key=lambda x: -x[1]["affected_count"]):
        sims = stats["similarities"]
        table_analysis.append({
            "table": table,
            "affected_count": stats["affected_count"],
            "avg_similarity": round(sum(sims) / len(sims), 4) if sims else None,
            "fontc_only": stats["fontc_only"],
            "fontmake_only": stats["fontmake_only"],
            "impact_score": stats["impact_score"],
        })

    # --- Issue clustering from annotations ---
    issue_clusters = []
    seen_issues = set()

    for target_id, annot_list in annotations.items():
        for annot in annot_list:
            link = annot.get("link", "")
            text = annot.get("text", "")

            # Extract issue number from link
            m = re.search(r"/issues/(\d+)", link)
            issue_number = int(m.group(1)) if m else None
            issue_key = link or text

            if issue_key in seen_issues:
                # Find existing cluster and add target
                for cluster in issue_clusters:
                    if cluster.get("issue_url") == link or cluster.get("text") == text:
                        if target_id not in cluster["targets"]:
                            cluster["targets"].append(target_id)
                        # Add "also" targets
                        for also_target in annot.get("also", []):
                            if also_target not in cluster["targets"]:
                                cluster["targets"].append(also_target)
                        break
                continue

            seen_issues.add(issue_key)
            targets = [target_id]
            for also_target in annot.get("also", []):
                if also_target not in targets:
                    targets.append(also_target)

            # Determine which tables are involved across all affected targets
            tables_involved = set()
            for t in targets:
                if t in diff_targets:
                    for table, value in diff_targets[t].items():
                        if is_table_key(table):
                            if isinstance(value, str) or (isinstance(value, (int, float)) and value < 0.9999):
                                tables_involved.add(table)

            issue_clusters.append({
                "issue_url": link,
                "issue_number": issue_number,
                "text": text,
                "target_count": len(targets),
                "targets": targets[:10],  # cap for JSON size
                "tables_involved": sorted(tables_involved),
            })

    # Update target counts after collecting all targets
    for cluster in issue_clusters:
        cluster["target_count"] = len(cluster["targets"])

    issue_clusters.sort(key=lambda x: -x["target_count"])

    # --- Diff profile clustering ---
    profile_groups = defaultdict(list)
    for target_id, diffs in diff_targets.items():
        sig_tables = []
        for table, value in sorted(diffs.items()):
            if not is_table_key(table):
                continue
            if isinstance(value, (int, float)) and value >= 0.9999:
                continue
            sig_tables.append(table)
        sig = tuple(sig_tables)
        profile_groups[sig].append(target_id)

    # Check which targets have annotations
    annotated_targets = set()
    for target_id, annot_list in annotations.items():
        annotated_targets.add(target_id)
        for annot in annot_list:
            for also in annot.get("also", []):
                annotated_targets.add(also)

    diff_profiles = []
    for sig, targets in sorted(profile_groups.items(), key=lambda x: -len(x[1])):
        if not sig:
            continue  # skip empty signatures
        totals = []
        for t in targets:
            if t in diff_targets and "total" in diff_targets[t]:
                totals.append(diff_targets[t]["total"])
        annotated_count = sum(1 for t in targets if t in annotated_targets)
        diff_profiles.append({
            "signature": list(sig),
            "target_count": len(targets),
            "avg_total_similarity": round(sum(totals) / len(totals), 4) if totals else None,
            "annotated_count": annotated_count,
            "example_targets": targets[:5],
        })

    # --- Prioritization ---
    prioritization = []

    # Issues ranked by impact
    for cluster in issue_clusters:
        prioritization.append({
            "type": "issue",
            "label": f"#{cluster['issue_number']}: {cluster['text']}" if cluster["issue_number"] else cluster["text"],
            "impact": cluster["target_count"],
            "link": cluster["issue_url"],
            "tables": cluster["tables_involved"],
        })

    # Unannotated table patterns — tables with high affected count but not fully covered by annotations
    for ta in table_analysis:
        prioritization.append({
            "type": "table",
            "label": f"{ta['table']} table diffs",
            "impact": ta["affected_count"],
            "link": None,
            "tables": [ta["table"]],
        })

    prioritization.sort(key=lambda x: -x["impact"])

    # --- Build overview ---
    overview = {
        "total_targets": total,
        "identical": len(identical_targets),
        "identical_pct": round(100 * len(identical_targets) / total, 1) if total else 0,
        "diff_targets": len(diff_targets),
        "fontc_failed": len(fontc_failed),
        "fontmake_failed": len(fontmake_failed),
        "both_failed": len(both_failed),
        "similarity_pct": None,  # filled from summary if available
    }

    # --- Build full target list for detail table ---
    all_targets = []
    for target_id, diffs in diff_targets.items():
        total_sim = diffs.get("total")
        tables = {}
        for table, value in diffs.items():
            if not is_table_key(table):
                continue
            tables[table] = value
        # Find repo URL from sources
        repo_url = None
        for source_key, url in sources.items():
            # source keys are like "owner/repo_hash", target_id contains the repo path
            if source_key.split("_")[0] in target_id or target_id.startswith(source_key.split("_")[0]):
                repo_url = url
                break
        # Find annotations for this target
        target_annotations = []
        if target_id in annotations:
            target_annotations = annotations[target_id]

        all_targets.append({
            "id": target_id,
            "total_similarity": round(total_sim, 4) if isinstance(total_sim, (int, float)) else None,
            "tables": tables,
            "repo_url": repo_url,
            "annotations": [{"text": a["text"], "link": a.get("link", "")} for a in target_annotations],
        })

    all_targets.sort(key=lambda x: x["total_similarity"] if x["total_similarity"] is not None else 2)

    return overview, table_analysis, issue_clusters, diff_profiles, prioritization, all_targets, fontc_failed, fontmake_failed, both_failed


def process_history(summary: list) -> list:
    """Extract daily time series from summary.json."""
    # Keep last entry per day
    daily = {}
    for entry in summary:
        if not entry.get("began"):
            continue
        date_str = entry["began"][:10]
        stats = entry.get("stats", {})
        daily[date_str] = {
            "date": date_str,
            "total_targets": stats.get("total_targets", 0),
            "identical": stats.get("identical", 0),
            "identical_pct": round(100 * stats["identical"] / stats["total_targets"], 1)
                if stats.get("total_targets") else 0,
            "fontc_failed": stats.get("fontc_failed", 0),
            "fontmake_failed": stats.get("fontmake_failed", 0),
            "both_failed": stats.get("both_failed", 0),
            "similarity_pct": round(stats.get("diff_perc_including_failures", 0), 1),
        }
    return [daily[k] for k in sorted(daily.keys())]


def main():
    print("Fetching fontc_crater data...")

    summary = fetch_json("results/summary.json")
    annotations = fetch_json("results/annotations.json")
    sources = fetch_json("results/sources.json")
    failed_repos = fetch_json("results/failed_repos.json")
    targets = fetch_json("targets.json")

    # Find the latest results file from the summary
    latest_entry = summary[-1]
    results_file = latest_entry.get("results_file", "")
    if not results_file:
        print("ERROR: Could not determine latest results file from summary.json")
        sys.exit(1)

    print(f"  Latest run: {latest_entry.get('began', '?')}, results file: {results_file}")
    run_data = fetch_json(f"results/{results_file}")

    print("Processing data...")
    overview, table_analysis, issue_clusters, diff_profiles, prioritization, all_targets, fontc_failed_list, fontmake_failed_list, both_failed_list = process_latest_run(
        run_data, annotations, sources
    )

    history = process_history(summary)

    # Fill similarity_pct from latest summary entry
    latest_stats = latest_entry.get("stats", {})
    overview["similarity_pct"] = round(latest_stats.get("diff_perc_including_failures", 0), 1)

    # Also use summary stats if our parsing missed failure categories
    if overview["fontc_failed"] == 0 and latest_stats.get("fontc_failed", 0) > 0:
        overview["fontc_failed"] = latest_stats["fontc_failed"]
    if overview["fontmake_failed"] == 0 and latest_stats.get("fontmake_failed", 0) > 0:
        overview["fontmake_failed"] = latest_stats["fontmake_failed"]
    if overview["both_failed"] == 0 and latest_stats.get("both_failed", 0) > 0:
        overview["both_failed"] = latest_stats["both_failed"]
    if overview["total_targets"] == 0 and latest_stats.get("total_targets", 0) > 0:
        overview["total_targets"] = latest_stats["total_targets"]
        overview["identical"] = latest_stats.get("identical", 0)
        overview["identical_pct"] = round(100 * overview["identical"] / overview["total_targets"], 1)

    if isinstance(failed_repos, dict):
        failed_repos = {k: v for k, v in failed_repos.items() if not is_private_repo_token(k)}
    elif isinstance(failed_repos, list):
        failed_repos = [r for r in failed_repos if not is_private_repo_token(str(r))]

    crater_sources_index = build_crater_sources_index(sources)
    crater_targets_index = build_crater_targets_index(targets)
    failed_repos_index = build_failed_repos_index(failed_repos)

    fonts_repo_sha = targets.get("fonts_repo_sha") if isinstance(targets, dict) else None

    output = {
        "_metadata": {
            "generated": datetime.now().isoformat(),
            "latest_run": latest_entry.get("began", "")[:10],
            "fontc_rev": latest_entry.get("fontc_rev", ""),
            "fonts_repo_sha": fonts_repo_sha,
            "data_source": "https://github.com/googlefonts/fontc_crater",
        },
        "overview": overview,
        "table_analysis": table_analysis,
        "issue_clusters": issue_clusters,
        "diff_profiles": diff_profiles[:50],  # cap at 50 profiles
        "history": history,
        "prioritization": prioritization[:100],  # cap at 100 items
        "failed_repos": failed_repos,
        "failed_repos_index": failed_repos_index,
        "targets": all_targets,
        "crater_sources": crater_sources_index,
        "crater_targets": crater_targets_index,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput written to {OUTPUT}")
    print(f"  Overview: {overview['total_targets']} targets, {overview['identical']} identical ({overview['identical_pct']}%)")
    print(f"  Table analysis: {len(table_analysis)} tables")
    print(f"  Issue clusters: {len(issue_clusters)} issues")
    print(f"  Diff profiles: {len(diff_profiles)} clusters")
    print(f"  History: {len(history)} data points")
    print(f"  Targets with diffs: {len(all_targets)}")
    print(f"  Crater source repos (unique normalized URLs): {len(crater_sources_index)}")
    print(f"  Crater target repos (declared in targets.json): {len(crater_targets_index)}")
    print(f"  Failed-repo entries (failed_repos.json): {len(failed_repos_index)}")


if __name__ == "__main__":
    main()
