#!/usr/bin/env python3
"""Amend PR #10282 commits to add override config.yaml files."""
import os, re, subprocess, sys, tempfile

GF = "/mnt/shared/google/fonts"
BRANCH = "sources_per_family_2026-02-27"

def run(cmd, check=True, capture=False):
    if capture:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check, cwd=GF)
        return r.stdout.strip()
    subprocess.run(cmd, shell=True, check=check, cwd=GF)

FAMILIES = {
    "IBM Plex Sans Hebrew": {
        "dir": "ofl/ibmplexsanshebrew",
        "config": "sources:\n  - IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew.designspace\n",
        "remove_config_yaml": False,
    },
    "IBM Plex Sans Devanagari": {
        "dir": "ofl/ibmplexsansdevanagari",
        "config": "sources:\n  - IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari.designspace\n",
        "remove_config_yaml": False,
    },
    "IBM Plex Sans Condensed": {
        "dir": "ofl/ibmplexsanscondensed",
        "config": "sources:\n  - IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Roman.designspace\n  - IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Italic.designspace\n",
        "remove_config_yaml": False,
    },
    "Hina Mincho": {
        "dir": "ofl/hinamincho",
        "config": "sources:\n  - sources/Hina-Mincho.glyphs\n",
        "remove_config_yaml": False,
    },
    "Goudy Bookletter 1911": {
        "dir": "ofl/goudybookletter1911",
        "config": "sources:\n  - source/GoudyBookletter1911.ufo\n",
        "remove_config_yaml": False,
    },
    "Gayathri": {
        "dir": "ofl/gayathri",
        "config": "sources:\n  - sources/Gayathri.designspace\n",
        "remove_config_yaml": False,
    },
    "Galada": {
        "dir": "ofl/galada",
        "config": "sources:\n  - master/Galada.ufo\n",
        "remove_config_yaml": False,
    },
    "Farsan": {
        "dir": "ofl/farsan",
        "config": "sources:\n  - Sources/Farsan.glyphs\n",
        "remove_config_yaml": False,
    },
    "Fragment Mono SC": {
        "dir": "ofl/fragmentmonosc",
        "config": "sources:\n  - Fragment-Mono.glyphs\nfamilyName: Fragment Mono\nbuildVariable: false\ncheckCompatibility: false\nbuildSmallCap: true\nautohintTTF: true\nautohintOTF: true\n",
        "remove_config_yaml": True,  # Remove config_yaml field from METADATA.pb since override takes precedence
    },
}

# Find target commits
commits_log = run(f"git log --format='%h %s' felipesanches/{BRANCH} --not upstream/main", capture=True)
target_commits = {}
for line in commits_log.split('\n'):
    parts = line.split(' ', 1)
    if len(parts) < 2:
        continue
    sha, subject = parts
    for name in FAMILIES:
        if name in subject:
            target_commits[sha] = name
            print(f"  {sha} -> {name}")

if not target_commits:
    print("No commits found!")
    sys.exit(1)

print(f"\nFound {len(target_commits)} commits to amend")

# Checkout and set up branch
run(f"git checkout {BRANCH}")

# Create GIT_SEQUENCE_EDITOR
editor = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
editor.write(f"""#!/usr/bin/env python3
import sys
target_shas = {set(target_commits.keys())!r}
with open(sys.argv[1]) as f:
    lines = f.readlines()
new_lines = []
marked = 0
for line in lines:
    parts = line.split()
    if len(parts) >= 2 and parts[0] == 'pick':
        sha = parts[1]
        if any(sha.startswith(t) or t.startswith(sha) for t in target_shas):
            line = 'edit ' + ' '.join(parts[1:]) + '\\n'
            marked += 1
    new_lines.append(line)
with open(sys.argv[1], 'w') as f:
    f.writelines(new_lines)
import sys as _sys
print(f'Marked {{marked}} commits as edit', file=_sys.stderr)
""")
editor.close()
os.chmod(editor.name, 0o755)

env = os.environ.copy()
env["GIT_SEQUENCE_EDITOR"] = f"python3 {editor.name}"

print(f"\nStarting rebase on branch {BRANCH}...")
result = subprocess.run(
    ["git", "rebase", "-i", "upstream/main"],
    cwd=GF, env=env, capture_output=True, text=True
)
print(f"stderr: {result.stderr[:300]}")

def apply_and_amend():
    subject = run("git log -1 --format=%s", capture=True)
    matched = None
    for name, data in FAMILIES.items():
        if name in subject:
            matched = (name, data)
            break
    if not matched:
        print(f"  No match for: {subject}")
        return
    name, data = matched
    print(f"  Processing: {name}")

    # Write config.yaml
    config_path = os.path.join(GF, data["dir"], "config.yaml")
    with open(config_path, "w") as f:
        f.write(data["config"])
    run(f"git add {data['dir']}/config.yaml")
    print(f"    Wrote config.yaml")

    # Optionally remove config_yaml from METADATA.pb
    if data.get("remove_config_yaml"):
        metadata_path = os.path.join(GF, data["dir"], "METADATA.pb")
        with open(metadata_path) as f:
            content = f.read()
        # Remove the config_yaml line
        new_content = re.sub(r'\s*config_yaml: "[^"]+"\n', '\n', content)
        if new_content != content:
            with open(metadata_path, "w") as f:
                f.write(new_content)
            run(f"git add {data['dir']}/METADATA.pb")
            print(f"    Removed config_yaml from METADATA.pb")

    run("git commit --amend --no-edit")
    print(f"    Amended ✓")

for i in range(60):
    status = run("git status", capture=True)
    if "rebase" not in status.lower():
        print("\nRebase complete!")
        break
    apply_and_amend()
    result = subprocess.run(
        ["git", "rebase", "--continue"],
        cwd=GF, env=env, capture_output=True, text=True
    )
    if "Successfully rebased" in result.stdout + result.stderr:
        print("\nRebase complete!")
        break

os.unlink(editor.name)

print(f"\nTotal commits: {run('git rev-list --count upstream/main..HEAD', capture=True)}")
print("\nVerification:")
for name, data in FAMILIES.items():
    p = os.path.join(GF, data["dir"], "config.yaml")
    status = "✓" if os.path.exists(p) else "✗ MISSING"
    print(f"  {status} {name}")
