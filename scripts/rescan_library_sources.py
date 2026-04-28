#!/usr/bin/env python3
"""Rescan all METADATA.pb files under the canonical gfonts clone and refresh
data/gfonts_library_sources.json with current source-block + override-config
state.

Fields that come from disk (refreshed):
  path, family_name, designer, license, repository_url, commit, branch,
  config_yaml, override_config, has_source_block, has_investigation_report

Fields that are managed elsewhere (preserved):
  reproducible_build (set by build_registry.json via sync_dashboard.py),
  status (recomputed below from the disk-derived fields + reproducible_build),
  date_added (preserved from existing entry; sourced from METADATA.pb if new).

Usage: python3 scripts/rescan_library_sources.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from collections import Counter

GFONTS = Path("/home/fsanches/compartilhado/gfonts")
LICENSE_DIRS = ("ofl", "apache", "ufl")
SOURCES = Path(__file__).resolve().parent.parent / "data" / "gfonts_library_sources.json"


def parse_metadata(text: str) -> dict:
    """Extract the fields we care about from METADATA.pb text."""
    out = {}
    for key in ("name", "designer", "license", "date_added"):
        m = re.search(rf'^{key}\s*:\s*"([^"]*)"', text, re.M)
        if m:
            out[key] = m.group(1)
    src_match = re.search(r"source\s*\{(.*?)\n\}", text, re.S)
    if src_match:
        body = src_match.group(1)
        out["has_source_block"] = True
        for key in ("repository_url", "commit", "branch", "config_yaml"):
            m = re.search(rf'{key}\s*:\s*"([^"]*)"', body)
            if m:
                out[key] = m.group(1)
    else:
        out["has_source_block"] = False
    return out


def determine_status(entry: dict) -> str:
    """Status reflects the *enrichment* state of the source block.
    Mirrors the historical rule used by Felipe's earlier regen runs."""
    if not entry.get("has_source_block"):
        return "no_source"
    if not entry.get("repository_url"):
        return "no_source"
    if not entry.get("commit"):
        return "missing_commit"
    if not entry.get("config_yaml") and not entry.get("override_config"):
        return "missing_config"
    return "complete"


def rescan() -> dict:
    """Walk the disk and build the families list."""
    families = []
    for license_dir in LICENSE_DIRS:
        ldir = GFONTS / license_dir
        if not ldir.is_dir():
            continue
        for fam_dir in sorted(ldir.iterdir()):
            md_path = fam_dir / "METADATA.pb"
            if not md_path.is_file():
                continue
            try:
                text = md_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"WARN: failed to read {md_path}: {e}", file=sys.stderr)
                continue
            md = parse_metadata(text)
            entry = {
                "path": f"{license_dir}/{fam_dir.name}/METADATA.pb",
                "family_name": md.get("name", ""),
                "designer": md.get("designer", ""),
                "license": md.get("license", ""),
                "repository_url": md.get("repository_url", ""),
                "commit": md.get("commit", ""),
                "branch": md.get("branch", ""),
                "config_yaml": md.get("config_yaml", ""),
                "override_config": (fam_dir / "config.yaml").is_file(),
                "has_source_block": md.get("has_source_block", False),
                "has_investigation_report": (fam_dir / "upstream_info.md").is_file(),
                "date_added": md.get("date_added", ""),
            }
            entry["status"] = determine_status(entry)
            families.append(entry)
    return families


def merge_with_existing(new_families: list, existing: dict) -> list:
    """Preserve `reproducible_build` from existing entries (keyed by path).
    For new families that didn't exist before, leave it unset."""
    by_path = {f["path"]: f for f in existing.get("families", [])}
    for f in new_families:
        prev = by_path.get(f["path"])
        if prev:
            f["reproducible_build"] = prev.get("reproducible_build", "")
            # Preserve date_added if METADATA.pb didn't have it
            if not f.get("date_added"):
                f["date_added"] = prev.get("date_added", "")
        else:
            f["reproducible_build"] = ""
    # Order families by path for stability
    new_families.sort(key=lambda x: x["path"])
    return new_families


def compute_summary(families: list) -> dict:
    s = Counter()
    s["total_families"] = len(families)
    s["total"] = len(families)
    for f in families:
        if f.get("has_source_block"):
            s["has_source_block"] += 1
            s["with_source_block"] += 1
        if f.get("repository_url"):
            s["has_repo_url"] += 1
        if f.get("commit"):
            s["has_commit"] += 1
        if f.get("config_yaml"):
            s["with_config_yaml"] += 1
        if f.get("override_config"):
            s["override_configs"] += 1
        if f.get("has_investigation_report"):
            s["with_investigation_report"] += 1
            s["investigation_reports"] += 1
        st = f.get("status", "")
        if st == "complete":
            s["complete"] += 1
        elif st == "missing_config":
            s["missing_config"] += 1
        elif st == "missing_commit":
            s["missing_commit"] += 1
        elif st == "no_source":
            s["no_source"] += 1
        elif st == "needs_correction":
            s["needs_correction"] += 1
    s["no_upstream_repo"] = 0
    return dict(s)


def main():
    existing = json.loads(SOURCES.read_text())

    print(f"Rescanning METADATA.pb under {GFONTS}/{{{','.join(LICENSE_DIRS)}}}...", file=sys.stderr)
    new_families = rescan()
    print(f"Found {len(new_families)} families", file=sys.stderr)

    merged = merge_with_existing(new_families, existing)
    summary = compute_summary(merged)

    # Diff vs existing
    old_summary = existing.get("summary", {})
    print("\n=== Summary changes ===", file=sys.stderr)
    for key in sorted(set(summary.keys()) | set(old_summary.keys())):
        ov = old_summary.get(key, 0)
        nv = summary.get(key, 0)
        delta = nv - ov
        marker = " " if delta == 0 else ("+" if delta > 0 else "-")
        if delta != 0:
            print(f"  {key:32s} {ov:5d} -> {nv:5d} ({marker}{abs(delta)})", file=sys.stderr)

    # Build the new structure preserving top-level metadata fields
    out = dict(existing)
    out["families"] = merged
    out["summary"] = summary
    from datetime import datetime, timezone
    out["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out["generated_at"] = out["last_updated"]
    out["last_updated_gfonts_commit"] = subprocess.check_output(
        ["git", "-C", str(GFONTS), "rev-parse", "HEAD"], text=True).strip()

    SOURCES.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {SOURCES}", file=sys.stderr)
    print(f"At gfonts commit: {out['last_updated_gfonts_commit'][:9]}", file=sys.stderr)


if __name__ == "__main__":
    main()
