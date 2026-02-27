# Coral Pixels

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Tanukizamurai
**METADATA.pb path**: `ofl/coralpixels/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/tanukifont/Coral-Pixels |
| Commit | `2817da74e36af89291ed233f6e2d799554eff991` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/tanukifont/Coral-Pixels`. This matches the copyright string in the font file ("Copyright 2024 The Coral Pixels Project Authors (https://github.com/tanukifont/Coral-Pixels)"). The initial onboarding commit `c7ee9d63` in google/fonts (2025-03-28) by Emma Marichal explicitly states: "Taken from the upstream repo https://github.com/tanukifont/Coral-Pixels at commit https://github.com/tanukifont/Coral-Pixels/commit/2817da74e36af89291ed233f6e2d799554eff991."

## How the Commit Hash Was Identified

The commit hash `2817da74e36af89291ed233f6e2d799554eff991` is explicitly referenced in the initial onboarding commit `c7ee9d63` in google/fonts (2025-03-28, author: Emma Marichal). The commit message states: "Taken from the upstream repo https://github.com/tanukifont/Coral-Pixels at commit https://github.com/tanukifont/Coral-Pixels/commit/2817da74e36af89291ed233f6e2d799554eff991."

This commit was verified to exist in the upstream repo. It is a merge commit dated 2025-03-22 with the message "Merge pull request #1 from emmamarichal/main" and the description "Coral Pixel on Google Fonts!". This is the only commit in the repository, representing the initial setup of the upstream repo by Emma Marichal in preparation for onboarding to Google Fonts.

The onboarding was merged into google/fonts via PR #9274 on 2025-04-01.

## How Config YAML Was Resolved

The config file `sources/config.yaml` exists in the upstream repository at the recorded commit hash `2817da74`. It contains gftools-builder configuration:

```yaml
sources:
  - CoralPixels.glyphs
familyName: "Coral Pixels"
outputDir: ../fonts
ttDir: $outputDir/ttf
buildTTF: true
buildOTF: false
```

The `config_yaml` field in METADATA.pb was added by a later commit `0ebca658` in google/fonts (2025-09-04, "sources info for Coral Pixels"), which added the `config_yaml: "sources/config.yaml"` line to the existing source block. No override config.yaml exists in the google/fonts family directory (`ofl/coralpixels/`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2025-03-22 11:47:17 +0900
- Commit message: "Merge pull request #1 from emmamarichal/main"
- Source files at commit: `sources/CoralPixels.glyphs`, `sources/config.yaml`, `sources/CustomFilter_GF_Latin_All.plist`
- Pre-built font: `fonts/ttf/CoralPixels-Regular.ttf`
- Upstream repo is clean and on branch `main`
- The upstream repo has only this single commit (the merge commit)

## Confidence

**High**: The repository URL is confirmed by the copyright string, the onboarding commit message, and the METADATA.pb source block. The commit hash is directly referenced in the onboarding commit message and is the sole commit in the upstream repository. The config.yaml is present at the referenced commit in the expected location (`sources/config.yaml`). The source file is a `.glyphs` file (CoralPixels.glyphs), which is fully compatible with gftools-builder. All metadata fields are consistent and verified.

## Open Questions

None. All source metadata is complete and verified.
