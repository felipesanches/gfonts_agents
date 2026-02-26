# Atkinson Hyperlegible

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Braille Institute, Applied Design Works, Elliott Scott, Megan Eiswerth, Linus Boman, Theodore Petrosky
**METADATA.pb path**: `ofl/atkinsonhyperlegible/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible |
| Commit | `1cb311624b2ddf88e9e37873999d165a8cd28b46` |
| Config YAML | `sources/config.yml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/atkinson-hyperlegible` was added to METADATA.pb by Simon Cozens in commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb", 2024-04-03). This was part of a systematic effort to merge upstream repository information from `upstream.yaml` files into METADATA.pb source blocks. The URL is also explicitly referenced in the google/fonts onboarding commit body for PR #3362: "taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible".

## How the Commit Hash Was Identified

The commit hash `1cb311624b2ddf88e9e37873999d165a8cd28b46` was added in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), porting data from the fontc_crater targets.json file. This commit hash is also directly referenced in the google/fonts onboarding PR #3362 body, which states: "taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible at commit https://github.com/googlefonts/atkinson-hyperlegible/commit/1cb311624b2ddf88e9e37873999d165a8cd28b46."

PR #3362 was created by `vv-monsalve` and merged on 2021-05-07. The font was initially added to Google Fonts on 2021-04-30, and this was the onboarding commit using gftools-packager.

## How Config YAML Was Resolved

The config file `sources/config.yml` (note: `.yml` extension, not `.yaml`) exists in the upstream repository at the referenced commit. It was added to METADATA.pb in the same [Batch 1/4] commit that added the commit hash. The config specifies:

- Two .glyphs source files: `AtkinsonHyperlegible.glyphs` and `AtkinsonHyperlegible-Italic.glyphs`
- `buildVariable: false` (static font build)
- Family name: "Atkinson Hyperlegible"

There is no override config.yaml in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2021-04-29 22:23:13 -0500
- Commit message: "OFL single line"
- Source files at commit: `sources/AtkinsonHyperlegible.glyphs`, `sources/AtkinsonHyperlegible-Italic.glyphs`, `sources/config.yml`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts onboarding PR #3362 body, providing a direct paper trail. The repository is under the `googlefonts` organization. The config.yml exists at the referenced commit and correctly lists the source files. The METADATA.pb files block includes explicit file mappings from the upstream repo to the google/fonts directory.

## Open Questions

None
