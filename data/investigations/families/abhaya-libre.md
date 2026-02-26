# Abhaya Libre

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Mooniak
**METADATA.pb path**: `ofl/abhayalibre/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/mooniak/abhaya-libre-font |
| Commit | `f53da70786fe1dba6193bdbd45a2c4159e511079` |
| Config YAML | override in google/fonts |
| Branch | -- |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field: `https://github.com/mooniak/abhaya-libre-font`. This URL was added to google/fonts in commit `aec1b9f3e` ("Add upstream repository URL"). The URL matches the copyright holder "Mooniak" listed in the font files.

## How the Commit Hash Was Identified

The commit hash `f53da70786fe1dba6193bdbd45a2c4159e511079` was pre-existing in the METADATA.pb `source { commit }` field. This commit was added to METADATA.pb via commits `04009b5bb` and `5862ed413` ("sources info for Abhaya Libre").

**Important note on commit relevance**: This commit (`f53da70`, dated 2024-05-31) is the HEAD of the upstream repository -- its message is "Update to GF repo tempalte and CI". It is NOT the original onboarding commit. The actual last font-modifying commit in google/fonts on the main branch is `f8dbc76905437e` from 2017-02-17, created via PR #665 ("abhayalibre: v1.050 added"), submitted by `m4rc1e`. The PR body simply says "Fixes #460."

At the time of PR #665, the upstream repo's HEAD was approximately `ade314aa` ("Adding description for Google Fonts"). The referenced commit `f53da70` represents a much later state of the upstream repo with CI and template updates. This commit was likely chosen for the `config_yaml` field pointing to `sources/config.yaml`, which only exists at this newer commit.

The upstream repo has had significant development since 2017, including source file reorganization (the main source file changed from `sources/glyphs/Abhaya-Masters.glyphs` to `sources/AbhayaLibre.glyphs`).

## How Config YAML Was Resolved

An override `config.yaml` exists in the google/fonts family directory at `ofl/abhayalibre/config.yaml`. Its contents:

```yaml
sources:
  - sources/glyphs/Abhaya-Masters.glyphs
buildStatic: true
buildVariable: false
```

This override references the source file path `sources/glyphs/Abhaya-Masters.glyphs`, which matches the file structure at the original onboarding time (circa 2017). The upstream repo's own `sources/config.yaml` at commit `f53da70` references `AbhayaLibre.glyphs` (relative path) and is configured for variable font builds, which differs from the static fonts currently in the Google Fonts catalog.

The METADATA.pb also has `config_yaml: "sources/config.yaml"` pointing to the upstream config. Since a local override exists, this field could be considered redundant, but it documents where the upstream config lives.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-05-31 08:15:08 +0530
- Commit message: "Update to GF repo tempalte and CI"
- Source files at commit: `sources/AbhayaLibre.glyphs`, `sources/config.yaml`, plus multiple historical `.glyphs` and `.ufo` files in `documentation/development/`

## Confidence

**Medium**: The repository URL is well-established and verified. However, the commit hash in METADATA.pb (`f53da70`) does not correspond to the original onboarding commit -- it is the repo HEAD from 2024, significantly newer than the 2017 font onboarding via PR #665. The override config.yaml correctly references the older source file structure (`sources/glyphs/Abhaya-Masters.glyphs`), which suggests the override was written with knowledge of the actual onboarding state. The current METADATA.pb commit reference is a pragmatic choice to support the `config_yaml` field pointing to the upstream's `sources/config.yaml`.

## Open Questions

- The commit `f53da70` in METADATA.pb is the repo HEAD (2024), not the original onboarding commit from ~2017. Should the commit reference be updated to match the actual state used for onboarding (approximately `ade314aa` or earlier)?
- The upstream repo has had significant changes since 2017, including adding Tamil support and renaming source files. Is a font update from the newer upstream planned?
