# Blaka Ink

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Mohamed Gaber
**METADATA.pb path**: `ofl/blakaink/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Gue3bara/Blaka |
| Commit | `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` |
| Config YAML | `sources/blakaink.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/Gue3bara/Blaka` was already present in the METADATA.pb `source { repository_url }` field. Blaka Ink shares the same upstream repository as Blaka and Blaka Hollow. The URL is confirmed by the copyright string ("Copyright 2019 The Blaka Project Authors (https://github.com/Gue3bara/Blaka)").

Blaka Ink has a more complex history than its sibling families. It was first test-loaded by Rod Sheeter (`4e93e54fd`, 2022-04-07) as a color font experiment. The proper v1.001 onboarding was done via PR #4667 (`b6afa0153`, 2022-05-13, by Rosalie Wagner), which referenced the upstream repo at commit `df0ea4f92f29bb6af8dc9984d81fe1aaec1a7186`. It was subsequently updated to v1.002 (`450cec3f9`, 2023-03-21, by Yanone, at commit `023c078707d89764cbe9e720c37c11511eb1686b`) and v1.003 (`7dc85ffdb`, 2023-09-29, by Yanone, at the current commit).

## How the Commit Hash Was Identified

The commit hash `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is recorded in METADATA.pb. It matches the gftools-packager commit `7dc85ffdb` in google/fonts, which states: "Blaka Ink Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Gue3bara/Blaka at commit https://github.com/Gue3bara/Blaka/commit/7f264eee862d3e94c2cb6a728c6429c2f3b9adc3."

This is the same commit used for all three Blaka family updates (done in the same batch on 2023-09-29). The commit exists in the upstream repo with message "Bumped version to 1.003 across all fonts" and is the HEAD of the repository.

Previous upstream commits used for this family:
- v1.001: `df0ea4f92f29bb6af8dc9984d81fe1aaec1a7186` (PR #4667)
- v1.002: `023c078707d89764cbe9e720c37c11511eb1686b` (gftools-packager commit `450cec3f9`)

## How Config YAML Was Resolved

The config file `sources/blakaink.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
  - Blaka-Ink.glyphs
outputDir: "../fonts/ink"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/blakaink.yaml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: Latest commit (HEAD) in the Blaka repo
- Commit message: "Bumped version to 1.003 across all fonts"
- Config YAML at commit: `sources/blakaink.yaml` exists
- Source file referenced: `Blaka-Ink.glyphs` (relative to sources/ directory)
- Binary file in METADATA.pb: `fonts/ink/ttf/BlakaInk-Regular.ttf`

## Confidence

**High**: The repository URL and commit hash are consistently referenced across METADATA.pb, the gftools-packager commit in google/fonts, and the upstream repo. The commit exists and is the HEAD of the repo. The config YAML file exists at the recorded commit. All three Blaka families share the same repo and commit.

## Open Questions

None. All data is verified and consistent. Blaka Ink has a richer update history than Blaka and Blaka Hollow, including color font experiments and multiple version updates, but the current state is fully documented.
