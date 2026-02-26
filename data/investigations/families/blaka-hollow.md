# Blaka Hollow

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Mohamed Gaber
**METADATA.pb path**: `ofl/blakahollow/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Gue3bara/Blaka |
| Commit | `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` |
| Config YAML | `sources/blakahollow.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/Gue3bara/Blaka` was already present in the METADATA.pb `source { repository_url }` field. Blaka Hollow shares the same upstream repository as Blaka and Blaka Ink. The URL is confirmed by the copyright string ("Copyright 2019 The Blaka Project Authors (https://github.com/Gue3bara/Blaka)") and by the gftools-packager commits in google/fonts.

The initial onboarding was done via commit `21f51aedb` (PR #4556, 2022-04-27, by Yanone), which referenced the upstream repo. The latest update was commit `1c8403b96` (2023-09-29, by Yanone).

## How the Commit Hash Was Identified

The commit hash `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is recorded in METADATA.pb. It matches the gftools-packager commit `1c8403b96` in google/fonts, which states: "Blaka Hollow Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Gue3bara/Blaka at commit https://github.com/Gue3bara/Blaka/commit/7f264eee862d3e94c2cb6a728c6429c2f3b9adc3."

This is the same commit used for the Blaka and Blaka Ink updates (all three families were updated in the same batch on 2023-09-29). The commit exists in the upstream repo with message "Bumped version to 1.003 across all fonts" and is the HEAD of the repository.

## How Config YAML Was Resolved

The config file `sources/blakahollow.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
  - temp/BlakaHollow-Regular.glyphs
outputDir: "../fonts/hollow"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/blakahollow.yaml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: Latest commit (HEAD) in the Blaka repo
- Commit message: "Bumped version to 1.003 across all fonts"
- Config YAML at commit: `sources/blakahollow.yaml` exists
- Source file referenced: `temp/BlakaHollow-Regular.glyphs` (in sources/temp/)
- Binary file in METADATA.pb: `fonts/hollow/ttf/BlakaHollow-Regular.ttf`

## Confidence

**High**: The repository URL and commit hash are consistently referenced across METADATA.pb, the gftools-packager commit in google/fonts, and the upstream repo. The commit exists and is the HEAD of the repo. The config YAML file exists at the recorded commit. All three Blaka families (Blaka, Blaka Hollow, Blaka Ink) share the same repo and commit.

## Open Questions

None. All data is verified and consistent.
