# Big Shoulders Inline Display SC

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Patric King
**METADATA.pb path**: `ofl/bigshouldersinlinedisplaysc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `0b3d09a86862b19efae28eae0cd868f17c476b20` |
| Config YAML | (omitted - override config.yaml in google/fonts) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/xotypeco/big_shoulders` was already present in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font files. All Big Shoulders variants share this upstream repository.

## How the Commit Hash Was Identified

The commit hash `0b3d09a86862b19efae28eae0cd868f17c476b20` was recorded in the METADATA.pb file from the initial onboarding. The onboarding commit in google/fonts (`ab4f392c8`) by Simon Cozens states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/0b3d09a86862b19efae28eae0cd868f17c476b20."

This was part of PR #7786, which was merged on 2024-06-25 (same day as the Display SC PR #7783). The upstream commit `0b3d09a` (dated 2024-02-26) has the message "regenerate font files" and was authored by XO Type Co.

Big Shoulders Inline Display SC is a Small Caps variant derived from the Inline source. The SC binary does not exist as a pre-built file in the upstream repo. Instead, it is generated via the override config.yaml recipe which applies `smcp -> ccmp` layout remapping to the Inline Display build.

This commit hash (`0b3d09a`) is shared with other SC variants onboarded by Simon Cozens in the same batch (Big Shoulders Display SC via PR #7783).

## How Config YAML Was Resolved

An override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersinlinedisplaysc/config.yaml`. Therefore, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

The override config defines a recipe that:
1. Builds from `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`
2. Subspaces to `opsz=72` (display optical size)
3. Builds both the regular Inline Display variant and the SC variant
4. For the SC variant: applies `smcp -> ccmp` layout remapping, then renames to "Big Shoulders Inline Display SC"

The config was added by Simon Cozens as part of PR #7786. The same PR also added the parent config.yaml for `bigshouldersinlinedisplay` (commit `478e94ec1`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-02-26
- Commit message: "regenerate font files"
- Commit author: XO Type Co
- Source file at commit: `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs` (exists)
- Pre-built SC binary at commit: Does not exist (expected - SC is generated via recipe)
- Override config.yaml in google/fonts: Yes

## Confidence

**High**: The commit hash `0b3d09a` is directly referenced in both the google/fonts onboarding commit and the PR #7786 body. It exists in the upstream repo. The SC variant is correctly generated from sources at this commit via the override config.yaml recipe.

## Open Questions

None. The data is complete and verified.
