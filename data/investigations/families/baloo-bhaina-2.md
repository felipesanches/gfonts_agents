# Baloo Bhaina 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloobhaina2/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | da523dfa21aa0e376253d61c21e39146dc55702a |
| Config YAML | builder/BalooBhaina2.yaml |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block. This is a fork of the canonical `https://github.com/EkType/Baloo2-Variable` repository. The font copyright references `https://github.com/EkType/Baloo2` (the original non-Variable repo).

PR #3988 ("Baloo Bhaina 2: Version 1.700 added") explicitly states: "taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa..."

## How the Commit Hash Was Identified

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` was identified from the google/fonts commit `35975c1b3` (2021-10-29) with message: "Baloo Bhaina 2: Version 1.700 added (#3988)". The commit body states: "[gftools-packager] Baloo Bhaina 2: Version 1.700 added ... taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa..."

Cross-verification: The upstream commit `da523df` is dated 2021-10-28, while the google/fonts merge was on 2021-10-29, giving only a 1-day gap. This is the fastest turnaround among the Baloo 2 families onboarded at this time, suggesting it was processed quickly alongside the other families.

This is the same upstream commit used for Baloo 2 (merged 2021-11-25) and Baloo Bhai 2 (merged 2021-11-03). All three were built from the same upstream snapshot since all Baloo 2 families share a single monorepo.

## How Config YAML Was Resolved

The config file `builder/BalooBhaina2.yaml` is specified in the METADATA.pb `source` block and was verified to exist at commit `da523df`. Contents:

```yaml
sources:
  - ../sources/BalooBhaina2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

No override config.yaml exists in the google/fonts family directory (`ofl/baloobhaina2/`).

## Verification

- **Commit exists in upstream repo**: Yes, in EkType/Baloo2-Variable (parent repo). Also accessible via GitHub API on yanone/Baloo2-Variable (fork).
- **Commit date**: 2021-10-28 17:08:59 +0200
- **Commit message**: "Update BalooTammudu2[wght].ttf"
- **Source files at commit**: `sources/BalooBhaina2.glyphs` (among 10 family .glyphs files)
- **Font files at commit**: `fonts/variable/BalooBhaina2[wght].ttf` (among 10 family variable fonts)
- **Builder config at commit**: `builder/BalooBhaina2.yaml` (confirmed present)

## Confidence

**HIGH**: All data is consistent across multiple sources. The PR, commit body, and METADATA.pb all agree. The commit date (2021-10-28) is just 1 day before the google/fonts merge (2021-10-29). The same commit was used for Baloo 2, Baloo Bhai 2, and Baloo Bhaina 2.

**Minor concern**: Same as Baloo 2 and Baloo Bhai 2 -- the METADATA.pb points to yanone's fork rather than the EkType parent repo.

## Open Questions

1. Should the `repository_url` be updated to `https://github.com/EkType/Baloo2-Variable` (the parent repo) for consistency with Baloo Bhaijaan 2 which already points to EkType? The commit `da523df` exists in the EkType repo's history (merged via PR #2). PR #4104 attempted to correct EkType repo URLs for some Baloo families.
