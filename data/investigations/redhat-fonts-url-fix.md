# Investigation: Red Hat Display / Text / Mono — Broken repository_url

**Date**: 2026-02-25
**Issue**: gfonts_agents-kn6
**Families**: Red Hat Display, Red Hat Text, Red Hat Mono

## Problem

The three Red Hat font families in google/fonts have `repository_url` pointing to
three separate `bghryct/*` repos that are all 404:

- `https://github.com/bghryct/RedHatDisplay` → 404
- `https://github.com/bghryct/RedHatMono` → 404
- `https://github.com/bghryct/RedHatText` → 404

## Investigation

### Current METADATA.pb state

Each family has a separate repo URL and commit hash:

| Family | Old URL | Old Commit |
|--------|---------|------------|
| Red Hat Display | bghryct/RedHatDisplay | fd36df3a3ad95084fe777597ed4b5c19961b3631 |
| Red Hat Mono | bghryct/RedHatMono | a0f2a7032143500e44dfd569d09ba30414d51a1c |
| Red Hat Text | bghryct/RedHatText | dfbc50b16e27d5be1986c3ec79534460a74c1370 |

### Replacement repo

All three were consolidated into **`https://github.com/RedHatOfficial/RedHatFont`** (HTTP 200, 570 stars).

The repo structure:
```
source/
  Proportional/
    RedHatDisplay/config.yaml  (sources: RedHatDisplay.glyphs, RedHatDisplay-Italic.glyphs)
    RedHatText/config.yaml     (sources: RedHatText.glyphs, RedHatText-Italic.glyphs)
  Mono/
    config.yaml                (sources: RedHatMono.glyphs, RedHatMono-Italic.glyphs)
```

### Commit history analysis

The RedHatOfficial/RedHatFont repo has a single merge commit:
- `32287097803f6c58136b60bc7a4a594a7fcbd689` (2025-03-06) — "Merge pull request #69 from bghryct/master"

**The old bghryct commits do NOT exist in this repo.** This is a completely
separate repo that received a merge from bghryct, not a rename/transfer.

### google/fonts onboarding history

PR #8502 (Red Hat Mono v1.030, merged 2024-11-20) explicitly states:
> "Taken from the upstream repo https://github.com/bghryct/RedHatMono at commit a0f2a703..."

So the fonts were onboarded from the bghryct repos while they still existed.

## Decision

**Update `repository_url` to `https://github.com/RedHatOfficial/RedHatFont` for all three families.**

The old commit hashes must be removed since they don't exist in the new repo.
The single commit in RedHatOfficial/RedHatFont (`3228709`) should be used instead,
since it represents the merged state of the old repos. This is not the original
onboarding commit, but the old repos no longer exist.

### config_yaml paths in the new repo

| Family | config_yaml path |
|--------|-----------------|
| Red Hat Display | source/Proportional/RedHatDisplay/config.yaml |
| Red Hat Text | source/Proportional/RedHatText/config.yaml |
| Red Hat Mono | source/Mono/config.yaml |

## Risk

The fonts built from RedHatOfficial/RedHatFont@3228709 may not exactly match
the binaries currently in google/fonts (which were built from the old bghryct repos).
This should be verified by building from the new repo and comparing binaries.

## Action

1. Update METADATA.pb `repository_url` for all three families
2. Update `commit` to `32287097803f6c58136b60bc7a4a594a7fcbd689`
3. Add `config_yaml` paths
4. Update tracking in gfonts_library_sources.json
