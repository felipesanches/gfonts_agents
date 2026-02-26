# Big Shoulders Inline Text SC

**Status**: `complete`
**Date**: 2026-02-26
**Designer**: Patric King
**License**: OFL
**METADATA.pb**: `ofl/bigshouldersinlinetextsc/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `0b3d09a86862b19efae28eae0cd868f17c476b20` |
| Config YAML | Override config.yaml in google/fonts |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url` and confirmed by the copyright string: "Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)". All Big Shoulders variants share the same upstream repository.

### Commit Hash
The google/fonts commit `6ddde5289` ("Big Shoulders Inline Text SC: Version 2.002 added", 2024-05-30) explicitly states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit 0b3d09a86862b19efae28eae0cd868f17c476b20."

Commit `0b3d09a` in upstream ("regenerate font files", 2024-02-26) was verified to exist and contains the relevant source files in `Big-Shoulders-Inline/`.

Note: The SC variant font binary does not exist at this commit in upstream. The `BigShouldersInlineTextSC[wght].ttf` file is not present in `Big-Shoulders-Inline/fonts/variable/text/` at commit `0b3d09a` -- only `BigShouldersInlineText[wght].ttf` (without SC) exists. The SC variant is built using the override config.yaml recipe, which applies a `smcp -> ccmp` remap operation to the source. The commit hash correctly references the source files used for building.

### Config YAML
An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersinlinetextsc/config.yaml`. It uses a recipe-based build that:
1. Builds from `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`
2. Subspaces to `opsz=10` (text optical size)
3. Remaps `smcp -> ccmp` to produce the small caps variant
4. Renames to "Big Shoulders Inline Text SC"

The upstream repo does have a `Big-Shoulders-Inline/sources/config.yml` at this commit, but it builds the full family (not the SC variant), so the override is necessary.

## Evidence

### METADATA.pb source block
```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "Documentation/DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "Big-Shoulders-Inline/fonts/variable/text/BigShouldersInlineTextSC[wght].ttf" dest_file: "BigShouldersInlineTextSC[wght].ttf" }
  branch: "master"
}
```

### google/fonts history
- `6ddde5289` (2024-05-30): "Big Shoulders Inline Text SC: Version 2.002 added" -- references commit `0b3d09a`
- `380119ebb`: "Add SC line to description"
- `4ea9c8031`: "Update DESCRIPTION.en_us.html"
- `7c878c616`: "Update OFL.txt"

### Upstream repo cache
- Cached at: `xotypeco/big_shoulders`
- Commit `0b3d09a86862b19efae28eae0cd868f17c476b20` verified ("regenerate font files", 2024-02-26)
- Source file `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs` exists at this commit
- `Big-Shoulders-Inline/sources/config.yml` exists at this commit

## Confidence

**High**: Commit hash explicitly stated in google/fonts commit message. Verified in upstream repo. Override config.yaml handles SC variant build.

## Notes
- Part of the Big Shoulders superfamily (all in https://github.com/xotypeco/big_shoulders)
- Same commit `0b3d09a` as Big Shoulders Stencil Display SC (both were added on the same date, 2024-05-30)
- The METADATA.pb `source_file` references a file that doesn't exist in upstream at that commit -- the SC font is built via the override config recipe, not copied from upstream
- Date added to Google Fonts: 2024-05-30
