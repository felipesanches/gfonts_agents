#!/usr/bin/env python3
"""
Scan upstream repos for config.yaml files for families with missing_config status.

For each of the ~870 families that already have repository_url and commit but
are missing config_yaml, this script:
1. Looks up the repo in the local cache
2. Checks out the recorded commit hash (using git show/ls-tree, non-destructive)
3. Searches for yaml files that look like gftools-builder configs
4. Also checks if google/fonts already has an override config.yaml
5. Records findings to data/config_yaml_scan_results.json
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

CACHE_BASE = "/mnt/shared/upstream_repos/fontc_crater_cache"
GFONTS_DIR = "/mnt/shared/gfonts"
TRACKING_FILE = "data/gfonts_library_sources.json"
RESULTS_FILE = "data/config_yaml_scan_results.json"

# Keys that indicate a gftools-builder config
GFTOOLS_KEYS = {
    "sources", "familyName", "buildVariable", "buildStatic", "buildOTF",
    "buildWebfont", "autohintTTF", "cleanUp", "removeOutlineOverlaps",
    "stat", "axisOrder", "includeSourceFixes", "logLevel",
    "buildSmallCap", "splitItalic", "expandFeaturesToInstances",
    "fvarInstanceAxisDflts", "recipeProvider",
}


def parse_github_url(url):
    """Extract owner/repo from a GitHub URL. Returns (owner, repo) or None."""
    if not url:
        return None
    # Normalize www.github.com -> github.com and strip trailing slashes
    url = url.rstrip("/")
    url = url.replace("www.github.com", "github.com")
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?$", url)
    if m:
        return m.group(1), m.group(2)
    return None


def list_files_at_commit(repo_path, commit):
    """List all files in a repo at a specific commit using git ls-tree."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "ls-tree", "-r", "--name-only", commit],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return None
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except (subprocess.TimeoutExpired, Exception):
        return None


def read_file_at_commit(repo_path, commit, file_path):
    """Read file content at a specific commit using git show."""
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "show", f"{commit}:{file_path}"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            return None
        return result.stdout
    except (subprocess.TimeoutExpired, Exception):
        return None


def is_gftools_config(content):
    """Check if YAML content looks like a gftools-builder configuration."""
    if not content:
        return False
    # Check for known gftools-builder keys
    found_keys = set()
    for line in content.split("\n"):
        line = line.strip()
        if ":" in line:
            key = line.split(":")[0].strip().lstrip("- ")
            if key in GFTOOLS_KEYS:
                found_keys.add(key)
    # Must have 'sources' key at minimum for it to be a valid gftools config
    return "sources" in found_keys


def find_configs_in_repo(repo_path, commit):
    """Find all gftools-builder config files in a repo at a given commit."""
    files = list_files_at_commit(repo_path, commit)
    if files is None:
        return None, "failed to list files"

    # Find candidate yaml files
    candidates = []
    for f in files:
        basename = os.path.basename(f).lower()
        if basename.endswith((".yaml", ".yml")):
            # Skip CI, github actions, and other non-config yamls
            lower_path = f.lower()
            if any(skip in lower_path for skip in [
                ".github/", ".ci/", "ci/", ".circleci/",
                ".travis", "crowdin", "codecov",
                ".pre-commit", "mkdocs", ".readthedocs",
            ]):
                continue
            candidates.append(f)

    # Check each candidate
    valid_configs = []
    for candidate in candidates:
        content = read_file_at_commit(repo_path, commit, candidate)
        if content and is_gftools_config(content):
            valid_configs.append(candidate)

    return valid_configs, None


def check_gfonts_override(family_path):
    """Check if the family directory in google/fonts has an override config.yaml."""
    family_dir = os.path.join(GFONTS_DIR, os.path.dirname(family_path))
    config_path = os.path.join(family_dir, "config.yaml")
    if os.path.isfile(config_path):
        return config_path
    return None


def main():
    with open(TRACKING_FILE) as f:
        data = json.load(f)

    families = data["families"]
    missing_config = [f for f in families if f.get("status") == "missing_config"]

    print(f"Scanning {len(missing_config)} families with missing_config status...")

    results = {
        "total_scanned": 0,
        "config_found": 0,
        "config_not_found": 0,
        "override_found": 0,
        "repo_not_in_cache": 0,
        "non_github": 0,
        "errors": 0,
        "families": [],
    }

    for i, family in enumerate(missing_config):
        family_name = family["family_name"]
        url = family.get("repository_url", "")
        commit = family.get("commit", "")
        path = family.get("path", "")

        result = {
            "family_name": family_name,
            "path": path,
            "repository_url": url,
            "commit": commit,
            "configs_found": [],
            "override_config": None,
            "status": None,
            "error": None,
        }

        results["total_scanned"] += 1

        # Check for override config in google/fonts
        override = check_gfonts_override(path)
        if override:
            result["override_config"] = override
            results["override_found"] += 1

        # Parse GitHub URL
        parsed = parse_github_url(url)
        if not parsed:
            result["status"] = "non_github"
            result["error"] = f"Non-GitHub or unparseable URL: {url}"
            results["non_github"] += 1
            results["families"].append(result)
            continue

        owner, repo = parsed
        repo_path = os.path.join(CACHE_BASE, owner, repo)

        if not os.path.isdir(repo_path):
            result["status"] = "not_in_cache"
            result["error"] = f"Repo not in cache: {repo_path}"
            results["repo_not_in_cache"] += 1
            results["families"].append(result)
            continue

        # Find configs at the recorded commit
        configs, error = find_configs_in_repo(repo_path, commit)
        if error:
            result["status"] = "error"
            result["error"] = error
            results["errors"] += 1
        elif configs:
            result["configs_found"] = configs
            result["status"] = "found"
            results["config_found"] += 1
        else:
            result["status"] = "not_found"
            results["config_not_found"] += 1

        results["families"].append(result)

        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(missing_config)}...")

    # Summary
    print(f"\nResults:")
    print(f"  Total scanned: {results['total_scanned']}")
    print(f"  Config found in upstream: {results['config_found']}")
    print(f"  Config NOT found: {results['config_not_found']}")
    print(f"  Override config in google/fonts: {results['override_found']}")
    print(f"  Repo not in cache: {results['repo_not_in_cache']}")
    print(f"  Non-GitHub URL: {results['non_github']}")
    print(f"  Errors: {results['errors']}")

    # Save results
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {RESULTS_FILE}")

    # Print breakdown of found configs
    found = [f for f in results["families"] if f["status"] == "found"]
    single_config = [f for f in found if len(f["configs_found"]) == 1]
    multi_config = [f for f in found if len(f["configs_found"]) > 1]
    print(f"\n  Single config: {len(single_config)}")
    print(f"  Multiple configs: {len(multi_config)}")

    if multi_config:
        print("\n  Families with multiple configs:")
        for f in multi_config[:20]:
            print(f"    {f['family_name']}: {f['configs_found']}")
        if len(multi_config) > 20:
            print(f"    ... and {len(multi_config) - 20} more")


if __name__ == "__main__":
    main()
