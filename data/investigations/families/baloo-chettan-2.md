# Baloo Chettan 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/baloochettan2/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `ffd6308743a5829fe6980ce86f5629ba0250df98` |
| Config YAML | `builder/BalooChettan2.yaml` |
| Branch | `master` |

## How the Repository URL Was Found
The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block and confirmed by the gftools-packager commit message in google/fonts PR #3985. The copyright string in METADATA.pb references `https://github.com/EkType/Baloo2`, which is the original Ek Type repository, but the variable font conversion was done by Yanone in this separate repository.

## How the Commit Hash Was Identified
The commit hash `ffd6308743a5829fe6980ce86f5629ba0250df98` was identified through the following chain of evidence:

1. **Initial submission**: PR #3985 was originally submitted by @yanone with commit `da523dfa21aa0e376253d61c21e39146dc55702a` (Oct 28, 2021).
2. **Review feedback**: @RosaWagner flagged a kerning regression on Nov 3, 2021.
3. **Upstream fix**: Yanone fixed kerning in Chettan and Thambi at upstream commit `7a30396`, then rebuilt the font binary at commit `ffd6308` (Nov 19, 2021).
4. **PR update**: Yanone pushed the updated fonts to PR #3985 on Nov 19, 2021, referencing the new commit `ffd6308`.
5. **Merge**: PR was merged by @RosaWagner on Nov 25, 2021.

The final merged commit in google/fonts (`164f84fea7f2a61dc501b32686e60cca9d029e08`) confirms the font was taken from commit `ffd6308`.

## How Config YAML Was Resolved
The config file `builder/BalooChettan2.yaml` exists at commit `ffd6308` in the upstream repository. It specifies the source as `../sources/BalooChettan2.glyphs` with variable font build only. No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2021-11-19 11:34:42 +0100
- Commit message: "Update BalooChettan2[wght].ttf"
- Source files at commit: `sources/BalooChettan2.glyphs`, `builder/BalooChettan2.yaml`
- PR #3985 merged by @RosaWagner on 2021-11-25
- google/fonts commit: `164f84fea7f2a61dc501b32686e60cca9d029e08`

## Confidence
**High**: The commit hash is fully verified through multiple independent sources: gftools-packager message, PR discussion showing the update from the original commit to the fixed one, and the upstream repo history confirming the kerning fix.

## Open Questions
None
