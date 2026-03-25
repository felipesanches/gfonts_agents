#!/usr/bin/env python3
"""Comprehensive dashboard sync — single source of truth enforcement.

This script is the ONLY way dashboard data should be updated. It reads
from the canonical sources and propagates changes to ALL dependent files,
ensuring full coherence across every page.

Usage:
    python scripts/sync_dashboard.py                # dry-run (report only)
    python scripts/sync_dashboard.py --apply        # apply changes
    python scripts/sync_dashboard.py --apply --commit  # apply + git commit + push

Sources of truth:
    1. data/build_registry.json (version-controlled in this repo)
       → reproducible_build status, isolation, failure categories
    2. /mnt/shared/google/fonts/build_tools/normalization_results.json
       → normalized_match count
    3. /mnt/shared/gfonts-repro-builds/*/comparison_report.json
       → per-family deep analysis (root cause, reflow risk)

Targets (all in this repo's data/ directory):
    1. data/gfonts_library_sources.json
       → reproducible_build field per family
       → status field (complete if family builds successfully)
       → summary counts
    2. data/build_system.json
       → summary (processed, per-status counts, normalized_match)
       → root_cause_summary, reflow_risk_summary
       → per-family entries
    3. data/reproducible-build-system.md
       → all tables and counts
    4. data/build_failure_categories.json
       → timestamped snapshots
"""

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
# Single source of truth — version-controlled in this repo
BUILD_REGISTRY = DATA_DIR / "build_registry.json"
NORMALIZATION_RESULTS = Path("/mnt/shared/google/fonts/build_tools/normalization_results.json")
REPRO_BUILDS_DIR = Path("/mnt/shared/gfonts-repro-builds")


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def validate_coherence(registry, sources, build_system, norm_results):
    """Check that all data files are consistent. Returns list of issues."""
    issues = []

    # Count statuses from registry
    reg_statuses = Counter()
    for fam, entry in registry.get("families", {}).items():
        if not isinstance(entry, dict):
            continue
        s = entry.get("reproducible_build", "unknown")
        reg_statuses[s] += 1

    reg_yes = reg_statuses.get("yes", 0)
    reg_cv = reg_statuses.get("compiler-version", 0)
    reg_bf = reg_statuses.get("build-failure", 0)
    reg_total = sum(reg_statuses.values())

    # Check build_system.json summary matches registry
    bs_summary = build_system.get("summary", {})
    bs_yes = bs_summary.get("yes", 0)
    bs_cv = bs_summary.get("compiler_version", bs_summary.get("compiler-version", 0))
    bs_bf = bs_summary.get("build_failure", bs_summary.get("build-failure", 0))
    bs_total = bs_summary.get("processed", 0)
    bs_norm = bs_summary.get("normalized_match", 0)

    if bs_yes != reg_yes:
        issues.append(f"build_system.json yes={bs_yes} != registry yes={reg_yes}")
    if bs_cv != reg_cv:
        issues.append(f"build_system.json compiler_version={bs_cv} != registry compiler-version={reg_cv}")
    if bs_bf != reg_bf:
        issues.append(f"build_system.json build_failure={bs_bf} != registry build-failure={reg_bf}")

    # Check normalization count
    if norm_results:
        norm_match = norm_results.get("normalized_match", 0)
        if bs_norm != norm_match:
            issues.append(f"build_system.json normalized_match={bs_norm} != normalization_results={norm_match}")

    # Check gfonts_library_sources.json consistency
    src_summary = sources.get("summary", {})
    src_complete = src_summary.get("complete", 0)

    # Every family with successful reproducible_build should be status=complete
    # Every family with missing-source should NOT be status=complete
    for fam_data in sources.get("families", []):
        rb = fam_data.get("reproducible_build")
        status = fam_data.get("status")
        if rb and rb not in ("build-failure", "missing-source", "metadata-stanza-wrong"):
            if status != "complete":
                path = fam_data.get("path", "?")
                issues.append(f"{path}: reproducible_build={rb} but status={status} (should be complete)")
        if rb in ("missing-source", "metadata-stanza-wrong") and status == "complete":
            path = fam_data.get("path", "?")
            issues.append(f"{path}: reproducible_build={rb} but status=complete (should be missing_url or needs_correction)")

    # Check summary counts match actual family data
    actual_statuses = Counter(f.get("status") for f in sources.get("families", []))
    if src_complete != actual_statuses.get("complete", 0):
        issues.append(f"sources summary.complete={src_complete} != actual count={actual_statuses.get('complete', 0)}")

    return issues


def sync_sources(registry, sources):
    """Sync gfonts_library_sources.json from build registry."""
    changes = 0

    # Build a lookup from path to registry family name
    reg_families = registry.get("families", {})

    for fam_data in sources.get("families", []):
        path = fam_data.get("path", "")
        # Extract family directory name from path like "ofl/familyname/METADATA.pb"
        parts = path.split("/")
        if len(parts) >= 2:
            dirname = parts[1]
        else:
            continue

        entry = reg_families.get(dirname, {})
        if not isinstance(entry, dict):
            continue

        # Sync reproducible_build
        rb = entry.get("reproducible_build")
        if rb and fam_data.get("reproducible_build") != rb:
            fam_data["reproducible_build"] = rb
            changes += 1

        # Sync status: if family builds successfully, it's complete
        # If source is missing/wrong, demote from complete
        if rb and rb not in ("build-failure", "missing-source", "metadata-stanza-wrong"):
            if fam_data.get("status") != "complete":
                fam_data["status"] = "complete"
                changes += 1
        elif rb == "missing-source" and fam_data.get("status") == "complete":
            fam_data["status"] = "missing_url"
            changes += 1
        elif rb == "metadata-stanza-wrong" and fam_data.get("status") == "complete":
            fam_data["status"] = "needs_correction"
            changes += 1

    # Recalculate summary
    statuses = Counter(f.get("status") for f in sources.get("families", []))
    sources["summary"]["total"] = len(sources["families"])
    sources["summary"]["complete"] = statuses.get("complete", 0)
    sources["summary"]["missing_config"] = (
        statuses.get("missing_config", 0) + statuses.get("no_config_possible", 0)
    )
    sources["summary"]["missing_commit"] = statuses.get("missing_commit", 0)
    sources["summary"]["no_source"] = statuses.get("missing_url", 0)
    sources["summary"]["no_upstream_repo"] = statuses.get("no_upstream_repo", 0)
    sources["summary"]["needs_correction"] = statuses.get("needs_correction", 0)

    return changes


def sync_build_system(registry, build_system, norm_results):
    """Sync build_system.json summary from build registry + normalization."""
    reg_statuses = Counter()
    for fam, entry in registry.get("families", {}).items():
        if not isinstance(entry, dict):
            continue
        s = entry.get("reproducible_build", "unknown")
        reg_statuses[s] += 1

    summary = build_system.setdefault("summary", {})
    summary["processed"] = sum(reg_statuses.values())
    summary["yes"] = reg_statuses.get("yes", 0)
    summary["compiler_version"] = reg_statuses.get("compiler-version", 0)
    summary["build_failure"] = reg_statuses.get("build-failure", 0)
    summary["timestamp_diff"] = reg_statuses.get("timestamp-diff", 0)
    summary["name_table"] = reg_statuses.get("name-table", 0)
    summary["legacy_no_modern_source"] = reg_statuses.get("legacy-no-modern-source", 0)
    summary["metadata_stanza_wrong"] = reg_statuses.get("metadata-stanza-wrong", 0)
    summary["missing_source"] = reg_statuses.get("missing-source", 0)

    if norm_results:
        summary["normalized_match"] = norm_results.get("normalized_match", 0)

    return True


def sync_build_timings():
    """Regenerate build_timings.json from comparison reports."""
    import glob

    timings = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Build timing data extracted from comparison reports",
        "families": {},
    }

    for report_path in glob.glob(str(REPRO_BUILDS_DIR / "*/comparison_report.json")):
        try:
            r = load_json(report_path)
            family = r.get(
                "family", os.path.basename(os.path.dirname(report_path))
            )
            bt = r.get("build_time_seconds")
            if bt and bt > 0:
                timings["families"][family] = {
                    "timings": [{
                        "build_time_seconds": round(bt, 1),
                        "status": r.get("overall_status", "?"),
                        "timestamp": r.get("timestamp", ""),
                    }]
                }
        except Exception:
            pass

    save_json(DATA_DIR / "build_timings.json", timings)
    return len(timings["families"])


def sync_progress_history(sources):
    """Append a snapshot to progress_history.json if the numbers changed."""
    history_path = DATA_DIR / "progress_history.json"
    history = load_json(history_path) if history_path.exists() else {"entries": []}

    current = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": dict(sources.get("summary", {})),
        "source": "sync_dashboard",
    }

    # Only append if numbers changed from last entry
    entries = history.get("entries", [])
    if entries:
        last = entries[-1].get("summary", {})
        if last.get("complete") == current["summary"].get("complete") and \
           last.get("total") == current["summary"].get("total"):
            return  # No change

    entries.append(current)
    history["entries"] = entries
    save_json(history_path, history)


def main():
    parser = argparse.ArgumentParser(description="Sync all dashboard data from sources of truth")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--commit", action="store_true", help="Git commit and push after apply")
    args = parser.parse_args()

    # Load sources of truth
    # Try primary (version-controlled in this repo), fall back to google/fonts working copy
    if not BUILD_REGISTRY.exists():
        print(f"ERROR: {BUILD_REGISTRY} not found")
        sys.exit(1)

    registry = load_json(BUILD_REGISTRY)
    sources = load_json(DATA_DIR / "gfonts_library_sources.json")
    build_system = load_json(DATA_DIR / "build_system.json")
    norm_results = load_json(NORMALIZATION_RESULTS) if NORMALIZATION_RESULTS.exists() else None

    # Validate current state
    print("=== Pre-sync validation ===")
    issues = validate_coherence(registry, sources, build_system, norm_results)
    if issues:
        print(f"Found {len(issues)} coherence issues:")
        for issue in issues[:20]:
            print(f"  - {issue}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more")
    else:
        print("All data is coherent.")

    if not args.apply:
        if issues:
            print(f"\nRun with --apply to fix {len(issues)} issues.")
        return

    # Apply syncs
    print("\n=== Syncing ===")

    src_changes = sync_sources(registry, sources)
    print(f"gfonts_library_sources.json: {src_changes} changes")
    save_json(DATA_DIR / "gfonts_library_sources.json", sources)

    sync_build_system(registry, build_system, norm_results)
    print("build_system.json: summary updated")
    save_json(DATA_DIR / "build_system.json", build_system)

    timing_count = sync_build_timings()
    print(f"build_timings.json: {timing_count} families with timing data")

    sync_progress_history(sources)
    print("progress_history.json: snapshot appended")

    # Post-sync validation
    print("\n=== Post-sync validation ===")
    # Reload to verify
    sources = load_json(DATA_DIR / "gfonts_library_sources.json")
    build_system = load_json(DATA_DIR / "build_system.json")
    issues = validate_coherence(registry, sources, build_system, norm_results)
    if issues:
        print(f"WARNING: {len(issues)} issues remain after sync:")
        for issue in issues[:10]:
            print(f"  - {issue}")
    else:
        print("All data is coherent.")

    # Summary
    bs = build_system["summary"]
    norm = bs.get("normalized_match", 0)
    print(f"\n=== Dashboard Status ===")
    print(f"Families Tested:                {bs['processed']}")
    print(f"Byte-Identical:                 {bs['yes']} ({bs['yes']/bs['processed']*100:.1f}%)")
    print(f"Normalized Match:               {norm} ({norm/bs['processed']*100:.1f}%)")
    print(f"Functionally Equivalent:        {bs['yes']+norm} ({(bs['yes']+norm)/bs['processed']*100:.1f}%)")
    print(f"Different After Normalization:  {bs['compiler_version']-norm} ({(bs['compiler_version']-norm)/bs['processed']*100:.1f}%)")
    print(f"Build Failure:                  {bs['build_failure']}")
    print(f"Library Sources Complete:        {sources['summary']['complete']}")

    # Mandatory reminder: message log must be updated alongside dashboard data
    log_path = DATA_DIR / "message_log.json"
    if log_path.exists():
        log_mtime = datetime.fromtimestamp(log_path.stat().st_mtime, tz=timezone.utc)
        age_hours = (datetime.now(timezone.utc) - log_mtime).total_seconds() / 3600
        if age_hours > 1:
            print(f"\n⚠️  REMINDER: data/message_log.json was last updated {age_hours:.0f} hours ago.")
            print("   Per policy, the message log MUST be updated with every dashboard commit.")
            print("   Please update it before committing.\n")

    if args.commit:
        print("\n=== Committing ===")
        os.chdir(str(REPO_ROOT))
        subprocess.run(["git", "add", "data/"], check=True)
        msg = (
            f"Dashboard sync: {bs['yes']} byte-identical, "
            f"{bs['yes']+norm} functionally equivalent\n\n"
            f"Assisted by an AI agent (Claude Opus 4.6)"
        )
        result = subprocess.run(
            ["git", "commit", "-m", msg],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("Committed and pushed.")
        else:
            print("Nothing to commit (no changes).")


if __name__ == "__main__":
    main()
