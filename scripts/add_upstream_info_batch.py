#!/usr/bin/env python3
"""
Add upstream_info.md files to google/fonts for families that have investigation
reports but no upstream_info.md yet. Documentation-only change.

Usage:
  python3 scripts/add_upstream_info_batch.py --start a --end a --branch upstream-info-4-a
  python3 scripts/add_upstream_info_batch.py --start a --end a --branch upstream-info-4-a --dry-run
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile

GOOGLE_FONTS_DIR = "/mnt/shared/google/fonts"
INVESTIGATIONS_DIR = "/home/fsanches/projetos/gfonts_agents/data/investigations/families"
BATCH_SIZE = 50  # families per commit


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


def setup_branch(branch_name):
    """Ensure we're on the correct branch, creating from upstream/main."""
    print("Fetching upstream...")
    run_git("fetch", "upstream", capture=False)

    existing = run_git("branch", "--list", branch_name)
    if existing:
        run_git("checkout", branch_name, capture=False)
        print(f"Switched to existing branch: {branch_name}")
    else:
        run_git("checkout", "-b", branch_name, "upstream/main", capture=False)
        print(f"Created new branch: {branch_name}")

    current = run_git("branch", "--show-current")
    if current != branch_name:
        print(f"ERROR: Expected branch {branch_name}, got {current}")
        sys.exit(1)


def find_family_dir(slug):
    """Find the family directory in google/fonts (ofl/ or apache/)."""
    for prefix in ("ofl", "apache"):
        path = os.path.join(GOOGLE_FONTS_DIR, prefix, slug)
        if os.path.isdir(path):
            return prefix + "/" + slug
    return None


def get_eligible_families(start_char, end_char):
    """Find families with reports but no upstream_info.md, in the given range."""
    families = []

    for filename in sorted(os.listdir(INVESTIGATIONS_DIR)):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]

        # Check if slug falls in the range
        first = slug[0].lower()
        if first < start_char.lower() or first > end_char.lower():
            continue

        # Check if family dir exists in google/fonts
        family_dir = find_family_dir(slug)
        if not family_dir:
            continue

        # Skip if upstream_info.md already exists
        upstream_info_path = os.path.join(GOOGLE_FONTS_DIR, family_dir, "upstream_info.md")
        if os.path.exists(upstream_info_path):
            continue

        families.append({
            "slug": slug,
            "family_dir": family_dir,
            "report_path": os.path.join(INVESTIGATIONS_DIR, filename),
        })

    return families


def create_batch_commit(families_batch, batch_num, total_batches, dry_run=False):
    """Create a single commit for a batch of families."""
    slugs = [f["slug"] for f in families_batch]
    first = slugs[0]
    last = slugs[-1]
    count = len(slugs)

    commit_msg = (
        f"Add upstream_info.md for {count} families ({first} to {last})\n\n"
        f"Documentation-only: adds investigation reports as upstream_info.md\n"
        f"for families that already have source metadata in METADATA.pb.\n"
        f"Batch {batch_num}/{total_batches}.\n\n"
        f"Families: {', '.join(slugs)}"
    )

    if dry_run:
        print(f"  [DRY RUN] Would commit {count} families: {first} .. {last}")
        return

    # Write upstream_info.md for each family
    staged_files = []
    for family in families_batch:
        with open(family["report_path"], "r") as f:
            report_text = f.read()

        cleaned_report = clean_paths(report_text)
        upstream_info_path = os.path.join(GOOGLE_FONTS_DIR, family["family_dir"], "upstream_info.md")

        with open(upstream_info_path, "w") as f:
            f.write(cleaned_report)

        rel_path = os.path.join(family["family_dir"], "upstream_info.md")
        run_git("add", rel_path)
        staged_files.append(rel_path)

    # Create commit
    msg_file = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    msg_file.write(commit_msg)
    msg_file.close()

    run_git("commit", "-F", msg_file.name, capture=False)
    os.unlink(msg_file.name)

    print(f"  Committed {count} families: {first} .. {last}")


def main():
    parser = argparse.ArgumentParser(description="Add upstream_info.md to google/fonts")
    parser.add_argument("--start", required=True, help="Start character (inclusive)")
    parser.add_argument("--end", required=True, help="End character (inclusive)")
    parser.add_argument("--branch", required=True, help="Branch name to create")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE, help="Families per commit")
    args = parser.parse_args()

    # Find eligible families
    families = get_eligible_families(args.start, args.end)
    print(f"Found {len(families)} eligible families in range [{args.start}-{args.end}]")

    if not families:
        print("Nothing to do.")
        return

    if args.dry_run:
        print("\n[DRY RUN MODE]")
        for i, f in enumerate(families):
            print(f"  {i+1}. {f['slug']} -> {f['family_dir']}/upstream_info.md")

    # Calculate batches
    batches = []
    for i in range(0, len(families), args.batch_size):
        batches.append(families[i:i + args.batch_size])

    total_batches = len(batches)
    print(f"\nWill create {total_batches} commits ({args.batch_size} families each)")

    if not args.dry_run:
        setup_branch(args.branch)

    for i, batch in enumerate(batches):
        print(f"\nBatch {i+1}/{total_batches} ({len(batch)} families):")
        create_batch_commit(batch, i + 1, total_batches, dry_run=args.dry_run)

    if not args.dry_run:
        # Verify no /mnt/shared paths remain
        print("\nVerifying no /mnt/shared paths in staged files...")
        result = subprocess.run(
            ["grep", "-r", "/mnt/shared", "--include=upstream_info.md",
             GOOGLE_FONTS_DIR + "/ofl", GOOGLE_FONTS_DIR + "/apache"],
            capture_output=True, text=True
        )
        if result.stdout.strip():
            print("WARNING: Found /mnt/shared paths in upstream_info.md files!")
            print(result.stdout[:500])
        else:
            print("OK: No /mnt/shared paths found.")

        total_commits = run_git("rev-list", "--count", "upstream/main..HEAD")
        print(f"\nTotal commits on branch: {total_commits}")
        print(f"\nNext: push and open PR:")
        print(f"  git -C {GOOGLE_FONTS_DIR} push felipesanches {args.branch}")
    else:
        print(f"\n[DRY RUN] Would create {total_batches} commits with {len(families)} families total")


if __name__ == "__main__":
    main()
