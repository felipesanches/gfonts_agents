# Big Shoulders Stencil

**Status**: `complete`
**Date**: 2026-02-26
**Designer**: Patric King
**License**: OFL
**METADATA.pb**: `ofl/bigshouldersstencil/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `8ba99c9e347396d828b263b8b818269cb99eb27c` |
| Config YAML | `Big-Shoulders-Stencil/sources/config.yml` (upstream) |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url` and confirmed by the copyright string. All Big Shoulders variants share the same upstream repository.

### Commit Hash
The google/fonts commit `3b113037a` ("Big Shoulders Stencil: Version 2.001 added", 2025-02-07) explicitly states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit 8ba99c9e347396d828b263b8b818269cb99eb27c."

Binary verification: The SHA256 of `Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf` at commit `8ba99c9` in upstream matches the current file in google/fonts (`758ec880296a8bdaf736a31fc57e90fa16673d8c357efc3c36bdb6582d625f0a`).

### Config YAML
The METADATA.pb specifies `config_yaml: "Big-Shoulders-Stencil/sources/config.yml"` pointing to the upstream repo. This file exists at commit `8ba99c9` and contains a gftools-builder configuration for the Stencil family.

This is the only one of the five Stencil/Inline Text SC families that uses the upstream config.yml rather than an override config.yaml. This makes sense because Big Shoulders Stencil is the "parent" family with the `opsz` axis -- the other variants (Display, Text, Display SC) are subspaced or remapped derivatives that require recipe-based override configs.

No override config.yaml exists in the google/fonts family directory.

## Evidence

### METADATA.pb source block
```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders-Stencil/sources/config.yml"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "Documentation/DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf" dest_file: "BigShouldersStencil[opsz,wght].ttf" }
  branch: "master"
}
```

### google/fonts history
- `3b113037a` (2025-02-07): "Big Shoulders Stencil: Version 2.001 added" -- references commit `8ba99c9`, resolves #7830
- `754593c0e`: "Update METADATA.pb - added date"
- `f8206935e`: "Update OFL.txt - url link"
- `34926685b`: "Add config_yaml to METADATA.pb for 15 font families"

### Issue #7830
Filed by vv-monsalve: "Update Big Shoulders families with `opsz` axis". This was the request to add the optical size axis variant, which Big Shoulders Stencil fulfills (it has both `opsz` and `wght` axes).

### Upstream repo cache
- Cached at: `xotypeco/big_shoulders`
- Commit `8ba99c9e347396d828b263b8b818269cb99eb27c` verified ("Update README.md", 2025-02-06)
- This is the HEAD of master at the time of onboarding
- `Big-Shoulders-Stencil/sources/config.yml` exists at this commit
- `Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf` exists and binary-matches google/fonts

## Confidence

**High**: Commit hash explicitly stated in google/fonts commit message and binary-verified via SHA256 match. Config YAML confirmed in upstream.

## Notes
- Part of the Big Shoulders superfamily (all in https://github.com/xotypeco/big_shoulders)
- This is the newest addition to Google Fonts of the five families investigated (added 2025-02-06), with the `opsz` (optical size) axis
- Commit `8ba99c9` is the most recent upstream commit (2025-02-06), making it the HEAD of master at onboarding time
- Date added to Google Fonts: 2025-02-06
