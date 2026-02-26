# Advent Pro

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: VivaRado
**METADATA.pb path**: `ofl/adventpro/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/Advent |
| Commit | `d206a139ee9045993fbd1e530b93f28f8bf4e3b1` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in METADATA.pb in the `source { repository_url }` field: `https://github.com/googlefonts/Advent`. This is consistent with the copyright notice in the font files: "Copyright 2018 The Advent Pro Project Authors (https://github.com/googlefonts/Advent)".

The `googlefonts` GitHub organization is the canonical home for Google Fonts projects that have been adopted under Google's maintenance.

## How the Commit Hash Was Identified

The commit hash `d206a139ee9045993fbd1e530b93f28f8bf4e3b1` was already present in METADATA.pb and is corroborated by multiple sources:

1. **Merged commit message** in google/fonts (commit `ce1042736e67`, PR #5522, 2022-12-01): The final squashed commit body explicitly states: "Advent Pro Version 3.000 taken from the upstream repo https://github.com/googlefonts/Advent at commit https://github.com/googlefonts/Advent/commit/d206a139ee9045993fbd1e530b93f28f8bf4e3b1."

2. **PR #5522 initial body** referenced a different commit (`036dd5878f3b92c39fd74def865e6b2755bba8ba`) -- this was the initial packager run. The commit was updated during the PR review process, and the final merged version uses `d206a139`.

3. The commit `036dd587` from the initial PR body no longer exists in the upstream repo (the repo is a shallow clone with only the `d206a139` commit visible), but the correct final commit is present and verified.

The commit `d206a139` dates to 2022-11-25, about one week before the google/fonts merge on 2022-12-01, which is a typical timeline for font packager PRs.

## How Config YAML Was Resolved

The `sources/config.yaml` file exists in the upstream repository at the recorded commit. Its contents:

```yaml
sources:
  - AdventPro.designspace
axisOrder:
  - wdth
  - wght
  - ital
familyName: Advent Pro
buildOTF: false
buildTTF: true
buildWebfont: false
buildStatic: false
buildVariable: true
```

This is a standard gftools-builder configuration for a variable font with width, weight, and italic axes. The `config_yaml: "sources/config.yaml"` field is correctly set in METADATA.pb.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-11-25 16:46:12 +0100
- Commit message: "Latest binaries"
- Source files at commit: Multiple `.designspace` files and `.ufo` directories under `font_source/UFOs/latest/`, plus `sources/config.yaml`

Key source files include:
- `font_source/UFOs/latest/adv_wght_wdth.designspace`
- `font_source/UFOs/latest/adv_wght_wdth_ital.designspace`
- `font_source/EFO/font.designspace`
- Multiple `.ufo` font directories

## Confidence

**High**: All three key fields (repository_url, commit, config_yaml) were pre-existing in METADATA.pb. The commit hash is corroborated by the gftools-packager commit message in google/fonts (PR #5522). The config.yaml exists at the recorded commit and is a valid gftools-builder configuration. The timeline is consistent (upstream commit 2022-11-25, google/fonts merge 2022-12-01).

## Open Questions

None -- this family is fully documented and verified.
