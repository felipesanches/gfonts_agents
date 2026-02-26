# Baloo Bhaijaan 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloobhaijaan2/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/EkType/Baloo2-Variable |
| Commit | da4090c1dd5798a3e72d7138e379ee1f94d6349c |
| Config YAML | builder/BalooBhaijaan2.yaml |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/EkType/Baloo2-Variable` is documented in the METADATA.pb `source` block. Unlike the other Baloo 2 families (Baloo 2, Baloo Bhai 2, Baloo Bhaina 2) which reference the yanone fork, Baloo Bhaijaan 2 correctly points to the EkType parent repository. This is because Baloo Bhaijaan 2 was onboarded later (Version 1.701, September 2022) compared to the others (Version 1.700, October-November 2021), and by that time the URL had been corrected to point to the canonical upstream.

PR #5216 ("Baloo Bhaijaan 2: Version 1.701 added") confirms: "taken from the upstream repo https://github.com/EkType/Baloo2-Variable at commit da4090c1dd5798a3e72d7138e379ee1f94d6349c."

## How the Commit Hash Was Identified

The commit `da4090c1dd5798a3e72d7138e379ee1f94d6349c` was identified from the google/fonts commit `d3d979f3d` (2022-09-13) with message: "[gftools-packager] Baloo Bhaijaan 2: Version 1.701 added (#5216)". The commit body states: "Baloo Bhaijaan 2 Version 1.701 taken from the upstream repo https://github.com/EkType/Baloo2-Variable at commit da4090c1dd5798a3e72d7138e379ee1f94d6349c."

Cross-verification: The upstream commit `da4090c` is dated 2022-09-09 18:21:28 +0530, while the google/fonts merge was on 2022-09-13, giving a 4-day gap. This is consistent with a rapid onboarding cycle.

The upstream commit `da4090c` is a merge commit: "Merge pull request #5 from yanone/master". This merge brought in commit `29ddd81` ("Regenerated fonts as 1.701 without data changes") from the yanone fork. So the Version 1.701 update was done by yanone regenerating the fonts, then merging that work into the EkType parent repo.

## How Config YAML Was Resolved

The config file `builder/BalooBhaijaan2.yaml` is specified in the METADATA.pb `source` block and was verified to exist at commit `da4090c`. Contents:

```yaml
sources:
  - ../sources/BalooBhaijaan2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

No override config.yaml exists in the google/fonts family directory (`ofl/baloobhaijaan2/`).

## Verification

- **Commit exists in upstream repo**: Yes, verified in `/mnt/shared/upstream_repos/fontc_crater_cache/EkType/Baloo2-Variable/`
- **Commit date**: 2022-09-09 18:21:28 +0530
- **Commit message**: "Merge pull request #5 from yanone/master"
- **Source files at commit**: `sources/BalooBhaijaan2.glyphs` (among 10 family .glyphs files)
- **Font files at commit**: `fonts/variable/BalooBhaijaan2[wght].ttf` (among 10 family variable fonts)
- **Builder config at commit**: `builder/BalooBhaijaan2.yaml` (confirmed present)

## Confidence

**HIGH**: All data is fully consistent. The METADATA.pb correctly points to the EkType parent repo (not the yanone fork). The commit hash matches the gftools-packager message. The commit date is 4 days before the google/fonts merge, which is consistent with normal processing time. The `da4090c` merge commit is the tip of the EkType repo's master branch, representing the latest state at onboarding time.

## Open Questions

None. This family's source data is correctly documented and verified.
