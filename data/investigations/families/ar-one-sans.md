# AR One Sans

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Niteesh Yadav
**METADATA.pb path**: `ofl/aronesans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/niteeshy/ar-one-sans |
| Commit | `6dc5e6850f2ced9f28e733c9a7860c54246e17a8` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/niteeshy/ar-one-sans`. This matches the copyright string in the font metadata ("Copyright 2018 The AR One Project Authors (https://github.com/niteeshy/ar-one-sans)"). The gftools-packager onboarding commit `29abece3f` in google/fonts also references this URL in its body. PR #6662 in google/fonts confirms it.

## How the Commit Hash Was Identified

The current METADATA.pb commit hash is `6dc5e6850f2ced9f28e733c9a7860c54246e17a8`. However, this does **not** match the original onboarding commit referenced by gftools-packager.

The original font onboarding in google/fonts was done via PR #6662, with the gftools-packager commit `29abece3f` (2023-09-06) stating: "AR One Sans Version 1.001;gftools[0.9.33] taken from the upstream repo https://github.com/niteeshy/ar-one-sans at commit https://github.com/niteeshy/ar-one-sans/commit/a463b112ca9393f1904765e0f32891b849eb9cf1."

The original onboarding commit `a463b112ca9393f1904765e0f32891b849eb9cf1` is **no longer present** in the upstream repository -- the repository appears to have been force-pushed, leaving only a single commit (`6dc5e68`, dated 2024-04-14, message: "Update README.md"). This remaining commit is from **7 months after** the original onboarding (2023-09-06), so there is a significant time gap.

The METADATA.pb source block was added by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported information from fontc_crater's target.json. The `6dc5e68` commit hash was likely used as the only available commit in the force-pushed repo.

## How Config YAML Was Resolved

The config file `sources/config.yaml` exists in the upstream repository at the recorded commit hash `6dc5e68`. It contains a comprehensive gftools-builder configuration referencing `AROneSans.glyphs` as the source file, with axis order for ARRR and wght axes, and full STAT table definitions. No override config.yaml exists in the google/fonts family directory (`ofl/aronesans/`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-04-14 20:14:41 -0700
- Commit message: "Update README.md"
- Source files at commit: `sources/AROneSans.glyphs`, `sources/config.yaml`

## Confidence

**Medium**: The repository URL is well-established and confirmed by multiple sources. The config.yaml is present and valid at the recorded commit. However, the commit hash in METADATA.pb (`6dc5e68`, dated 2024-04-14) does not match the original onboarding commit (`a463b112`) cited by gftools-packager in PR #6662 (dated 2023-09-06). The upstream repo was force-pushed, losing the original onboarding commit. The current commit is 7 months newer than the onboarding, so source files may have changed. Since this is the only commit remaining in the repo, it is used as the best available reference, but it may not exactly reproduce the original onboarded fonts.

## Open Questions

1. The original onboarding commit `a463b112ca9393f1904765e0f32891b849eb9cf1` is no longer present in the upstream repo. The current METADATA.pb commit `6dc5e68` is from 2024-04-14, 7 months after the onboarding on 2023-09-06. Were the source files (`AROneSans.glyphs`) modified during that period? If so, the fonts built from this commit may differ from what was originally onboarded.
2. Should the commit hash be flagged as "best available but not original onboarding commit" in the tracking data?
