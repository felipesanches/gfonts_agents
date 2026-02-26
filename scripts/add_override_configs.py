#!/usr/bin/env python3
"""
Amend 34 commits in PR #10271 to add override config.yaml files
for families that have compatible sources but no config.
"""

import os
import re
import subprocess
import sys
import tempfile

GOOGLE_FONTS_DIR = "/mnt/shared/google/fonts"
INVESTIGATIONS_DIR = "/home/fsanches/projetos/gfonts_agents/data/investigations/families"

# Map family name -> override config.yaml content
CONFIGS = {
    "Adamina": """\
sources:
  - sources/Adamina.glyphs
buildVariable: false
""",
    "Alegreya SC": """\
sources:
  - sources/Alegreya.glyphs
  - "sources/Alegreya italic.glyphs"
familyName: Alegreya SC
buildVariable: false
""",
    "Alegreya Sans SC": """\
sources:
  - sources/Alegreya_Sans.glyphs
  - sources/Alegreya_Sans-Italic.glyphs
familyName: Alegreya Sans SC
buildVariable: false
""",
    "Amiko": """\
sources:
  - "source/Amiko v1.000.glyphs"
buildVariable: false
""",
    "Archivo Black": """\
sources:
  - SRC/Archivo-Black.glyphs
buildVariable: false
""",
    "Atma": """\
sources:
  - Sources/Mastering/TT/Atma-Light.ufo
  - Sources/Mastering/TT/Atma-Regular.ufo
  - Sources/Mastering/TT/Atma-Medium.ufo
  - Sources/Mastering/TT/Atma-SemiBold.ufo
  - Sources/Mastering/TT/Atma-Bold.ufo
buildVariable: false
""",
    "Bahiana": """\
sources:
  - sources/Bahiana.glyphs
buildVariable: false
""",
    "Bahianita": """\
sources:
  - Bahianita/sources/Bahianita.glyphs
buildVariable: false
""",
    "Ballet": """\
sources:
  - sources/Ballet.glyphs
axisOrder:
  - opsz
buildStatic: false
""",
    "Barlow": """\
sources:
  - sources/Barlow.glyphs
familyName: Barlow
buildVariable: false
""",
    "Barlow Condensed": """\
sources:
  - sources/Barlow.glyphs
familyName: Barlow Condensed
buildVariable: false
""",
    "Barlow Semi Condensed": """\
sources:
  - sources/Barlow.glyphs
familyName: Barlow Semi Condensed
buildVariable: false
""",
    "Barriecito": """\
sources:
  - Barriecito/sources/Barriecito.glyphs
buildVariable: false
""",
    "Barrio": """\
sources:
  - sources/Barrio.glyphs
buildVariable: false
""",
    "Basic": """\
sources:
  - Basic-Regular.ufo
buildVariable: false
""",
    "Bellota": """\
sources:
  - src/Bellota.glyphs
familyName: Bellota
buildVariable: false
""",
    "Bellota Text": """\
sources:
  - src/Bellota.glyphs
familyName: Bellota Text
buildVariable: false
""",
    "BenchNine": """\
sources:
  - src/BenchNine-Light.ufo
  - src/BenchNine-Regular.ufo
  - src/BenchNine-Bold.ufo
buildVariable: false
""",
    "Bigshot One": """\
sources:
  - src/BigshotOne.ufo
buildVariable: false
""",
    "Biryani": """\
sources:
  - "Source Files/Biryani 20150307.glyphs"
buildVariable: false
""",
    "Bowlby One SC": """\
sources:
  - src/BowlbyOneSC-Regular.ufo
buildVariable: false
""",
    "Cabin": """\
sources:
  - sources/CabinRegular.designspace
  - sources/CabinItalic.designspace
""",
    "Cabin Condensed": """\
sources:
  - sources/Cabin.glyphs
familyName: Cabin Condensed
buildVariable: false
""",
    "Cabin Sketch": """\
sources:
  - sources/CabinSketch.glyphs
buildVariable: false
""",
    "Caladea": """\
sources:
  - sources/glyphs/Caladea_Roman.glyphs
  - sources/glyphs/Caladea_Italics.glyphs
buildVariable: false
""",
    "Cambay": """\
sources:
  - "Sources/Cambay Regular/Cambay Devanagari-Regular.ufo"
  - "Sources/Cambay Oblique/Cambay Devanagari-Oblique.ufo"
  - "Sources/Cambay Bold/Cambay Devanagari-Bold.ufo"
  - "Sources/Cambay Bold Oblique/Cambay Devanagari-Bold Oblique.ufo"
buildVariable: false
""",
    "Caveat": """\
sources:
  - sources/Caveat.designspace
""",
    "Changa One": """\
sources:
  - ChangaOne-Regular.otf.ufo
  - ChangaOne_Italic.otf.ufo
buildVariable: false
""",
    "Coda": """\
sources:
  - coda/in-progress/Regular/src/Coda.ufo
  - coda/in-progress/Heavy/src/Coda-Heavy-IN.ufo
buildVariable: false
""",
    "Comfortaa": """\
sources:
  - sources/Comfortaa.glyphs
""",
    "Dai Banna SIL": """\
sources:
  - source/DaiBannaSILUpright.designspace
  - source/DaiBannaSILItalic.designspace
buildVariable: false
""",
    "Dhurjati": """\
sources:
  - Dhurjati.ufo
buildVariable: false
""",
    "Dhyana": """\
sources:
  - Regular/src/Dhyana.ufo
  - Bold/src/Dhyana-Bold.ufo
buildVariable: false
""",
    "Didact Gothic": """\
sources:
  - "sources/Didact Gothic.glyphs"
buildVariable: false
""",
}


def run_git(*args, capture=True, check=True):
    cmd = ["git", "-C", GOOGLE_FONTS_DIR] + list(args)
    if capture:
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
        return result.stdout.strip()
    else:
        subprocess.run(cmd, check=check)


def family_to_slug(family_name):
    return family_name.lower().replace(" ", "-")


def clean_paths(text):
    text = text.replace("/mnt/shared/upstream_repos/fontc_crater_cache/", "upstream_repos/fontc_crater_cache/")
    text = text.replace("/mnt/shared/google/fonts/", "google/fonts/")
    text = text.replace("/mnt/shared/google/fonts", "google/fonts")
    text = text.replace("/mnt/shared/", "")
    return text


def update_report_for_config(report_text, family_name, config_content):
    """Update investigation report to reflect the new override config.yaml."""
    # Add a section about the override config at the end (before Open Questions if it exists)
    override_note = f"""
## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
{config_content.strip()}
```

This override config enables gftools-builder to compile the font from upstream sources.
"""
    # Insert before "## Open Questions" if present, otherwise append
    if "## Open Questions" in report_text:
        report_text = report_text.replace("## Open Questions", override_note + "\n## Open Questions")
    else:
        report_text = report_text.rstrip() + "\n" + override_note

    # Update status references from missing_config to complete
    report_text = report_text.replace("**Status**: missing_config", "**Status**: complete")
    # Update table status fields
    report_text = re.sub(
        r'\|\s*\**Status\**\s*\|\s*missing_config\s*\|',
        '| **Status** | complete |',
        report_text
    )
    report_text = re.sub(
        r'\|\s*Status\s*\|\s*missing_config\s*\|',
        '| Status | complete |',
        report_text
    )
    # Update Config YAML field in tables
    report_text = re.sub(
        r'\|\s*\**Config YAML\**\s*\|\s*(?:--|None|none|N/A)[^|]*\|',
        '| **Config YAML** | Override in google/fonts |',
        report_text
    )
    report_text = re.sub(
        r'\|\s*Config YAML\s*\|\s*(?:--|None|none|N/A)[^|]*\|',
        '| Config YAML | Override in google/fonts |',
        report_text
    )
    # Update bullet-point format config_yaml
    report_text = re.sub(
        r'-\s*\**config_yaml\**:\s*None.*',
        '- **config_yaml**: Override in google/fonts',
        report_text
    )
    return report_text


def generate_updated_commit_message(old_msg, config_content):
    """Update the commit message to reflect new config status."""
    lines = old_msg.strip().split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("- Config:"):
            new_lines.append("- Config: override config.yaml in google/fonts")
        elif line.startswith("- Status: missing_config"):
            new_lines.append("- Status: complete")
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


def build_sed_command(commit_hashes):
    """Build a sed command to mark specific commits as 'edit'."""
    parts = []
    for h in commit_hashes:
        short = h[:12]
        parts.append(f"s/^pick {short}/edit {short}/")
    return "; ".join(parts)


def main():
    # Verify branch
    run_git("checkout", "sources_per_family_2026-02-26")
    branch = run_git("branch", "--show-current")
    print(f"On branch: {branch}")

    # Get all commits and map family -> (hash, dir)
    log = run_git("log", "--format=%H %s", "sources_per_family_2026-02-26", "--not", "upstream/main")
    commit_map = {}  # family_name -> (hash, family_dir)
    for line in log.strip().split("\n"):
        parts = line.split(" ", 1)
        full_hash = parts[0]
        subject = parts[1]
        match = re.match(r'^(.+?):\s*(?:add|fix) source block (?:to|in) METADATA\.pb', subject)
        if match:
            family_name = match.group(1).strip()
            # Get the family directory
            changed = run_git("diff", "--name-only", f"{full_hash}~1", full_hash)
            for f in changed.split("\n"):
                if "METADATA.pb" in f:
                    family_dir = os.path.dirname(f)
                    commit_map[family_name] = (full_hash, family_dir)
                    break

    print(f"Found {len(commit_map)} commits in PR")

    # Identify which families need config
    families_to_edit = []
    for family_name in CONFIGS:
        if family_name in commit_map:
            families_to_edit.append(family_name)
        else:
            print(f"  WARNING: {family_name} not found in PR commits!")

    print(f"Will edit {len(families_to_edit)} commits to add config.yaml")

    # Write a Python sequence editor script that marks specific commits as 'edit'
    editor_script_path = "/tmp/rebase_editor.py"
    # Build set of exact commit subjects to match
    subjects_to_edit = set()
    for family in families_to_edit:
        # Find the exact subject from the commit
        full_hash = commit_map[family][0]
        subject = run_git("log", "-1", "--format=%s", full_hash)
        subjects_to_edit.add(subject)
        print(f"  Will edit: {subject}")

    with open(editor_script_path, "w") as f:
        f.write("#!/usr/bin/env python3\n")
        f.write("import sys\n")
        f.write(f"subjects = {repr(subjects_to_edit)}\n")
        f.write("""
with open(sys.argv[1], 'r') as fh:
    lines = fh.readlines()
new_lines = []
for line in lines:
    matched = False
    for subj in subjects:
        if subj in line and line.startswith('pick '):
            new_lines.append('edit ' + line[5:])
            matched = True
            break
    if not matched:
        new_lines.append(line)
with open(sys.argv[1], 'w') as fh:
    fh.writelines(new_lines)
""")
    os.chmod(editor_script_path, 0o755)

    print(f"\nStarting interactive rebase...")
    env = os.environ.copy()
    env["GIT_SEQUENCE_EDITOR"] = editor_script_path
    result = subprocess.run(
        ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "-i", "upstream/main"],
        env=env,
        capture_output=True,
        text=True,
    )

    # Process each stopped commit
    processed = 0
    total = len(families_to_edit)

    while processed < total:
        # Check if we're in a rebase
        rebase_dir = os.path.join(GOOGLE_FONTS_DIR, ".git", "rebase-merge")
        if not os.path.exists(rebase_dir):
            rebase_dir = os.path.join(GOOGLE_FONTS_DIR, ".git", "rebase-apply")
            if not os.path.exists(rebase_dir):
                print("Rebase finished.")
                break

        # Get current commit info
        msg = run_git("log", "-1", "--format=%B")
        first_line = msg.split("\n")[0]
        match = re.match(r'^(.+?):\s*(?:add|fix) source block', first_line)
        if not match:
            print(f"  Not a config-target commit: {first_line[:60]}, continuing...")
            result = subprocess.run(
                ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "--continue"],
                capture_output=True, text=True,
                env={**os.environ, "GIT_EDITOR": "true"},
            )
            continue

        family_name = match.group(1).strip()

        if family_name not in CONFIGS:
            print(f"  {family_name}: not in config list, continuing...")
            result = subprocess.run(
                ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "--continue"],
                capture_output=True, text=True,
                env={**os.environ, "GIT_EDITOR": "true"},
            )
            continue

        processed += 1
        print(f"\n[{processed}/{total}] {family_name}")

        # Get family directory
        changed_files = run_git("diff", "--name-only", "HEAD~1")
        family_dir = None
        for f in changed_files.split("\n"):
            if "METADATA.pb" in f:
                family_dir = os.path.dirname(f)
                break

        if not family_dir:
            print(f"  WARNING: No family dir found, skipping")
            result = subprocess.run(
                ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "--continue"],
                capture_output=True, text=True,
                env={**os.environ, "GIT_EDITOR": "true"},
            )
            continue

        config_content = CONFIGS[family_name]
        slug = family_to_slug(family_name)

        # 1. Write override config.yaml
        config_path = os.path.join(GOOGLE_FONTS_DIR, family_dir, "config.yaml")
        with open(config_path, "w") as f:
            f.write(config_content)
        print(f"  Wrote: {family_dir}/config.yaml")

        # 2. Update upstream_info.md
        report_path = os.path.join(INVESTIGATIONS_DIR, f"{slug}.md")
        if os.path.exists(report_path):
            with open(report_path) as f:
                report_text = f.read()
            updated_report = update_report_for_config(report_text, family_name, config_content)
            updated_report = clean_paths(updated_report)

            info_path = os.path.join(GOOGLE_FONTS_DIR, family_dir, "upstream_info.md")
            with open(info_path, "w") as f:
                f.write(updated_report)
            print(f"  Updated: {family_dir}/upstream_info.md")

        # 3. Update commit message
        new_msg = generate_updated_commit_message(msg, config_content)
        msg_file = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
        msg_file.write(new_msg)
        msg_file.close()

        # 4. Stage and amend
        run_git("add", os.path.join(family_dir, "config.yaml"))
        run_git("add", os.path.join(family_dir, "upstream_info.md"))
        run_git("commit", "--amend", "-F", msg_file.name, capture=False)
        os.unlink(msg_file.name)

        # 5. Continue rebase
        result = subprocess.run(
            ["git", "-C", GOOGLE_FONTS_DIR, "rebase", "--continue"],
            capture_output=True, text=True,
            env={**os.environ, "GIT_EDITOR": "true"},
        )
        if result.returncode != 0:
            if "Successfully rebased" in (result.stdout + result.stderr):
                print(f"\nRebase completed after {processed} edits!")
                break
            if "No rebase in progress" in result.stderr:
                print(f"\nRebase completed (no rebase in progress)")
                break

    # Final check
    final_count = run_git("rev-list", "--count", "upstream/main..HEAD")
    print(f"\nDone! Final commit count: {final_count}")

    # Verify some config.yaml files
    print("\nVerification:")
    for family in ["Adamina", "Ballet", "Caveat"]:
        if family in commit_map:
            fdir = commit_map[family][1]
            exists = os.path.exists(os.path.join(GOOGLE_FONTS_DIR, fdir, "config.yaml"))
            print(f"  {fdir}/config.yaml: {'EXISTS' if exists else 'MISSING'}")


if __name__ == "__main__":
    main()
