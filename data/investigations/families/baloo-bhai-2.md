# Baloo Bhai 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloobhai2/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | da523dfa21aa0e376253d61c21e39146dc55702a |
| Config YAML | builder/BalooBhai2.yaml |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block. Like Baloo 2, this is a fork of the EkType/Baloo2-Variable parent repository. The font copyright references `https://github.com/EkType/Baloo2` (the original non-Variable repo), while the build sources come from the Variable fork.

PR #3982 ("Baloo Bhai 2: Version 1.700 added") explicitly references this URL and commit.

## How the Commit Hash Was Identified

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` was identified from the google/fonts commit `29d0f9137` (2021-11-03) with message: "Baloo Bhai 2: Version 1.700 added (#3982)". The commit body states: "[gftools-packager] Baloo Bhai 2: Version 1.700 added ... taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa..."

PR #3982 body confirms the same information.

Cross-verification: The upstream commit `da523df` is dated 2021-10-28, while the google/fonts merge was on 2021-11-03, giving a ~6-day gap. This is the same commit used for Baloo 2 and Baloo Bhaina 2, since all the Baloo 2 families (except Bhaijaan) were onboarded from the same upstream commit.

## How Config YAML Was Resolved

The config file `builder/BalooBhai2.yaml` is specified in the METADATA.pb `source` block and was verified to exist at commit `da523df`. Contents:

```yaml
sources:
  - ../sources/BalooBhai2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

No override config.yaml exists in the google/fonts family directory (`ofl/baloobhai2/`).

## Verification

- **Commit exists in upstream repo**: Yes, in EkType/Baloo2-Variable (parent repo). Also accessible via GitHub API on yanone/Baloo2-Variable (fork).
- **Commit date**: 2021-10-28 17:08:59 +0200
- **Commit message**: "Update BalooTammudu2[wght].ttf"
- **Source files at commit**: `sources/BalooBhai2.glyphs` (among 10 family .glyphs files)
- **Font files at commit**: `fonts/variable/BalooBhai2[wght].ttf` (among 10 family variable fonts)
- **Builder config at commit**: `builder/BalooBhai2.yaml` (confirmed present)

## Confidence

**HIGH**: All data is consistent across multiple sources. The PR, commit body, and METADATA.pb all agree. The commit date predates the google/fonts merge. The same commit was used for Baloo 2, Baloo Bhai 2, and Baloo Bhaina 2.

**Minor concern**: Same as Baloo 2 -- the METADATA.pb points to yanone's fork rather than the EkType parent repo, which is the canonical upstream.

## Open Questions

1. Should the `repository_url` be updated to `https://github.com/EkType/Baloo2-Variable` (the parent repo)? The commit `da523df` was authored by yanone but merged into EkType via PR #2. PR #4104 attempted to correct EkType repo URLs for some Baloo families.
