#!/usr/bin/env python3
"""
Directly amend commits in the batch4 PR branch using rebase with correct short hash matching.
"""
import os, re, subprocess, sys, tempfile

GF = "/mnt/shared/google/fonts"

def run(cmd, check=True, capture=False):
    if capture:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check, cwd=GF)
        return r.stdout.strip()
    subprocess.run(cmd, shell=True, check=check, cwd=GF)

# Family name → (metadata_dir, config_content, commit_to_add_if_missing)
FAMILIES = {
    "Fraunces": (
        "ofl/fraunces",
        "sources:\n  - sources/Roman/Fraunces.designspace\n  - sources/Italic/FrauncesItalic.designspace\n",
        None
    ),
    "IBM Plex Sans KR": (
        "ofl/ibmplexsanskr",
        "sources:\n  - IBM-Plex-Sans-KR/sources/masters/IBM Plex Sans KR.glyphs\n",
        None
    ),
    "IBM Plex Sans Thai Looped": (
        "ofl/ibmplexsansthailooped",
        "sources:\n  - IBM-Plex-Sans-Thai-Looped/sources/masters/IBM Plex Sans Thai Looped.designspace\n",
        None
    ),
    "IBM Plex Sans Thai": (
        "ofl/ibmplexsansthai",
        "sources:\n  - IBM-Plex-Sans-Thai/sources/masters/IBM Plex Sans Thai.designspace\n",
        None
    ),
    "IBM Plex Serif": (
        "ofl/ibmplexserif",
        "sources:\n  - IBM-Plex-Serif/sources/masters/IBM Plex Serif Roman.designspace\n  - IBM-Plex-Serif/sources/masters/IBM Plex Serif Italic.designspace\n",
        None
    ),
    "Katibeh": (
        "ofl/katibeh",
        "sources:\n  - Sources/Katibeh Master.glyphs\n",
        "3fde990dc2f1648d63b7fe2841902d268529c1c2"
    ),
    "Kavivanar": (
        "ofl/kavivanar",
        "sources:\n  - source/Kavivanar-Regular.ufo\n",
        "689a10bac6313880ae05b86aea2ad91979c9880d"
    ),
}

# Build mapping from family name patterns to commit SHA prefixes
commits_log = run("git log --format='%h %s' upstream/main..HEAD", capture=True)
target_commits = {}
for line in commits_log.split('\n'):
    parts = line.split(' ', 1)
    if len(parts) < 2:
        continue
    sha, subject = parts
    for family_name in FAMILIES:
        if family_name in subject:
            target_commits[sha] = family_name
            print(f"Found: {sha} -> {family_name}")

if not target_commits:
    print("No commits found!")
    sys.exit(1)

# Create the GIT_SEQUENCE_EDITOR that uses short SHAs
editor = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
editor.write(f"""#!/usr/bin/env python3
import sys
target_shas = {set(target_commits.keys())!r}
with open(sys.argv[1]) as f:
    lines = f.readlines()
new_lines = []
for line in lines:
    parts = line.split()
    if len(parts) >= 2 and parts[0] == 'pick':
        # Check if this SHA matches any of our targets (prefix match)
        sha = parts[1]
        matched = any(sha.startswith(t) or t.startswith(sha) for t in target_shas)
        if matched:
            line = 'edit ' + ' '.join(parts[1:]) + '\\n'
    new_lines.append(line)
with open(sys.argv[1], 'w') as f:
    f.writelines(new_lines)
print('Editor done, marked', sum(1 for l in new_lines if l.startswith('edit')), 'commits as edit', file=__import__('sys').stderr)
""")
editor.close()
os.chmod(editor.name, 0o755)

env = os.environ.copy()
env["GIT_SEQUENCE_EDITOR"] = f"python3 {editor.name}"

print("\nStarting rebase...")
result = subprocess.run(
    ["git", "rebase", "-i", "upstream/main"],
    cwd=GF, env=env, capture_output=True, text=True
)
print(f"stdout: {result.stdout[:300]}")
print(f"stderr: {result.stderr[:300]}")

def apply_changes_and_continue():
    """Apply changes at the current rebase stop and amend."""
    subject = run("git log -1 --format=%s", capture=True)
    print(f"\n  Stopped at: {subject}")

    matched = None
    for family_name, (metadata_dir, config_content, extra_commit) in FAMILIES.items():
        if family_name in subject:
            matched = (family_name, metadata_dir, config_content, extra_commit)
            break

    if not matched:
        print(f"  No match, continuing...")
        run("git rebase --continue", check=False)
        return True

    family_name, metadata_dir, config_content, extra_commit = matched

    # Add commit to METADATA.pb if needed
    if extra_commit:
        metadata_path = os.path.join(GF, metadata_dir, "METADATA.pb")
        with open(metadata_path) as f:
            content = f.read()
        if 'commit: "' not in content:
            lines = content.split("\n")
            new_lines = []
            inserted = False
            for line in lines:
                new_lines.append(line)
                if not inserted and "repository_url:" in line:
                    new_lines.append(f'  commit: "{extra_commit}"')
                    inserted = True
            with open(metadata_path, "w") as f:
                f.write("\n".join(new_lines))
            run(f"git add {metadata_dir}/METADATA.pb")
            print(f"  Added commit {extra_commit[:8]} to METADATA.pb")

    # Write config.yaml
    config_path = os.path.join(GF, metadata_dir, "config.yaml")
    with open(config_path, "w") as f:
        f.write(config_content)
    run(f"git add {metadata_dir}/config.yaml")
    print(f"  Wrote config.yaml to {metadata_dir}/config.yaml")

    # Amend
    run("git commit --amend --no-edit")
    print(f"  Amended ✓")
    return True

# Loop through rebase stops
max_iterations = 50
for i in range(max_iterations):
    status = run("git status", capture=True)
    if "rebase" not in status.lower() or ("interactive rebase" not in status.lower() and "rebase in progress" not in status.lower()):
        print("\nRebase complete!")
        break

    apply_changes_and_continue()

    result = subprocess.run(
        ["git", "rebase", "--continue"],
        cwd=GF, env=env, capture_output=True, text=True
    )
    # Check if done
    if "Successfully rebased" in result.stdout or "Successfully rebased" in result.stderr:
        print("\nRebase complete!")
        break
    if result.returncode != 0 and "stopped at" not in result.stderr:
        status = run("git status", capture=True)
        if "rebase" not in status.lower():
            print("\nRebase complete!")
            break

os.unlink(editor.name)

# Verify
print(f"\nTotal commits: {run('git rev-list --count upstream/main..HEAD', capture=True)}")

# Show changed commits
print("\nVerifying config.yaml files:")
for family_name, (metadata_dir, _, _) in FAMILIES.items():
    config_path = os.path.join(GF, metadata_dir, "config.yaml")
    if os.path.exists(config_path):
        print(f"  ✓ {family_name}: {config_path}")
    else:
        print(f"  ✗ {family_name}: MISSING")
