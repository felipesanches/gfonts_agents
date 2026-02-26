# Agu Display

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Seun Badejo
**METADATA.pb path**: `ofl/agudisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/theseunbadejo/Agu-Display |
| Commit | `d520ebead8de4091a82040fe3d8f94d84c38c66f` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb source block from the initial onboarding. The onboarding commit `6913b3938` (2024-11-25) stated: "Taken from the upstream repo https://github.com/theseunbadejo/Agu-Display at commit 17a7ce91583f40d9e8f21eab6c57870a59c1b668." The copyright field also references this URL. The METADATA.pb also includes a minisite URL: https://www.agudisplay.com.

## How the Commit Hash Was Identified

The commit hash has been updated once since onboarding:

1. **Original onboarding** (PR #8487, google/fonts commit `6913b3938`, 2024-11-25): Version 1.103 was taken from upstream commit `17a7ce91583f40d9e8f21eab6c57870a59c1b668`. This commit no longer exists in the upstream repository (likely due to force-push or rebase). PR #8487 had an empty body; the commit reference was only in the commit message.

2. **Batch port from fontc_crater** (google/fonts commit `19cdcec59`, 2025-03-31): The commit hash was changed from `17a7ce91` to `d520ebead8de4091a82040fe3d8f94d84c38c66f`, based on fontc_crater's target.json data. This commit is the current HEAD of the upstream repo, dated 2025-02-10 ("Merge pull request #35 from theseunbadejo/ghactions-cairofix").

The current METADATA.pb commit `d520ebea` is from February 2025, approximately 3 months after the font was originally onboarded in November 2024. The original onboarding commit `17a7ce91` is no longer recoverable from the upstream repo.

## How Config YAML Was Resolved

The `sources/config.yaml` path was added by the batch port commit `19cdcec59` (2025-03-31). The config file exists at the recorded commit and specifies:
- Source: `AguDisplay.glyphs`
- Family name: Agu Display
- Axis order: morf (custom MORF axis for morphing between letterform styles)
- `autohintOTF: False`
- STAT table with values: Uzo (0), Ala (30), Osisi (60)

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is HEAD of the shallow clone)
- Commit date: 2025-02-10 23:52:34 +0100
- Commit message: "Merge pull request #35 from theseunbadejo/ghactions-cairofix"
- Source files at commit:
  - `sources/AguDisplay.glyphs`
  - `sources/config.yaml`
  - `documentation/Nsibidi_Libre_Skeleton.glyphs`
  - `.github/workflows/build.yaml`

## Confidence

**Medium**: The repository URL is well-established and confirmed by the onboarding commit. However, the commit hash `d520ebea` is NOT the original onboarding commit -- it is the fontc_crater HEAD, dated 2025-02-10, approximately 3 months after the original onboarding on 2024-11-25. The original onboarding commit `17a7ce91` is lost from the upstream repo. The current commit's message ("Merge pull request #35 from theseunbadejo/ghactions-cairofix") suggests it relates to a GitHub Actions CI fix, not a font source change, so the font sources at this commit are likely identical to what was originally onboarded. The METADATA.pb also includes an `archive_url` pointing to a release zip (v1.05), providing an additional reference point.

## Open Questions

1. Were any font source changes made between the original onboarding commit `17a7ce91` (November 2024) and the current METADATA.pb commit `d520ebea` (February 2025)? The "ghactions-cairofix" merge suggests only CI changes, but this should be confirmed.
2. Why was the original onboarding commit `17a7ce91` lost? Was the repo rebased or force-pushed?
3. Does the archive_url release (v1.05) correspond to the onboarded fonts, and could it serve as an alternative verification reference?
