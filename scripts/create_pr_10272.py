#!/usr/bin/env python3
"""
Create per-family commits for a new PR to google/fonts.
Each commit adds/fixes source metadata in METADATA.pb and includes upstream_info.md.
"""

import os
import re
import subprocess
import sys
import tempfile

GOOGLE_FONTS_DIR = "/mnt/shared/google/fonts"
INVESTIGATIONS_DIR = "/home/fsanches/projetos/gfonts_agents/data/investigations/families"

# Family definitions: (family_name, slug, metadata_dir, action, changes)
# action: "add_source_block", "add_commit", "fix_commit", "fix_url"
FAMILIES = [
    # Category 1: Add commit hash to existing source block
    {
        "name": "DotGothic16",
        "slug": "dotgothic16",
        "metadata_dir": "ofl/dotgothic16",
        "action": "add_commit",
        "commit": "e44ca7bb46e7f353302c1431bf752af007c4fdfe",
        "status": "complete",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans",
        "slug": "encode-sans",
        "metadata_dir": "ofl/encodesans",
        "action": "add_commit",
        "commit": "6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans Condensed",
        "slug": "encode-sans-condensed",
        "metadata_dir": "ofl/encodesanscondensed",
        "action": "add_commit",
        "commit": "370cdccdb22daf862c6fca0636aad64b6835decd",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans Expanded",
        "slug": "encode-sans-expanded",
        "metadata_dir": "ofl/encodesansexpanded",
        "action": "add_commit",
        "commit": "370cdccdb22daf862c6fca0636aad64b6835decd",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans SC",
        "slug": "encode-sans-sc",
        "metadata_dir": "ofl/encodesanssc",
        "action": "add_commit",
        "commit": "6407de854a4dc3bfbe2160a11c5b57f5a1baf3bc",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans Semi Condensed",
        "slug": "encode-sans-semi-condensed",
        "metadata_dir": "ofl/encodesanssemicondensed",
        "action": "add_commit",
        "commit": "370cdccdb22daf862c6fca0636aad64b6835decd",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Encode Sans Semi Expanded",
        "slug": "encode-sans-semi-expanded",
        "metadata_dir": "ofl/encodesanssemiexpanded",
        "action": "add_commit",
        "commit": "370cdccdb22daf862c6fca0636aad64b6835decd",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Ek Mukta",
        "slug": "ek-mukta",
        "metadata_dir": "ofl/ekmukta",
        "action": "add_commit",
        "commit": "bccb1e2d95db0eea6be66e001edb2aeb50ab8d2b",
        "status": "missing_config",
        "confidence": "MEDIUM",
    },
    {
        "name": "Caveat Brush",
        "slug": "caveat-brush",
        "metadata_dir": "ofl/caveatbrush",
        "action": "add_commit",
        "commit": "59745e818ef7973e11e70cb1358d0e902b56c5fc",
        "status": "missing_config",
        "confidence": "MEDIUM",
    },
    # Category 2: Fix commit hash
    {
        "name": "DynaPuff",
        "slug": "dynapuff",
        "metadata_dir": "ofl/dynapuff",
        "action": "fix_commit",
        "old_commit": "0cc624ef50b654ffe1a30785396aaba308406132",
        "commit": "d1b4a98067a23e7ffbcf5b3665a887241983857b",
        "status": "needs_correction",
        "confidence": "HIGH",
    },
    # Category 3: Fix repository URL
    {
        "name": "Elsie",
        "slug": "elsie",
        "metadata_dir": "ofl/elsie",
        "action": "fix_url",
        "old_url_pattern": r'repository_url: "https://github.com/googlefonts/elsiefont[^"]*"',
        "repo_url": "https://github.com/librefonts/elsie",
        "commit": "9734e9ff1331292fc07ec198d4e5b35216fdd425",
        "status": "missing_config",
        "confidence": "MEDIUM",
    },
    # Category 4: Add new source blocks
    {
        "name": "Cantata One",
        "slug": "cantata-one",
        "metadata_dir": "ofl/cantataone",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/cantataone",
        "commit": "947c3dd6e969867a02166335a27c48c0a7f9123d",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Cantora One",
        "slug": "cantora-one",
        "metadata_dir": "ofl/cantoraone",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/cantoraone",
        "commit": "45d202afe1668a05e0afd870e124d72c2b82143c",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Cedarville Cursive",
        "slug": "cedarville-cursive",
        "metadata_dir": "ofl/cedarvillecursive",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/cedarvillecursive",
        "commit": "cd212b0e2dc2364a3012ef43a3b9155c7ed0d352",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Dorsa",
        "slug": "dorsa",
        "metadata_dir": "ofl/dorsa",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/dorsa",
        "commit": "90d5bffc5b005be8d3f7728ccb9aae3deaae1c23",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Dr Sugiyama",
        "slug": "dr-sugiyama",
        "metadata_dir": "ofl/drsugiyama",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/drsugiyama",
        "commit": "11d194b70af6df309a24c9395f64280172839879",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Duru Sans",
        "slug": "duru-sans",
        "metadata_dir": "ofl/durusans",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/durusans",
        "commit": "2895eb6c9842f80c1e01bbf9fbb6231eaef66724",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Dynalight",
        "slug": "dynalight",
        "metadata_dir": "ofl/dynalight",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/dynalight",
        "commit": "af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Eagle Lake",
        "slug": "eagle-lake",
        "metadata_dir": "ofl/eaglelake",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/eaglelake",
        "commit": "4e2b26479cf425b115731aa69e380fd2f5fd88e5",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "East Sea Dokdo",
        "slug": "east-sea-dokdo",
        "metadata_dir": "ofl/eastseadokdo",
        "action": "add_source_block",
        "repo_url": "https://github.com/yoondesign/Yoonfont-KoreaDokdo",
        "commit": "1bc4d9ec41e5159a839e58a349fa2e88799e93bc",
        "status": "missing_config",
        "confidence": "MEDIUM",
    },
    {
        "name": "Eater",
        "slug": "eater",
        "metadata_dir": "ofl/eater",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/eater",
        "commit": "91120e636b79d400473167dae30ff31a7c03b813",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Economica",
        "slug": "economica",
        "metadata_dir": "ofl/economica",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/economica",
        "commit": "6bf48e6858755227cdd104ee4b44e9e2e4bb197b",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Electrolize",
        "slug": "electrolize",
        "metadata_dir": "ofl/electrolize",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/electrolize",
        "commit": "2450033307b2d9f771649ae84007e59eb4387d1f",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Elsie Swash Caps",
        "slug": "elsie-swash-caps",
        "metadata_dir": "ofl/elsieswashcaps",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/elsieswashcaps",
        "commit": "f48faa350a1a9641bd984b6945f791914a652c65",
        "status": "missing_config",
        "confidence": "MEDIUM",
    },
    {
        "name": "Emblema One",
        "slug": "emblema-one",
        "metadata_dir": "ofl/emblemaone",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/emblemaone",
        "commit": "65d5dad63686fcfc0c7e13ba2cb3143803d96bfe",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Emilys Candy",
        "slug": "emilys-candy",
        "metadata_dir": "ofl/emilyscandy",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/emilyscandy",
        "commit": "6c0f2ad7e9b0bcc6d69bbd5896b980bf1e208074",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Engagement",
        "slug": "engagement",
        "metadata_dir": "ofl/engagement",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/engagement",
        "commit": "4a28e79422bbd98791c29adff6630d14f620ffd3",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Erica One",
        "slug": "erica-one",
        "metadata_dir": "ofl/ericaone",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/ericaone",
        "commit": "bde7cb1ee528f936a9bae89a746742983531d9f8",
        "status": "missing_config",
        "confidence": "HIGH",
    },
    {
        "name": "Esteban",
        "slug": "esteban",
        "metadata_dir": "ofl/esteban",
        "action": "add_source_block",
        "repo_url": "https://github.com/librefonts/esteban",
        "commit": "35e274d49210b9c8a7864689b48d6156e6be6bbf",
        "status": "missing_config",
        "confidence": "HIGH",
    },
]


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


def add_source_block(metadata_path, repo_url, commit):
    """Add a source{} block to METADATA.pb."""
    with open(metadata_path, "r") as f:
        content = f.read()

    # Check if source block already exists
    if "source {" in content:
        print(f"  WARNING: source block already exists in {metadata_path}")
        return False

    # Add source block before the last closing of the file
    source_block = f'\nsource {{\n  repository_url: "{repo_url}"\n  commit: "{commit}"\n}}\n'
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

    if f'commit: "{commit}"' in content:
        print(f"  commit already present")
        return False

    # Check if there's already a commit field
    if 'commit: "' in content:
        print(f"  WARNING: commit field already exists")
        return False

    # Insert commit after repository_url line
    lines = content.split("\n")
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and "repository_url:" in line:
            # Add commit on the next line with same indentation
            indent = "  "
            new_lines.append(f'{indent}commit: "{commit}"')
            inserted = True

    if not inserted:
        print(f"  WARNING: could not find repository_url line")
        return False

    with open(metadata_path, "w") as f:
        f.write("\n".join(new_lines))
    return True


def fix_commit_in_source(metadata_path, old_commit, new_commit):
    """Replace a commit hash in the source{} block."""
    with open(metadata_path, "r") as f:
        content = f.read()

    if old_commit not in content:
        print(f"  WARNING: old commit {old_commit[:8]} not found")
        return False

    content = content.replace(old_commit, new_commit)

    with open(metadata_path, "w") as f:
        f.write(content)
    return True


def fix_url_in_source(metadata_path, old_url_pattern, new_url, commit):
    """Fix the repository_url and optionally add commit."""
    with open(metadata_path, "r") as f:
        content = f.read()

    # Replace the URL using regex
    new_content = re.sub(old_url_pattern, f'repository_url: "{new_url}"', content)
    if new_content == content:
        print(f"  WARNING: URL pattern not matched")
        return False

    # Add commit if not present
    if 'commit: "' not in new_content and commit:
        lines = new_content.split("\n")
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if "repository_url:" in line:
                new_lines.append(f'  commit: "{commit}"')
        new_content = "\n".join(new_lines)

    with open(metadata_path, "w") as f:
        f.write(new_content)
    return True


def generate_commit_message(family):
    """Generate concise commit message following the policy."""
    name = family["name"]
    action = family["action"]

    if action in ("fix_commit", "fix_url"):
        verb = "fix source block in"
    elif action == "add_commit":
        verb = "add commit hash to"
    else:
        verb = "add source block to"

    repo_url = family.get("repo_url", "")
    if not repo_url:
        # For add_commit actions, read from METADATA.pb
        metadata_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "METADATA.pb")
        with open(metadata_path, "r") as f:
            content = f.read()
        match = re.search(r'repository_url: "([^"]+)"', content)
        if match:
            repo_url = match.group(1)

    repo_owner = extract_repo_owner_name(repo_url) or "unknown"
    short_hash = family["commit"][:8]

    config = "none"
    # Check if override config exists in google/fonts dir
    config_path = os.path.join(GOOGLE_FONTS_DIR, family["metadata_dir"], "config.yaml")
    if os.path.exists(config_path):
        config = "override config.yaml in google/fonts"

    lines = [
        f'{name}: {verb} METADATA.pb',
        '',
        f'- Repo: {repo_owner}',
        f'- Commit: {short_hash}',
        f'- Config: {config}',
        f'- Status: {family["status"]}',
        f'- Confidence: {family["confidence"]}',
    ]

    if action == "fix_commit":
        lines.append(f'Note: Previous commit was HEAD ({family["old_commit"][:8]}), not the onboarding commit.')
    elif action == "fix_url":
        lines.append(f'Note: Previous URL returned 404.')

    return "\n".join(lines)


def main():
    # Create new branch from upstream/main
    branch_name = "sources_per_family_2026-02-27"
    print(f"Creating branch {branch_name} from upstream/main...")
    run_git("checkout", "upstream/main", capture=False)
    run_git("checkout", "-b", branch_name, capture=False)

    processed = 0
    skipped = 0

    for family in FAMILIES:
        name = family["name"]
        slug = family["slug"]
        metadata_dir = family["metadata_dir"]
        action = family["action"]
        print(f"\n[{processed + skipped + 1}/{len(FAMILIES)}] {name} ({action})")

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
        if action == "add_source_block":
            success = add_source_block(metadata_path, family["repo_url"], family["commit"])
        elif action == "add_commit":
            success = add_commit_to_source(metadata_path, family["commit"])
        elif action == "fix_commit":
            success = fix_commit_in_source(metadata_path, family["old_commit"], family["commit"])
        elif action == "fix_url":
            success = fix_url_in_source(metadata_path, family["old_url_pattern"], family["repo_url"], family["commit"])

        if not success:
            print(f"  Skipping due to error above")
            # Reset any changes
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
        commit_msg = generate_commit_message(family)
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
    print(f"Total commits: {run_git('rev-list', '--count', 'upstream/main..HEAD')}")


if __name__ == "__main__":
    main()
