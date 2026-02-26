# Baloo Da 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/balooda2/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `ffd6308743a5829fe6980ce86f5629ba0250df98` |
| Config YAML | `builder/BalooDa2.yaml` |
| Branch | `master` |

## How the Repository URL Was Found
The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block and confirmed by the gftools-packager commit message in google/fonts PR #3980. The copyright string references the original Ek Type repo `https://github.com/EkType/Baloo2`, but the variable font conversion was done by Yanone in this separate repository.

## How the Commit Hash Was Identified
The commit hash `ffd6308743a5829fe6980ce86f5629ba0250df98` was identified through the following chain of evidence:

1. **Initial submission**: PR #3980 was originally submitted by @yanone with commit `da523dfa21aa0e376253d61c21e39146dc55702a` (Oct 28, 2021).
2. **Review feedback**: @RosaWagner flagged a missing glyph on Oct 29, 2021.
3. **Upstream fix**: Yanone made fixes at upstream commit `7a30396` ("Fixed Kerning in Chettan and Thambi, and missing Unicode value in Da"), then rebuilt BalooDa2 at `ad6a1b1` and BalooChettan2 at `ffd6308`.
4. **PR update**: Yanone pushed the updated fonts to PR #3980 on Nov 19, 2021, referencing commit `ffd6308` (the tip commit that includes the Da 2 fix at `ad6a1b1`).
5. **Merge**: PR was merged by @RosaWagner on Nov 25, 2021, after discussion about transformed components (a known tooling issue at the time, tracked in ufo2ft#507).

The final merged commit in google/fonts (`9104fa8b6299c9de3d70e0a9dbe471cc7d5b5743`) confirms the font was taken from commit `ffd6308`.

## How Config YAML Was Resolved
The config file `builder/BalooDa2.yaml` exists at commit `ffd6308` in the upstream repository. It specifies the source as `../sources/BalooDa2.glyphs` with variable font build only. No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2021-11-19 11:34:42 +0100
- Commit message: "Update BalooChettan2[wght].ttf" (this commit updated Chettan2 binary; Da2 was rebuilt at `ad6a1b1` one commit earlier)
- Source files at commit: `sources/BalooDa2.glyphs`, `builder/BalooDa2.yaml`
- PR #3980 merged by @RosaWagner on 2021-11-25
- google/fonts commit: `9104fa8b6299c9de3d70e0a9dbe471cc7d5b5743`

## Confidence
**High**: The commit hash is verified through the PR update comment and the gftools-packager message. Although `ffd6308` itself only updated BalooChettan2, the Da 2 binary was updated at ancestor commit `ad6a1b1`, and gftools-packager correctly referenced `ffd6308` as the tip commit containing all fixes.

## Open Questions
None
