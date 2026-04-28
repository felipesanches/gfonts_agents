#!/usr/bin/env python3
"""Compute the numbers shown on the dashboard's *visible* tabs (Home + Crater
Coverage Detail) directly from the underlying JSON files.

Single source of truth for these numbers: this script and the
classifyMissingFamily JS function MUST agree. Any divergence means a bug.

Usage:
    python3 scripts/dashboard_visible_metrics.py            # human-readable
    python3 scripts/dashboard_visible_metrics.py --json     # machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "data" / "gfonts_library_sources.json"
CRATER = ROOT / "data" / "fontc_crater_analysis.json"


def normalize_repo_url(url: str) -> str:
    if not url:
        return ""
    u = str(url).strip().rstrip("/").lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    u = re.sub(r"^github\.com/", "", u)
    u = re.sub(r"\.git$", "", u)
    return u


def classify_missing(f: dict, crater_targets: dict, failed_index: dict) -> str:
    """Mirror of js/main.js:classifyMissingFamily."""
    has_url = bool(f.get("repository_url"))
    has_source = f.get("has_source_block") is True
    has_commit = bool(f.get("commit"))
    has_config = bool(f.get("config_yaml")) or f.get("override_config") is True
    rb = f.get("reproducible_build", "")
    repo = (f.get("repository_url") or "").lower()
    norm = normalize_repo_url(f.get("repository_url") or "")

    if norm and norm in failed_index:
        return "target_resolution_failed"
    if norm and norm in crater_targets:
        return "submitted_pending"
    if not has_source or not has_url:
        return "no_source"
    if "googlefontdirectory-hg" in repo or rb == "legacy-no-modern-source":
        return "legacy_sources"
    if not has_commit:
        return "no_commit"
    if not has_config:
        return "missing_config"
    return "ready_to_submit"


def compute() -> dict:
    sources = json.loads(SOURCES.read_text())
    crater = json.loads(CRATER.read_text())

    crater_index = crater.get("crater_sources", {}) or {}
    crater_targets = crater.get("crater_targets", {}) or {}
    failed_index = crater.get("failed_repos_index", {}) or {}
    crater_repo_set = set(crater_index.keys())
    families = sources.get("families", []) or []

    covered = []
    missing = []
    for f in families:
        norm = normalize_repo_url(f.get("repository_url") or "")
        if norm and norm in crater_repo_set:
            covered.append(f)
        else:
            missing.append(f)

    by_reason = Counter()
    for f in missing:
        by_reason[classify_missing(f, crater_targets, failed_index)] += 1

    total = len(families)
    return {
        "total": total,
        "covered": len(covered),
        "missing": len(missing),
        "coverage_pct": (100 * len(covered) / total) if total else 0,
        "missing_breakdown": dict(by_reason),
        "gfonts_commit": sources.get("last_updated_gfonts_commit", ""),
        "sources_last_updated": sources.get("last_updated", sources.get("generated_at", "")),
        "crater_latest_run": (crater.get("_metadata") or {}).get("latest_run", ""),
        "crater_generated": (crater.get("_metadata") or {}).get("generated", ""),
        "crater_fontc_rev": (crater.get("_metadata") or {}).get("fontc_rev", ""),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    args = ap.parse_args()

    metrics = compute()

    if args.json:
        json.dump(metrics, sys.stdout, indent=2)
        print()
        return 0

    print("=== Dashboard visible metrics (Home tab) ===")
    print(f"  Total families:    {metrics['total']:>5d}")
    print(f"  In Crater:         {metrics['covered']:>5d}")
    print(f"  Not in Crater:     {metrics['missing']:>5d}")
    print(f"  Coverage:          {metrics['coverage_pct']:>5.1f}%")
    print()
    print("=== Not in Crater — breakdown by next action ===")
    order = ["target_resolution_failed", "submitted_pending", "ready_to_submit",
             "missing_config", "no_commit", "legacy_sources", "no_source"]
    for k in order:
        n = metrics["missing_breakdown"].get(k, 0)
        if n:
            print(f"  {k:30s} {n:>5d}")
    print()
    print(f"Refreshed from gfonts commit {metrics['gfonts_commit'][:9]}")
    print(f"Crater run: {metrics['crater_latest_run']} (fontc rev {metrics['crater_fontc_rev']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
