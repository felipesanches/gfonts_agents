# Investigation: Orelega One — Broken repository_url

**Date**: 2026-02-25
**Issue**: gfonts_agents-kn6
**Family**: Orelega One

## Problem

METADATA.pb has `repository_url: "https://github.com/JapanYoshi/Orelega"` which is 404.
The entire `JapanYoshi` GitHub account no longer exists.

## Investigation

### Designer identity

The designer Haruki Wakamatsu (formerly "JapanYoshi") migrated from GitHub to GitLab
under the username `haleyhalcyon`.

### Replacement repo

**`https://gitlab.com/haleyhalcyon/orelega`** (HTTP 200)

- Contains the same commit referenced in google/fonts onboarding PR #3174:
  `756e15cc3dfeb958aafefc2e05db493e4473f0bd` (2021-03-12, author "JapanYoshi")
- Commit history shows commits by both "JapanYoshi" and "Haley Wakamatsu",
  confirming this is the same person
- Repo was re-pushed to GitLab on 2024-07-17
- Contains: `OrelegaOne-Regular.sfdir/`, `build.sh`, `OFL.txt`, `DESCRIPTION.en_us.html`

### Build configuration

**No `config.yaml` file exists in the repo.** The font uses a custom `build.sh` script.
An override config.yaml will need to be created in google/fonts, or the font will
need to be flagged as requiring special build handling.

### Onboarding history

PR #3174 (2021-03-12) onboarded Orelega One. The METADATA.pb currently has no commit
hash, only the (broken) repository_url and file mappings (OFL.txt, DESCRIPTION.en_us.html,
ttf/OrelegaOne-Regular.ttf).

## Decision

**Update `repository_url` to `https://gitlab.com/haleyhalcyon/orelega`**

Note: This is a **GitLab** URL, not GitHub. The `repository_url` field in METADATA.pb
supports any git hosting URL.

- No commit hash can be set yet without an override config.yaml or until we determine
  how to build from this repo (it uses build.sh, not gftools-builder)
- The font is a static .ttf only (not variable), built via custom build.sh

## Risk

- The font uses a custom build system (build.sh + fontmake), not gftools-builder
- fontc_crater may not be able to process this without special handling
- The commit that matches the deployed binary should be verified

## Action

1. Update METADATA.pb `repository_url` to the GitLab URL
2. Flag this font as needing a config.yaml override or special build handling
3. Update tracking in gfonts_library_sources.json
