# Bona Nova SC

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Capitalics, Mateusz Machalski, Andrzej Heidrich
**METADATA.pb path**: `ofl/bonanovasc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/kosmynkab/Bona-Nova |
| Commit | `a5cbdfb8741af20ea5bfe252f0128beed6c8beed` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/kosmynkab/Bona-Nova` was present in the METADATA.pb `source { repository_url }` field from the initial font addition. The PR #7774 by Simon Cozens explicitly states: "Taken from the upstream repo https://github.com/kosmynkab/Bona-Nova at commit a5cbdfb8741af20ea5bfe252f0128beed6c8beed." This also matches the copyright string in the font files.

Note that this is the same upstream repository used by the Bona Nova (non-SC) family at `ofl/bonanova/`.

## How the Commit Hash Was Identified

The commit hash `a5cbdfb8741af20ea5bfe252f0128beed6c8beed` was set in the METADATA.pb from the initial font addition commit `e92080ad6` by Simon Cozens (2024-05-27), via PR #7774. The PR body explicitly references this exact commit. The commit exists in the upstream repository (message: "remove fontbakery report") and is the latest commit in the repo (HEAD of `main`).

## How Config YAML Was Resolved

The `sources/config.yaml` file exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
  - BonaNova.glyphs
  - BonaNova-Italic.glyphs
familyName: Bona Nova
buildVariable: False
```

**Important discrepancy**: This config.yaml specifies `familyName: Bona Nova` (not "Bona Nova SC"). The config builds the regular Bona Nova family, not the SC (Small Caps) variant. The METADATA.pb `files { }` entries claim to copy pre-built `BonaNovaSC-*.ttf` files from `fonts/ttf/` in the upstream repo, but these files do **not** exist in the upstream repository at any point in its history. Only `BonaNova-Bold.ttf`, `BonaNova-Italic.ttf`, and `BonaNova-Regular.ttf` exist at `fonts/ttf/`.

The SC fonts were most likely compiled by Simon Cozens during the PR #7774 build process, possibly using gftools-builder with a small caps transformation, and then submitted as pre-built binaries. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (HEAD of main)
- Commit date: Not explicitly shown (shallow clone was unshallowed)
- Commit message: "remove fontbakery report"
- Source files at commit: `sources/BonaNova.glyphs`, `sources/BonaNova-Italic.glyphs`, `sources/config.yaml`
- SC TTF files at commit: **Not present** (only non-SC TTFs exist)
- No override config.yaml in google/fonts family directory

## Confidence

**Medium-High**: The repository URL and commit hash are well-documented, confirmed by the PR #7774 body text and the initial commit message. However, there is a notable discrepancy: the METADATA.pb `files { }` entries reference `BonaNovaSC-*.ttf` files that do not exist in the upstream repository, and the `config.yaml` builds "Bona Nova" (not the SC variant). The SC fonts were likely built through a separate process during onboarding. The `config_yaml` field pointing to `sources/config.yaml` may not be directly useful for rebuilding the SC variant.

## Open Questions

1. How were the BonaNovaSC-*.ttf files generated? The upstream repo only contains Bona Nova (non-SC) source files and pre-built TTFs. Was a special build configuration or post-processing step used to create the Small Caps variant?
2. Should the `files { }` entries in METADATA.pb be corrected, since they reference non-existent paths in the upstream?
3. Is the `config_yaml: "sources/config.yaml"` field appropriate for the SC family, given that the config builds the non-SC family?
