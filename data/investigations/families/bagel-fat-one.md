# Bagel Fat One

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Kyungwon Kim, JAMO
**METADATA.pb path**: `ofl/bagelfatone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/JAMO-TYPEFACE/BagelFat |
| Commit | `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b` |
| Config YAML | `Sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL is documented directly in the METADATA.pb `source {}` block and also in the copyright string: "Copyright 2022 The Bagel Fat Project Authors (https://github.com/JAMO-TYPEFACE/BagelFat)". The original gftools-packager onboarding commit `d9406e5bf` (2023-05-18) also explicitly referenced this URL.

## How the Commit Hash Was Identified

The font was originally onboarded via gftools-packager on 2023-05-18 at upstream commit `5ff1333d3384611f499419a844e2b3006dc7cacd`. However, this commit no longer exists in the upstream repository (it was force-pushed away; the repo is currently a shallow clone with only one commit visible).

On 2023-05-24, the TTF was updated in google/fonts (commit `42021857`) with the message "Adding missing glyph from GF Kernal". The upstream merge commit `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b` ("Merge pull request #3 from aaronbell/main") is dated the same day (2023-05-24), indicating Aaron Bell pushed the fix upstream and then the binary was updated in google/fonts.

The commit hash was later updated from `5ff1333` to `d8dd4e8` by the fontc_crater batch import (commit `19cdcec59` on 2025-03-31). The `config_yaml` path was initially set as `sources/config.yaml` (lowercase) but corrected to `Sources/config.yaml` (uppercase) in commit `7190093b1`.

## How Config YAML Was Resolved

The config.yaml exists in the upstream repository at `Sources/config.yaml`. It was added as part of the fontc_crater batch import. No override config.yaml exists in the google/fonts family directory. The config contains:

```yaml
sources:
  - BagelFat.glyphs
familyName: "Bagel Fat One"
buildOTF: false
```

## Verification

- Commit exists in upstream repo: Yes (it is the HEAD/only visible commit in the shallow clone)
- Commit date: 2023-05-24 09:58:56 -0700
- Commit message: "Merge pull request #3 from aaronbell/main"
- Source files at commit: `Sources/BagelFat.glyphs`, `Sources/config.yaml`

## Confidence

**High**: The commit `d8dd4e8` corresponds to the latest binary update in google/fonts (both dated 2023-05-24). While the original onboarding commit `5ff1333` was the initial upload, the current binaries reflect the subsequent fix (PR #3 for missing glyph). The original commit no longer exists due to force-push, making `d8dd4e8` the only verifiable reference point.

## Open Questions

- The original onboarding commit `5ff1333` was lost due to a force-push in the upstream repository. This cannot be recovered. The current commit `d8dd4e8` correctly reflects the state of the binaries currently in google/fonts.
