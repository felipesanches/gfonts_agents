# Baloo Tamma 2

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Ek Type
**METADATA.pb path**: `ofl/balootamma2/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit | `da523dfa21aa0e376253d61c21e39146dc55702a` |
| Config YAML | `builder/BalooTamma2.yaml` |
| Branch | `master` |

## How the Repository URL Was Found
The repository URL `https://github.com/yanone/Baloo2-Variable` is documented in the METADATA.pb `source` block and confirmed by the gftools-packager commit message in google/fonts PR #3984. The copyright string references the original Ek Type repo `https://github.com/EkType/Baloo2`, but the variable font conversion was done by Yanone in this separate repository.

## How the Commit Hash Was Identified
The commit hash `da523dfa21aa0e376253d61c21e39146dc55702a` was identified through the following evidence:

1. **Submission**: PR #3984 was submitted by @yanone with commit `da523dfa21aa0e376253d61c21e39146dc55702a` (Oct 28, 2021).
2. **No review issues**: The only comment on the PR was the fontbakery bot report. No regressions were flagged.
3. **Same-day merge**: PR was merged by @RosaWagner on Oct 29, 2021 (just 1 day after submission).
4. **No upstream updates**: This family did not have the kerning/glyph issues that affected Chettan 2 and Da 2, so the original commit was used as-is.

The final merged commit in google/fonts (`48be53e8ff974858f33a01c86ded83dba2fd710f`) confirms the font was taken from commit `da523df`.

## How Config YAML Was Resolved
The config file `builder/BalooTamma2.yaml` exists at commit `da523df` in the upstream repository. It specifies the source as `../sources/BalooTamma2.glyphs` with variable font build only. No override config.yaml exists in the google/fonts family directory.

## Verification
- Commit exists in upstream repo: Yes
- Commit date: 2021-10-28 17:08:59 +0200
- Commit message: "Update BalooTammudu2[wght].ttf" (this commit updated Tammudu2 binary; Tamma2 was rebuilt at ancestor `f98386c`)
- Source files at commit: `sources/BalooTamma2.glyphs`, `builder/BalooTamma2.yaml`
- PR #3984 merged by @RosaWagner on 2021-10-29
- google/fonts commit: `48be53e8ff974858f33a01c86ded83dba2fd710f`

## Confidence
**High**: The commit hash is consistent across all sources: METADATA.pb, gftools-packager message in the PR body, and the google/fonts merge commit. No updates were made to the PR, confirming the original commit was the one used.

## Open Questions
None
