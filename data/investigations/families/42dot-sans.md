# 42dot Sans

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: 42dot
**METADATA.pb path**: `ofl/42dotsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/42dot/42dot-Sans |
| Commit | `d23e87fe44d5b4f5afaa9dca9d5926d7c414d625` |
| Config YAML | `sources/config_variable.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/42dot/42dot-Sans`. This matches the copyright string in the font metadata ("Copyright 2024 The 42dot Sans Project Authors (https://github.com/42dot/42dot-Sans)"). The onboarding commit `d60948acd8c1` in google/fonts also references this same URL in its commit body: "Taken from the upstream repo https://github.com/42dot/42dot-Sans". PR #8772 in google/fonts confirms this URL.

## How the Commit Hash Was Identified

The commit hash `d23e87fe44d5b4f5afaa9dca9d5926d7c414d625` was already present in the METADATA.pb `source { commit }` field. This commit is directly cited in multiple places:

1. The google/fonts onboarding commit `d60948acd8c1` (2024-12-23) body states: "Taken from the upstream repo https://github.com/42dot/42dot-Sans at commit https://github.com/42dot/42dot-Sans/commit/d23e87fe44d5b4f5afaa9dca9d5926d7c414d625"
2. PR #8772 in google/fonts has the same reference in its body
3. The commit date in the upstream repo (2024-12-23 05:50:28 -0800) is essentially simultaneous with the google/fonts onboarding commit (2024-12-23 05:51:32 -0800), indicating the font was added immediately upon the upstream commit being made

## How Config YAML Was Resolved

The config file `sources/config_variable.yaml` was found in the upstream repository at the recorded commit hash. It contains a gftools-builder configuration referencing the `42dotSans.designspace` source file, with settings for variable font build only (no static, no OTF, no webfont). No override config.yaml exists in the google/fonts family directory (`ofl/42dotsans/`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-12-23 05:50:28 -0800
- Commit message: "Adding some metadata"
- Source files at commit: `sources/42dotSans.designspace`, `sources/42dotSans.glyphspackage/` (with many glyph files), `sources/config_variable.yaml`

## Confidence

**High**: All data is fully consistent. The repository URL, commit hash, and config_yaml were all pre-existing in METADATA.pb. The commit hash is directly corroborated by the google/fonts onboarding commit message and PR #8772. The commit exists in the upstream repo and contains the expected source files and build configuration. The near-simultaneous timestamps (within 1 minute) between upstream commit and onboarding strongly confirm the correct commit.

## Open Questions

None
