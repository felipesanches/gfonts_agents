# Baloo Thambi 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloothambi2/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `ffd6308743a5829fe6980ce86f5629ba0250df98` |
| Config YAML | `builder/BalooThambi2.yaml` |
| Branch | `master` |

## How the Repository URL Was Found
The repository URL was explicitly documented in the METADATA.pb `source {}` block. It is also referenced in the copyright string of the font files. The gftools-packager commit message in google/fonts (397ea6e1a, 2021-11-26) confirms: "Baloo Thambi 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable".

## How the Commit Hash Was Identified
The gftools-packager commit message (397ea6e1a) explicitly states: "at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98". This matches the commit hash in METADATA.pb.

## How Config YAML Was Resolved
The config file `builder/BalooThambi2.yaml` exists at the referenced commit in the upstream repo. It points to `../sources/BalooThambi2.glyphs` as the source and builds only variable fonts.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2021-11-19 11:34:42 +0100
- Commit message: "Update BalooChettan2[wght].ttf"
- Source files at commit: `sources/BalooThambi2.glyphs` (plus 9 other Baloo family .glyphs files in this monorepo)
- TTFs last updated in google/fonts: 2021-11-26 (commit 397ea6e1a)
- No override config.yaml in google/fonts family directory

## Confidence
**High**: The gftools-packager commit message explicitly references both the upstream repo and the exact commit hash. The config.yaml exists at the commit. All data is consistent.

## Open Questions
None
