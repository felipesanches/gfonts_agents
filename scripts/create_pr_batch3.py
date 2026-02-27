#!/usr/bin/env python3
"""
Create per-family commits for a new PR to google/fonts.
Reads family data from /tmp/pr_ready_families.txt.
Each commit adds/fixes source metadata in METADATA.pb and includes upstream_info.md.
"""

import os
import re
import subprocess
import sys
import tempfile

GOOGLE_FONTS_DIR = "/mnt/shared/google/fonts"
INVESTIGATIONS_DIR = "/home/fsanches/projetos/gfonts_agents/data/investigations/families"


def run_git(*args, capture=True, check=True):
    """Run a git command in the google/fonts repo."""
    cmd = ["git", "-C", GOOGLE_FONTS_DIR] + list(args)
    if capture:
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    else:
        subprocess.run(cmd, check=check)


def clean_paths(text):
    """Remove /mnt/shared prefixes from paths."""
    text = text.replace("/mnt/shared/upstream_repos/fontc_crater_cache/", "upstream_repos/fontc_crater_cache/")
    text = text.replace("/mnt/shared/google/fonts/", "google/fonts/")
    text = text.replace("/mnt/shared/google/fonts", "google/fonts")
    text = text.replace("/mnt/shared/", "")
    return text


def extract_repo_owner_name(url):
    """Extract owner/repo from a GitHub URL."""
    if not url:
        return None
    match = re.search(r'github\.com/([^/]+/[^/\s]+)', url)
    if match:
        return match.group(1).rstrip(')')
    return url


def parse_families(filepath):
    """Parse the pr_ready_families.txt file."""
    families = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) < 8:
                continue
            family = {
                "name": parts[0],
                "slug": parts[1],
                "metadata_dir": parts[2],
                "action": parts[3],
                "repo_url": parts[4],
                "commit": parts[5],
                "config_yaml_path": parts[6],
                "notes": parts[7] if len(parts) > 7 else "",
            }
            families.append(family)
    return families


def add_source_block(metadata_path, repo_url, commit, config_yaml=None):
    """Add a source{} block to METADATA.pb."""
    with open(metadata_path, "r") as f:
        content = f.read()

    if "source {" in content:
        print(f"  WARNING: source block already exists in {metadata_path}")
        return False

    lines = ['\nsource {']
    lines.append(f'  repository_url: "{repo_url}"')
    if commit:
        lines.append(f'  commit: "{commit}"')
    if config_yaml and config_yaml != "override":
        lines.append(f'  config_yaml: "{config_yaml}"')
    lines.append('}')
    source_block = '\n'.join(lines) + '\n'

    content = content.rstrip() + source_block

    with open(metadata_path, "w") as f:
        f.write(content)
    return True


def add_commit_to_source(metadata_path, commit):
    """Add commit field to existing source{} block."""
    with open(metadata_path, "r") as f:
        content = f.read()

    if "source {" not in content:
        print(f"  WARNING: no source block in {metadata_path}")
        return False

    if 'commit: "' in content:
        print(f"  WARNING: commit field already exists")
        return False

    lines = content.split("\n")
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and "repository_url:" in line:
            new_lines.append(f'  commit: "{commit}"')
            inserted = True

    if not inserted:
        print(f"  WARNING: could not find repository_url line")
        return False

    with open(metadata_path, "w") as f:
        f.write("\n".join(new_lines))
    return True


def fix_commit_in_source(metadata_path, new_commit):
    """Replace existing commit hash in the source{} block."""
    with open(metadata_path, "r") as f:
        content = f.read()

    match = re.search(r'commit: "([a-f0-9]+)"', content)
    if not match:
        print(f"  WARNING: no commit field found in source block")
        return False

    old_commit = match.group(1)
    content = content.replace(f'commit: "{old_commit}"', f'commit: "{new_commit}"')

    with open(metadata_path, "w") as f:
        f.write(content)
    print(f"  Replaced commit {old_commit[:8]} -> {new_commit[:8]}")
    return True


def fix_config_in_source(metadata_path, new_config_path):
    """Fix or add config_yaml field in existing source{} block."""
    with open(metadata_path, "r") as f:
        content = f.read()

    if "source {" not in content:
        print(f"  WARNING: no source block in {metadata_path}")
        return False

    # Check if config_yaml already exists
    if 'config_yaml:' in content:
        # Replace existing
        content = re.sub(r'config_yaml: "[^"]*"', f'config_yaml: "{new_config_path}"', content)
        print(f"  Replaced config_yaml -> {new_config_path}")
    else:
        # Add after last field in source block (before closing })
        # Find the source block and add config_yaml before the closing }
        lines = content.split("\n")
        new_lines = []
        in_source = False
        added = False
        for line in lines:
            if "source {" in line:
                in_source = True
            if in_source and line.strip() == "}" and not added:
                new_lines.append(f'  config_yaml: "{new_config_path}"')
                added = True
                in_source = False
            new_lines.append(line)

        if not added:
            print(f"  WARNING: could not add config_yaml")
            return False

        content = "\n".join(new_lines)
        print(f"  Added config_yaml: {new_config_path}")

    with open(metadata_path, "w") as f:
        f.write(content)
    return True


def get_repo_url_from_metadata(metadata_path):
    """Read repository_url from METADATA.pb."""
    with open(metadata_path, "r") as f:
        content = f.read()
    match = re.search(r'repository_url: "([^"]+)"', content)
    return match.group(1) if match else ""


def generate_commit_message(family, repo_url_resolved):
    """Generate concise commit message following the policy."""
    name = family["name"]
    action = family["action"]

    if action in ("fix_commit", "fix_config"):
        verb = "fix source block in"
    elif action == "add_commit":
        verb = "add commit hash to"
    else:
        verb = "add source block to"

    repo_owner = extract_repo_owner_name(repo_url_resolved) or "unknown"
    short_hash = family["commit"][:8] if family["commit"] else "unknown"

    # Determine config line
    config_yaml_path = family["config_yaml_path"]
    config = "none"
    if config_yaml_path == "override":
        # Check if override config exists in google/fonts dir
        config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
        if os.path.exists(config_path):
            config = "override config.yaml in google/fonts"
        else:
            config = "none (override config needed)"
    elif config_yaml_path:
        config = config_yaml_path
    else:
        # Check if override config exists anyway
        config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
        if os.path.exists(config_path):
            config = "override config.yaml in google/fonts"

    # Determine status and confidence from notes
    status = "missing_config"
    confidence = "MEDIUM"

    # Parse notes for status hints
    notes = family["notes"]
    if config_yaml_path and config_yaml_path != "override":
        status = "complete"
        confidence = "HIGH"
    elif config_yaml_path == "override":
        config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
        if os.path.exists(config_path):
            status = "complete"
            confidence = "HIGH"

    if action == "fix_commit":
        status = "needs_correction"
        confidence = "HIGH"
    elif action == "fix_config":
        status = "needs_correction"
        confidence = "HIGH"

    lines = [
        f'{name}: {verb} METADATA.pb',
        '',
        f'- Repo: {repo_owner}',
        f'- Commit: {short_hash}',
        f'- Config: {config}',
        f'- Status: {status}',
        f'- Confidence: {confidence}',
    ]

    if notes and "should be" in notes:
        lines.append(f'Note: {notes}')

    return "\n".join(lines)


def main():
    # Parse families from the data file
    families = parse_families("/tmp/pr_ready_families.txt")
    print(f"Loaded {len(families)} families from pr_ready_families.txt")

    # Filter out families with missing essential data
    valid_families = []
    for f in families:
        if f["action"] == "add_source_block" and (not f["repo_url"] or not f["commit"]):
            if not f["repo_url"]:
                print(f"  SKIP {f['name']}: no repo URL")
            elif not f["commit"]:
                print(f"  SKIP {f['name']}: no commit hash")
            continue
        if f["action"] == "add_commit" and not f["commit"]:
            print(f"  SKIP {f['name']}: no commit hash for add_commit")
            continue
        if f["action"] == "fix_commit" and not f["commit"]:
            print(f"  SKIP {f['name']}: no new commit hash for fix_commit")
            continue
        valid_families.append(f)

    print(f"\n{len(valid_families)} families to process (skipped {len(families) - len(valid_families)})")

    # Verify we're on the right branch
    current = run_git("branch", "--show-current")
    print(f"Current branch: {current}")
    if current != "sources_per_family_2026-02-27":
        print("ERROR: not on the expected branch")
        sys.exit(1)

    processed = 0
    skipped = 0

    for i, family in enumerate(valid_families):
        name = family["name"]
        slug = family["slug"]
        metadata_dir = family["metadata_dir"]
        action = family["action"]
        print(f"\n[{i+1}/{len(valid_families)}] {name} ({action})")

        metadata_path = os.path.join(GOOGLE_FONTS_DIR, metadata_dir, "METADATA.pb")
        if not os.path.exists(metadata_path):
            print(f"  ERROR: {metadata_path} not found, skipping")
            skipped += 1
            continue

        # Read investigation report
        report_path = os.path.join(INVESTIGATIONS_DIR, f"{slug}.md")
        if not os.path.exists(report_path):
            print(f"  ERROR: no report at {report_path}, skipping")
            skipped += 1
            continue

        with open(report_path, "r") as f:
            report_text = f.read()

        # Get repo URL (from data or METADATA.pb)
        repo_url = family["repo_url"]
        if not repo_url and action in ("fix_commit", "fix_config"):
            repo_url = get_repo_url_from_metadata(metadata_path)

        # Apply METADATA.pb changes
        success = False
        if action == "add_source_block":
            config = family["config_yaml_path"] if family["config_yaml_path"] != "override" else None
            success = add_source_block(metadata_path, family["repo_url"], family["commit"], config)
        elif action == "add_commit":
            success = add_commit_to_source(metadata_path, family["commit"])
        elif action == "fix_commit":
            success = fix_commit_in_source(metadata_path, family["commit"])
        elif action == "fix_config":
            success = fix_config_in_source(metadata_path, family["config_yaml_path"])

        if not success:
            print(f"  Skipping due to error above")
            run_git("checkout", "--", metadata_dir, capture=False, check=False)
            skipped += 1
            continue

        # Write upstream_info.md
        cleaned_report = clean_paths(report_text)
        upstream_info_path = os.path.join(GOOGLE_FONTS_DIR, metadata_dir, "upstream_info.md")
        with open(upstream_info_path, "w") as f:
            f.write(cleaned_report)
        print(f"  Wrote upstream_info.md")

        # Generate commit message
        commit_msg = generate_commit_message(family, repo_url)
        print(f"  Message: {commit_msg.split(chr(10))[0]}")

        # Write temp file for commit message
        msg_file = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
        msg_file.write(commit_msg)
        msg_file.close()

        # Stage and commit
        run_git("add", os.path.join(metadata_dir, "METADATA.pb"))
        run_git("add", os.path.join(metadata_dir, "upstream_info.md"))
        run_git("commit", "-F", msg_file.name, capture=False)

        os.unlink(msg_file.name)
        processed += 1

    print(f"\n{'=' * 60}")
    print(f"Done! Processed: {processed}, Skipped: {skipped}")
    print(f"Total commits on branch: {run_git('rev-list', '--count', 'upstream/main..HEAD')}")


if __name__ == "__main__":
    main()
