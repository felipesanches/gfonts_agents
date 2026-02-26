# Big Shoulders Stencil Display SC

**Status**: `complete`
**Date**: 2026-02-26
**Designer**: Patric King
**License**: OFL
**METADATA.pb**: `ofl/bigshouldersstencildisplaysc/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `0b3d09a86862b19efae28eae0cd868f17c476b20` |
| Config YAML | Override config.yaml in google/fonts |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url` and confirmed by the copyright string. All Big Shoulders variants share the same upstream repository.

### Commit Hash
The google/fonts commit `270facc12` ("Big Shoulders Stencil Display SC: Version 2.001 added", 2024-05-30) explicitly states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit 0b3d09a86862b19efae28eae0cd868f17c476b20."

Commit `0b3d09a` in upstream ("regenerate font files", 2024-02-26) was verified to exist.

Note: The SC variant font binary does not exist in the upstream repository at this commit. The `BigShouldersStencilDisplaySC[wght].ttf` file listed in METADATA.pb's `source_file` is not present in `Big-Shoulders-Stencil/fonts/variable/display/` at commit `0b3d09a` -- only `BigShouldersStencilDisplay[wght].ttf` (without SC) exists. The SC variant is built via the override config.yaml recipe, which applies a `smcp -> ccmp` remap operation to the source.

### Config YAML
An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersstencildisplaysc/config.yaml`. It uses a recipe-based build that:
1. Builds from `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`
2. Subspaces to `opsz=72` (display optical size)
3. Remaps `smcp -> ccmp` to produce the small caps variant
4. Renames to "Big Shoulders Stencil Display SC"

The config also builds the non-SC Display variant in the same recipe. It is identical to the override config in `ofl/bigshouldersstencildisplay/config.yaml`.

## Evidence

### METADATA.pb source block
```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "Documentation/DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "Big-Shoulders-Stencil/fonts/variable/display/BigShouldersStencilDisplaySC[wght].ttf" dest_file: "BigShouldersStencilDisplaySC[wght].ttf" }
  branch: "master"
}
```

### google/fonts history
- `270facc12` (2024-05-30): "Big Shoulders Stencil Display SC: Version 2.001 added" -- references commit `0b3d09a`
- `1d1d3e864`: "Add SC line to description"
- `94e9f371f`: "Update DESCRIPTION.en_us.html"
- `3674711b2`: "Update OFL.txt"

### Upstream repo cache
- Cached at: `xotypeco/big_shoulders`
- Commit `0b3d09a86862b19efae28eae0cd868f17c476b20` verified ("regenerate font files", 2024-02-26)
- Source file `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs` exists at this commit
- `Big-Shoulders-Stencil/sources/config.yml` exists at this commit

## Confidence

**High**: Commit hash explicitly stated in google/fonts commit message. Verified in upstream repo. Override config.yaml handles SC variant build.

## Notes
- Part of the Big Shoulders superfamily (all in https://github.com/xotypeco/big_shoulders)
- Same commit `0b3d09a` and same addition date (2024-05-30) as Big Shoulders Inline Text SC
- The override config.yaml in `bigshouldersstencildisplaysc` is identical to the one in `bigshouldersstencildisplay` -- both build Display and Display SC variants
- The METADATA.pb `source_file` references a file that doesn't exist in upstream at that commit -- the SC font is built via the override config recipe
- Date added to Google Fonts: 2024-05-30
