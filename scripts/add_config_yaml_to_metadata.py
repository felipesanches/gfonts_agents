#!/usr/bin/env python3
"""
Add config_yaml field to METADATA.pb source blocks.

Takes a JSON file with families and their config_yaml paths,
and modifies the corresponding METADATA.pb files in google/fonts.

Usage:
    python3 scripts/add_config_yaml_to_metadata.py [--batch N] [--batch-size M] [--dry-run]
"""

import argparse
import json
import os
import re
import sys

GFONTS_DIR = "/mnt/shared/google/fonts"
READY_FILE = "data/config_yaml_ready_for_pr.json"


def extract_source_block(content):
    """Extract the full source block text from METADATA.pb content."""
    lines = content.split("\n")
    in_source = False
    depth = 0
    source_lines = []
    for line in lines:
        if "source {" in line and not in_source:
            in_source = True
            depth = 1
            source_lines.append(line)
            continue
        if in_source:
            source_lines.append(line)
            depth += line.count("{") - line.count("}")
            if depth <= 0:
                break
    return "\n".join(source_lines)


def add_config_yaml_to_source_block(content, config_yaml_value):
    """Add config_yaml field to the source block in METADATA.pb content.

    Inserts after commit: or branch: line, before files {} blocks.
    Returns modified content, or None if already has config_yaml or can't find insertion point.
    """
    # First check if config_yaml already exists in the full source block
    source_block = extract_source_block(content)
    if re.search(r'config_yaml:\s*"[^"]*"', source_block):
        return None

    lines = content.split("\n")
    result = []
    in_source = False
    depth = 0
    inserted = False
    insert_after_idx = None

    for i, line in enumerate(lines):
        if "source {" in line and not in_source:
            in_source = True
            depth = 1
            result.append(line)
            continue

        if in_source and not inserted:
            depth += line.count("{") - line.count("}")

            # Track last suitable insertion point (after commit: or branch:)
            if re.match(r'\s*commit:', line) or re.match(r'\s*branch:', line):
                result.append(line)
                insert_after_idx = len(result)
                continue

            # If we hit files { or closing }, insert before it
            if (re.match(r'\s*files\s*\{', line) or (depth <= 0 and "}" in line)) and insert_after_idx is not None:
                result.insert(insert_after_idx, f'  config_yaml: "{config_yaml_value}"')
                inserted = True

            if depth <= 0:
                in_source = False

        result.append(line)

    if not inserted and insert_after_idx is not None:
        # Source block ended without files blocks; insert at tracked position
        result.insert(insert_after_idx, f'  config_yaml: "{config_yaml_value}"')
        inserted = True

    if not inserted:
        return None

    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=1, help="Batch number (1-indexed)")
    parser.add_argument("--batch-size", type=int, default=50, help="Families per batch")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--input", default=READY_FILE, help="Input JSON file with families")
    args = parser.parse_args()

    with open(args.input) as f:
        all_families = json.load(f)

    start = (args.batch - 1) * args.batch_size
    end = start + args.batch_size
    batch = all_families[start:end]

    if not batch:
        print(f"No families in batch {args.batch} (total: {len(all_families)})")
        return

    print(f"Batch {args.batch}: families {start + 1}-{min(end, len(all_families))} of {len(all_families)}")
    print(f"Processing {len(batch)} families...")

    modified = 0
    skipped = 0
    errors = 0

    for fam in batch:
        metadata_path = os.path.join(GFONTS_DIR, fam["path"])
        config_yaml = fam["config_yaml"]

        if not os.path.isfile(metadata_path):
            print(f"  ERROR: {fam['path']} not found")
            errors += 1
            continue

        with open(metadata_path) as f:
            content = f.read()

        new_content = add_config_yaml_to_source_block(content, config_yaml)

        if new_content is None:
            print(f"  SKIP: {fam['family_name']} (already has config_yaml or no insertion point)")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  WOULD MODIFY: {fam['family_name']} -> config_yaml: \"{config_yaml}\"")
        else:
            with open(metadata_path, "w") as f:
                f.write(new_content)
            print(f"  MODIFIED: {fam['family_name']} -> config_yaml: \"{config_yaml}\"")

        modified += 1

    print(f"\nSummary: {modified} modified, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
