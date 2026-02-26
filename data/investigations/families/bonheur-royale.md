# Bonheur Royale

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/bonheurroyale/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/bonheur-royale |
| Commit | `90087bb825c798641a29d2a1114ce7acd4048b0b` |
| Config YAML | `sources/config.yml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/bonheur-royale` was initially set during the original font onboarding via PR #3675 by Viviana Monsalve (2021-08-10). The PR body explicitly states: "taken from the upstream repo https://github.com/googlefonts/bonheur-royale". This URL also matches the copyright string in the font files. The source block was later added to METADATA.pb in commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb", 2024-04-03).

## How the Commit Hash Was Identified

The commit hash `90087bb825c798641a29d2a1114ce7acd4048b0b` was added to METADATA.pb in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31) by Felipe Sanches, which ported information from fontc_crater's target.json.

**Important note**: This commit (`90087bb`, "Nhung added to Contributors") is the **latest** commit in the upstream repo (HEAD), but it is **not** the original onboarding commit. The original onboarding commit referenced in PR #3675 was `5437451c7ef27d37081b96d4f73c445ca1813b10` ("py for sample imagge added").

However, the difference between the two commits is minimal:

```
90087bb Nhung added to Contributors  <-- current METADATA.pb (HEAD)
5437451 py for sample imagge added   <-- original onboarding commit
```

The only change between commit `5437451` and `90087bb` is adding a name to the CONTRIBUTORS file. No source files, fonts, or build configuration changed. The `sources/config.yml` is identical at both commits.

## How Config YAML Was Resolved

The config file `sources/config.yml` (note: `.yml` extension, not `.yaml`) exists in the upstream repository at both the original onboarding commit and the current recorded commit. Its contents:

```yaml
sources:
  - BonheurRoyale.glyphs
familyName: "Bonheur Royale"
buildVariable: false
# autohintTTF: false
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (HEAD of master)
- Commit message: "Nhung added to Contributors"
- Original onboarding commit: `5437451c7ef27d37081b96d4f73c445ca1813b10`
- Source files at recorded commit: `sources/BonheurRoyale.glyphs`, `sources/config.yml`
- Config.yml present: Yes (note `.yml` extension)
- No override config.yaml in google/fonts family directory

## Confidence

**High**: The repository URL is well-established and confirmed by multiple sources (PR #3675, copyright string, upstream.yaml). The commit hash `90087bb` is the HEAD of the repo rather than the original onboarding commit (`5437451`), but the only difference is a CONTRIBUTORS file update -- no source files changed. The config.yml is present and valid at the recorded commit.

## Open Questions

1. The recorded commit `90087bb` is the repo HEAD, not the original onboarding commit `5437451` from PR #3675. Should this be corrected to point to the original onboarding commit for accuracy? The functional difference is nil (only a CONTRIBUTORS file change), but for correctness the original commit may be preferred.
