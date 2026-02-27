#!/usr/bin/env python3
"""
Create per-family commits for batch4 PR to google/fonts.
Reads family data from /tmp/pr_ready_batch4.txt.
Each commit adds/fixes source metadata in METADATA.pb and includes upstream_info.md.
Branch: sources_per_family_batch4_2026-02-27
"""

import os
import re
import subprocess
import sys
import tempfile

GOOGLE_FONTS_DIR = "/mnt/shared/google/fonts"
INVESTIGATIONS_DIR = "/home/fsanches/projetos/gfonts_agents/data/investigations/families"
BRANCH_NAME = "sources_per_family_batch4_2026-02-27"
INPUT_FILE = "/tmp/pr_ready_batch4.txt"


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


def is_valid_commit(commit):
    """Check if a string is a valid commit hash."""
    if not commit:
        return False
    if commit.lower() in ("none", "n/a", "unknown", ""):
        return False
    return bool(re.match(r'^[a-f0-9]{7,40}$', commit))


def parse_families(filepath):
    """Parse the pr_ready families file."""
    families = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('FAMILY_NAME'):
                continue
            parts = line.split('|')
            if len(parts) < 7:
                continue
            family = {
                "name": parts[0].strip(),
                "slug": parts[1].strip(),
                "metadata_dir": parts[2].strip(),
                "action": parts[3].strip(),
                "repo_url": parts[4].strip(),
                "commit": parts[5].strip(),
                "config_yaml_path": parts[6].strip(),
                "notes": parts[7].strip() if len(parts) > 7 else "",
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
    if is_valid_commit(commit):
        lines.append(f'  commit: "{commit}"')
    if config_yaml and config_yaml not in ("none", "override", ""):
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

    if not is_valid_commit(commit):
        print(f"  ERROR: invalid commit hash: {commit}")
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

    if not is_valid_commit(new_commit):
        print(f"  ERROR: invalid target commit hash: {new_commit}")
        return False

    match = re.search(r'commit: "([a-f0-9]+)"', content)
    if not match:
        print(f"  WARNING: no commit field found in source block")
        return False

    old_commit = match.group(1)
    if old_commit == new_commit:
        print(f"  WARNING: commit already matches target {new_commit[:8]}")
        return False

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

    if not new_config_path or new_config_path in ("none", "override", ""):
        print(f"  ERROR: invalid config path: {new_config_path}")
        return False

    if 'config_yaml:' in content:
        content = re.sub(r'config_yaml: "[^"]*"', f'config_yaml: "{new_config_path}"', content)
        print(f"  Replaced config_yaml -> {new_config_path}")
    else:
        lines = content.split("\n")
        new_lines = []
        in_source = False
        added = False
        depth = 0
        for line in lines:
            if "source {" in line:
                in_source = True
                depth = 1
            elif in_source:
                if "{" in line:
                    depth += 1
                if "}" in line:
                    depth -= 1
                    if depth == 0 and not added:
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


def generate_commit_message(family, action):
    """Generate concise commit message following the policy."""
    name = family["name"]
    repo_url = family["repo_url"]
    commit = family["commit"]
    config_yaml_path = family["config_yaml_path"]

    if action in ("fix_commit", "fix_config"):
        verb = "fix source block in"
    elif action == "add_commit":
        verb = "add commit hash to"
    else:
        verb = "add source block to"

    repo_owner = extract_repo_owner_name(repo_url) or "unknown"
    short_hash = commit[:8] if is_valid_commit(commit) else "unknown"

    # Determine config line
    config = "none"
    if config_yaml_path == "override":
        config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
        if os.path.exists(config_path):
            config = "override config.yaml in google/fonts"
        else:
            config = "none (override config needed)"
    elif config_yaml_path and config_yaml_path not in ("none", ""):
        config = config_yaml_path
    else:
        config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
        if os.path.exists(config_path):
            config = "override config.yaml in google/fonts"

    # Determine status and confidence
    if action == "fix_commit":
        status = "needs_correction"
        confidence = "HIGH"
    elif action == "fix_config":
        status = "needs_correction"
        confidence = "HIGH"
    elif action == "add_commit":
        if config not in ("none", "none (override config needed)"):
            status = "complete"
        else:
            status = "missing_config"
        confidence = "HIGH"
    else:  # add_source_block
        if is_valid_commit(commit):
            if config not in ("none", "none (override config needed)"):
                status = "complete"
            else:
                status = "missing_config"
        else:
            status = "missing_config"
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

    return "\n".join(lines)


def setup_branch():
    """Ensure we're on the correct branch, creating it if needed."""
    # Fetch upstream
    print("Fetching upstream...")
    run_git("fetch", "upstream", capture=False)

    # Check if branch exists
    existing = run_git("branch", "--list", BRANCH_NAME)
    if existing:
        # Switch to it
        run_git("checkout", BRANCH_NAME, capture=False)
        print(f"Switched to existing branch: {BRANCH_NAME}")
    else:
        # Create from upstream/main
        run_git("checkout", "-b", BRANCH_NAME, "upstream/main", capture=False)
        print(f"Created new branch: {BRANCH_NAME}")

    current = run_git("branch", "--show-current")
    if current != BRANCH_NAME:
        print(f"ERROR: Expected branch {BRANCH_NAME}, got {current}")
        sys.exit(1)


def main():
    families = parse_families(INPUT_FILE)
    print(f"Loaded {len(families)} families from {INPUT_FILE}")

    # Filter invalid entries
    valid_families = []
    for f in families:
        if not f["name"] or not f["slug"]:
            print(f"  SKIP: empty name/slug")
            continue
        if not f["repo_url"]:
            print(f"  SKIP {f['name']}: no repo URL")
            continue
        if f["action"] == "add_commit" and not is_valid_commit(f["commit"]):
            print(f"  SKIP {f['name']}: add_commit but invalid commit: {f['commit']}")
            continue
        if f["action"] == "fix_commit" and not is_valid_commit(f["commit"]):
            print(f"  SKIP {f['name']}: fix_commit but invalid commit: {f['commit']}")
            continue
        valid_families.append(f)

    print(f"\n{len(valid_families)} families to process")

    # Setup branch
    setup_branch()

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

        # Apply METADATA.pb changes
        success = False
        config_for_add = family["config_yaml_path"]
        if config_for_add in ("none", "override", ""):
            config_for_add = None

        if action == "add_source_block":
            success = add_source_block(metadata_path, family["repo_url"], family["commit"], config_for_add)
        elif action == "add_commit":
            success = add_commit_to_source(metadata_path, family["commit"])
            # Also add config_yaml if provided
            if success and config_for_add:
                fix_config_in_source(metadata_path, config_for_add)
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
        commit_msg = generate_commit_message(family, action)
        print(f"  Message: {commit_msg.split(chr(10))[0]}")

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
    total_commits = run_git("rev-list", "--count", "upstream/main..HEAD")
    print(f"Total commits on branch: {total_commits}")
    print(f"\nNext: push and open PR:")
    print(f"  git -C {GOOGLE_FONTS_DIR} push felipesanches {BRANCH_NAME}")


if __name__ == "__main__":
    main()
