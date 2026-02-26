# Bakbak One

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Saumya Kishore, Sanchit Sawaria
**METADATA.pb path**: `ofl/bakbakone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/bakbak |
| Commit | `b53b9c31c16f0021b7c206a57a8f04a4d382bc67` |
| Config YAML | `sources/builder.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL is documented in:
1. The METADATA.pb `source {}` block (present since the initial onboarding via gftools-packager)
2. The copyright string: "Copyright 2021 The Bakbak One Project Authors (https://github.com/googlefonts/bakbak)"
3. The original onboarding commit `338bebe14` (2021-09-24): "taken from the upstream repo https://github.com/googlefonts/bakbak.git"

## How the Commit Hash Was Identified

The font has two TTF commits in google/fonts:

1. **Original onboarding** (commit `338bebe14`, 2021-09-24, PR #3810): gftools-packager referenced upstream commit `8308b62b527659d7be4a2890c5f07e2d1db1496b`
2. **Update to v1.003** (commit `10e8b3d30`, 2022-01-11, PR #4176): PR body says "Added fractions, Renamed remaining instances of BakBak to Bakbak, Added devanagari to METADATA.pb"

The current METADATA.pb commit `b53b9c31c16f0021b7c206a57a8f04a4d382bc67` matches perfectly with the latest upstream commit visible in the shallow clone. This commit is dated 2021-12-16 with message "Added fractions" — which aligns exactly with the PR #4176 description of "Added fractions". The timeline is consistent:
- Upstream commit `b53b9c3` on 2021-12-16 "Added fractions"
- google/fonts PR #4176 merged on 2022-01-11 "Bakbak Version 1.003"

The commit and config_yaml were added to METADATA.pb by Felipe Sanches in commit `c20c67c3b` (2025-04-01) with the note "(PR #4176)".

## How Config YAML Was Resolved

The upstream repository contains `sources/builder.yaml` with the following configuration:

```yaml
sources:
  - Bakbak.glyphs
familyName: "Bakbak One"
buildTTF: true
buildOTF: false
buildWebfont: false
buildVariable: false
```

This file exists at the HEAD commit (`b53b9c3`) in the upstream repo. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is the HEAD of the shallow clone)
- Commit date: 2021-12-16 13:57:28 +0400
- Commit message: "Added fractions"
- Source files at commit: `sources/Bakbak.glyphs`, `sources/HindKit-build.zip`, `sources/builder.yaml`

## Confidence

**High**: The commit `b53b9c3` aligns perfectly with the PR #4176 update (both describe "Added fractions"). The original onboarding used commit `8308b62` but the current binaries correspond to the v1.003 update from `b53b9c3`. The config_yaml path `sources/builder.yaml` is verified to exist at the commit. All fields are documented in METADATA.pb.

## Open Questions

None. This family has complete source documentation in METADATA.pb with verified repository URL, commit hash, branch, config_yaml, and file mappings.
