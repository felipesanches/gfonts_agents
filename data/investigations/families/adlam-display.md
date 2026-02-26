# ADLaM Display

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Mark Jamra, Neil Patel, Andrew Footit
**METADATA.pb path**: `ofl/adlamdisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/microsoft/ADLaM-Display |
| Commit | `879176243e9f7161a8aefdab8c36a4a7318ebe15` |
| Config YAML | `Sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/microsoft/ADLaM-Display`. The gftools-packager onboarding commit `40699510e6bf` in google/fonts confirms this, stating in its body: "ADLaM Display Version 2.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] taken from the upstream repo https://github.com/microsoft/ADLaM-Display". PR #6522 in google/fonts also references this URL.

## How the Commit Hash Was Identified

The commit hash `879176243e9f7161a8aefdab8c36a4a7318ebe15` was already present in the METADATA.pb `source { commit }` field. This commit is directly confirmed by multiple sources:

1. The gftools-packager onboarding commit `40699510e6bf` (2023-07-10 12:48:26 -0700) body states: "taken from the upstream repo https://github.com/microsoft/ADLaM-Display at commit https://github.com/microsoft/ADLaM-Display/commit/879176243e9f7161a8aefdab8c36a4a7318ebe15"
2. PR #6522 in google/fonts repeats this exact reference
3. The upstream commit date (2023-07-10 12:36:52 -0700) is just 12 minutes before the google/fonts onboarding commit (2023-07-10 12:48:26 -0700), indicating the font was packaged immediately after the upstream commit

## How Config YAML Was Resolved

The config file `Sources/config.yaml` (note: capital "S" in `Sources`) exists in the upstream repository at the recorded commit hash. It contains gftools-builder configuration referencing the `ADLaM-Display.glyphs` source file with `buildOTF: false`. The capitalized directory name is notable -- commit `7190093b1` in google/fonts ("A few fonts have `Sources` instead of `sources` directory") specifically addressed this naming convention. No override config.yaml exists in the google/fonts family directory (`ofl/adlamdisplay/`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-07-10 12:36:52 -0700
- Commit message: "Build"
- Source files at commit: `Sources/ADLaM-Display CORNERS.glyphs`, `Sources/ADLaM-Display.glyphs`, `Sources/config.yaml`

## Confidence

**High**: All data is fully consistent. The repository URL, commit hash, and config_yaml were all pre-existing in METADATA.pb. The commit hash is directly corroborated by the gftools-packager commit message, PR #6522, and the near-simultaneous timestamps (12 minutes apart) between the upstream commit and the onboarding. The commit exists in the upstream repo and contains the expected source files and build configuration.

## Open Questions

None
