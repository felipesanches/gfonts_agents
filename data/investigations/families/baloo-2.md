# Baloo 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloo2/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | da523dfa21aa0e376253d61c21e39146dc55702a |
| Config YAML | builder/Baloo2.yaml |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block. This is a fork of the original `https://github.com/EkType/Baloo2-Variable` repository. The yanone fork was used for the onboarding because yanone (the font engineer) did the work to make the fonts compatible with gftools-builder and created the builder YAML configs.

PR #3981 ("Baloo 2: Version 1.700 added") explicitly references: "Baloo 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa21aa0e376253d61c21e39146dc55702a."

**Important note about the repo relationship**: yanone/Baloo2-Variable is a fork of EkType/Baloo2-Variable (confirmed via GitHub API). The commit `da523df` was authored by yanone in a branch that was merged into EkType via pull request #2 (merge commit `a5f0e0d`). The commit exists in both repos' histories via GitHub's fork object sharing, but the local shallow clone of yanone's repo only has 1 commit (`29ddd81`).

## How the Commit Hash Was Identified

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` was identified from the google/fonts commit `8e0cd0588` (2021-11-25) with message: "Baloo 2: Version 1.700 added (#3981)". The commit body states: "[gftools-packager] Baloo 2: Version 1.700 added ... taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit da523dfa..."

PR #3981 body confirms the same information.

Cross-verification: The upstream commit `da523df` is dated 2021-10-28, while the google/fonts merge was on 2021-11-25, giving a ~28-day gap consistent with a normal review period.

## How Config YAML Was Resolved

The config file `builder/Baloo2.yaml` is specified in the METADATA.pb `source` block. It was verified to exist at commit `da523df` in the upstream repo. Contents:

```yaml
sources:
  - ../sources/Baloo2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

No override config.yaml exists in the google/fonts family directory (`ofl/baloo2/`).

## Verification

- **Commit exists in upstream repo**: Yes, in EkType/Baloo2-Variable (parent repo). Also accessible via GitHub API on yanone/Baloo2-Variable (fork).
- **Commit date**: 2021-10-28 17:08:59 +0200
- **Commit message**: "Update BalooTammudu2[wght].ttf"
- **Source files at commit**: `sources/Baloo2.glyphs` (and 9 other family .glyphs files)
- **Font files at commit**: `fonts/variable/Baloo2[wght].ttf` (and 9 other family variable fonts)
- **Builder config at commit**: `builder/Baloo2.yaml` (confirmed present)

## Confidence

**HIGH**: All data is consistent across multiple sources. The PR, commit message body, and METADATA.pb all agree on the repository URL and commit hash. The commit date is temporally consistent with the google/fonts merge date. The config.yaml exists at the referenced commit.

**Minor concern**: The METADATA.pb points to the yanone fork rather than the EkType parent repo. The commit `da523df` was originally authored by yanone but was later merged into the EkType parent. The local shallow clone of yanone's repo does not contain this commit (only has `29ddd81`), but GitHub's API resolves it through fork object sharing. For build reproducibility purposes, using the EkType parent URL might be more reliable long-term.

## Open Questions

1. Should the `repository_url` be updated to `https://github.com/EkType/Baloo2-Variable` (the parent repo) instead of `https://github.com/yanone/Baloo2-Variable` (the fork)? The commit `da523df` is natively part of the EkType repo's history (merged via PR #2), while the yanone fork only has it through GitHub's shared object store. PR #4104 ("Correct EkType Github Repo URL") was submitted to address this for some Baloo families, but it appears Baloo 2 was not updated.
