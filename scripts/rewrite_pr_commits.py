#!/usr/bin/env python3
"""
Rewrite PR #10271 commits to:
1. Add upstream_info.md to each family directory
2. Replace verbose commit messages with concise summaries
3. Clean /mnt/shared paths from reports
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


def family_to_slug(family_name):
    """Convert family name to slug for report filename."""
    return family_name.lower().replace(" ", "-")


def clean_paths(text):
    """Remove /mnt/shared prefixes from paths."""
    text = text.replace("/mnt/shared/upstream_repos/fontc_crater_cache/", "upstream_repos/fontc_crater_cache/")
    text = text.replace("/mnt/shared/google/fonts/", "google/fonts/")
    text = text.replace("/mnt/shared/google/fonts", "google/fonts")
    text = text.replace("/mnt/shared/", "")
    return text


def extract_field(text, field_name):
    """Extract a field value from a markdown table or bullet list."""
    # Try table format: | Field | Value |
    patterns = [
        rf'\|\s*\**{re.escape(field_name)}\**\s*\|\s*(.*?)\s*\|',
        rf'\|\s*{re.escape(field_name)}\s*\|\s*(.*?)\s*\|',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            val = match.group(1).strip()
            val = val.strip('`').strip('*').strip()
            return val

    # Try bullet list format: - **Field**: Value or - **Field Name**: Value
    bullet_patterns = [
        rf'-\s*\**{re.escape(field_name)}\**:\s*(.*?)(?:\n|$)',
        rf'-\s*\**{re.escape(field_name)}\**\s*:\s*(.*?)(?:\n|$)',
    ]
    for pattern in bullet_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            val = match.group(1).strip()
            val = val.strip('`').strip('*').strip()
            return val

    return None


# Keep backward compatibility
extract_table_field = extract_field


def extract_repo_owner_name(url):
    """Extract owner/repo from a GitHub URL."""
    if not url:
        return None
    match = re.search(r'github\.com/([^/]+/[^/\s]+)', url)
    if match:
        return match.group(1).rstrip(')')
    return url


def extract_short_hash(commit_str):
    """Extract short hash from commit string like `adf2c7e7...`."""
    if not commit_str:
        return None
    # Remove backticks and parenthetical notes
    cleaned = commit_str.strip('`').strip()
    # Take first 8 chars of the hash
    hash_match = re.match(r'([0-9a-f]{7,40})', cleaned)
    if hash_match:
        return hash_match.group(1)[:8]
    return cleaned[:8] if cleaned else None


def extract_confidence(text):
    """Extract confidence level from report."""
    match = re.search(r'\*\*(?:Confidence[:\s]*)?(\w+)\*\*', text)
    if match:
        level = match.group(1).upper()
        if level in ("HIGH", "MEDIUM", "LOW"):
            return level
    # Check section header style
    match = re.search(r'## Confidence\s+\*\*(\w+)\*\*', text)
    if match:
        return match.group(1).upper()
    return "MEDIUM"


def extract_status(text):
    """Extract status from report."""
    status = extract_field(text, "Status")
    if status:
        # Clean up markdown bold and backticks
        status = status.strip('*').strip('`').strip()
        if "complete" in status.lower():
            return "complete"
        elif "missing_config" in status.lower():
            return "missing_config"
        elif "missing" in status.lower():
            return status.lower()
        elif "needs_correction" in status.lower():
            return "needs_correction"
        return status.lower()
    # Try from header metadata
    match = re.search(r'\*\*Status\*\*:\s*(\S+)', text)
    if match:
        return match.group(1).strip()
    # Infer from content
    if "config.yaml" in text.lower() and ("no config" in text.lower() or "none" in text.lower()):
        if extract_field(text, "Repository URL") or extract_field(text, "Correct Repository URL"):
            return "missing_config"
    if extract_field(text, "Config YAML") or extract_field(text, "config_yaml"):
        config = extract_field(text, "Config YAML") or extract_field(text, "config_yaml")
        if config and config.lower() not in ("none", "--", "—", "-", "n/a"):
            return "complete"
        return "missing_config"
    return "missing_config"


def extract_commit_description(text, short_hash):
    """Try to extract a brief description of what the commit represents."""
    if not short_hash:
        return ""

    # Common patterns in the reports
    patterns = [
        rf'{short_hash}[0-9a-f]*\s*\(([^)]+)\)',  # hash (description)
        rf'message:\s*"([^"]+)"',  # message: "..."
        rf"message:\s*['\"]([^'\"]+)['\"]",
        rf'Commit message:\s*"([^"]+)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            desc = match.group(1).strip()
            if len(desc) < 80:
                return desc

    # Look for "only commit" or "single commit" mentions
    if re.search(r'only\s+(a\s+)?single\s+commit|only\s+commit|single\s+commit', text, re.IGNORECASE):
        return "only commit in repo"

    # Check bullet format: - **Commit**: `hash` (description)
    match = re.search(rf'-\s*\**Commit\**:\s*`?{short_hash}[0-9a-f]*`?\s*\(([^)]+)\)', text, re.IGNORECASE)
    if match:
        desc = match.group(1).strip()
        if len(desc) < 80:
            return desc

    return ""


def extract_config_description(text):
    """Extract config yaml description."""
    config = extract_table_field(text, "Config YAML")
    if not config:
        config = extract_table_field(text, "Config Yaml")
    if not config:
        return "none"

    config = config.strip('`').strip()

    # Normalize various "none" representations
    if config.lower().startswith("n/a") or config in ("--", "—", "None", "none", "N/A", "n/a", "-"):
        # Check if SFD-only
        if "SFD" in text or ".sfd" in text.lower():
            return "none (SFD-only sources)"
        if ".vfb" in text.lower() and ".sfd" not in text.lower():
            return "none (VFB-only sources)"
        if "legacy" in text.lower():
            return "none (legacy format)"
        return "none"

    if "None" in config and "SFD" in config:
        return "none (SFD-only sources)"

    # Clean up the path
    config = config.replace("/mnt/shared/", "")
    # Remove trailing backticks or markdown artifacts
    config = config.strip('`').strip()
    return config


def has_url_correction(text):
    """Check if the report mentions a URL correction."""
    if extract_table_field(text, "Correct Repository URL"):
        return True
    if re.search(r'corrected?\s+from|fork.*canonical|wrong.*url|incorrect.*url', text, re.IGNORECASE):
        return True
    return False


def get_correction_note(text):
    """Extract a note about corrections if any."""
    correct_url = extract_table_field(text, "Correct Repository URL")
    current_url = extract_table_field(text, "Repository URL")
    if correct_url and current_url and correct_url != current_url:
        old_owner = extract_repo_owner_name(current_url)
        return f"Previous repo URL pointed to {old_owner} instead of canonical upstream."
    return None


def generate_concise_message(family_name, report_text):
    """Generate a concise commit message from the report."""
    # Determine if this is an "add" or "fix" (correction)
    is_fix = has_url_correction(report_text)
    action = "fix source block in" if is_fix else "add source block to"

    # Extract fields
    repo_url = extract_field(report_text, "Correct Repository URL") or \
               extract_field(report_text, "Repository URL")
    repo_owner = extract_repo_owner_name(repo_url) or "unknown"

    commit_str = extract_field(report_text, "Correct Commit Hash") or \
                 extract_field(report_text, "Commit (correct)") or \
                 extract_field(report_text, "Commit Hash") or \
                 extract_field(report_text, "Commit")
    short_hash = extract_short_hash(commit_str) or "unknown"

    commit_desc = extract_commit_description(report_text, short_hash)

    config = extract_config_description(report_text)
    status = extract_status(report_text)
    confidence = extract_confidence(report_text)

    # Build message
    lines = [f"{family_name}: {action} METADATA.pb", ""]

    commit_line = f"- Commit: {short_hash}"
    if commit_desc:
        commit_line += f" ({commit_desc})"

    lines.append(f"- Repo: {repo_owner}")
    lines.append(commit_line)
    lines.append(f"- Config: {config}")
    lines.append(f"- Status: {status}")
    lines.append(f"- Confidence: {confidence}")

    correction_note = get_correction_note(report_text)
    if correction_note:
        lines.append(f"Note: {correction_note}")

    return "\n".join(lines)


def process_commit():
    """Process a single stopped commit during rebase."""
    # Get the commit message
    msg = run_git("log", "-1", "--format=%B")

    # Extract family name from first line: "Family Name: enrich METADATA.pb source info"
    first_line = msg.split("\n")[0]
    match = re.match(r'^(.+?):\s*enrich METADATA\.pb source info', first_line)
    if not match:
        print(f"  WARNING: Could not parse family name from: {first_line}")
        print(f"  Skipping this commit, continuing rebase...")
        run_git("rebase", "--continue", capture=False)
        return False

    family_name = match.group(1).strip()
    slug = family_to_slug(family_name)
    print(f"  Family: {family_name} (slug: {slug})")

    # Get the changed files to find the family directory
    changed_files = run_git("diff", "--name-only", "HEAD~1").split("\n")
    metadata_file = None
    for f in changed_files:
        if f.endswith("METADATA.pb"):
            metadata_file = f
            break

    if not metadata_file:
        print(f"  WARNING: No METADATA.pb found in changed files: {changed_files}")
        run_git("rebase", "--continue", capture=False)
        return False

    family_dir = os.path.dirname(metadata_file)
    print(f"  Family dir: {family_dir}")

    # Read the investigation report
    report_path = os.path.join(INVESTIGATIONS_DIR, f"{slug}.md")
    if not os.path.exists(report_path):
        print(f"  WARNING: No investigation report at {report_path}")
        run_git("rebase", "--continue", capture=False)
        return False

    with open(report_path, "r") as f:
        report_text = f.read()

    # Clean paths
    cleaned_report = clean_paths(report_text)

    # Write upstream_info.md
    upstream_info_path = os.path.join(GOOGLE_FONTS_DIR, family_dir, "upstream_info.md")
    with open(upstream_info_path, "w") as f:
        f.write(cleaned_report)
    print(f"  Wrote: {upstream_info_path}")

    # Generate concise commit message
    concise_msg = generate_concise_message(family_name, report_text)
    print(f"  Message: {concise_msg.split(chr(10))[0]}")

    # Write temp file for commit message
    msg_file = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    msg_file.write(concise_msg)
    msg_file.close()

    # Stage and amend
    run_git("add", os.path.join(family_dir, "upstream_info.md"))
    run_git("commit", "--amend", "-F", msg_file.name, capture=False)

    os.unlink(msg_file.name)
    return True


def main():
    # Verify we're on the right branch
    branch = run_git("branch", "--show-current")
    print(f"Current branch: {branch}")

    if branch != "sources_per_family_2026-02-26":
        print(f"ERROR: Expected branch sources_per_family_2026-02-26, got {branch}")
        sys.exit(1)

    # Count commits to rewrite
    commit_count = run_git("rev-list", "--count", "upstream/main..HEAD")
    print(f"Commits to rewrite: {commit_count}")

    # Start interactive rebase with all commits marked as 'edit'
    print("\nStarting interactive rebase...")
    env = os.environ.copy()
    env["GIT_SEQUENCE_EDITOR"] = "sed -i 's/^pick/edit/'"
    result = subprocess.run(
        ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "-i", "upstream/main"],
        env=env,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        # This is expected - it stops at first commit
        if "Stopped at" not in result.stdout and "Stopped at" not in result.stderr:
            print(f"Rebase start output: {result.stdout}")
            print(f"Rebase start stderr: {result.stderr}")

    # Process each commit
    processed = 0
    max_commits = int(commit_count)

    while processed < max_commits:
        processed += 1
        print(f"\n[{processed}/{max_commits}]")

        # Check if we're in a rebase
        rebase_dir = os.path.join(GOOGLE_FONTS_DIR, ".git", "rebase-merge")
        if not os.path.exists(rebase_dir):
            # Maybe also check rebase-apply
            rebase_dir = os.path.join(GOOGLE_FONTS_DIR, ".git", "rebase-apply")
            if not os.path.exists(rebase_dir):
                print("  Rebase seems to have finished early.")
                break

        success = process_commit()
        if not success:
            print(f"  Skipped commit {processed}")

        # Continue to next commit
        result = subprocess.run(
            ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "--continue"],
            capture_output=True,
            text=True,
            env={**os.environ, "GIT_EDITOR": "true"},
        )
        if result.returncode != 0:
            if "Successfully rebased" in result.stdout or "Successfully rebased" in result.stderr:
                print(f"\nRebase completed after {processed} commits!")
                break
            elif "No rebase in progress" in result.stderr:
                print(f"\nRebase completed (no rebase in progress) after {processed} commits!")
                break
            # Check if stopped at next commit
            if "Stopped at" not in result.stdout and "Stopped at" not in result.stderr:
                # Could be an error or could be the end
                if "Could not apply" in result.stderr:
                    print(f"  ERROR during rebase --continue: {result.stderr}")
                    sys.exit(1)

    # Final check
    final_count = run_git("rev-list", "--count", "upstream/main..HEAD")
    print(f"\nDone! Final commit count: {final_count}")


if __name__ == "__main__":
    main()
