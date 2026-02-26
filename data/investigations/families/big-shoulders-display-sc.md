# Big Shoulders Display SC

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Patric King
**METADATA.pb path**: `ofl/bigshouldersdisplaysc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `0b3d09a86862b19efae28eae0cd868f17c476b20` |
| Config YAML | (omitted - override config.yaml in google/fonts) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/xotypeco/big_shoulders` was already present in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font files ("Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)"). This URL is shared across all Big Shoulders family variants (Display, Display SC, Inline, Inline Display, Inline Display SC, Inline Text, Stencil Display, Stencil Text, Text, Text SC).

## How the Commit Hash Was Identified

The commit hash `0b3d09a86862b19efae28eae0cd868f17c476b20` was recorded in the METADATA.pb file from the initial onboarding of this family. The onboarding commit in google/fonts (`2035603`) by Simon Cozens states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/0b3d09a86862b19efae28eae0cd868f17c476b20."

This was part of PR #7783, which was merged on 2024-06-25. The upstream commit `0b3d09a` (dated 2024-02-26) has the message "regenerate font files" and was authored by XO Type Co.

Big Shoulders Display SC is a Small Caps variant. The pre-built binary `BigShouldersDisplaySC[wght].ttf` does not exist in the upstream repo at this commit. Instead, it is generated via the override config.yaml recipe in the google/fonts family directory, which builds from `BigShoulders.glyphs` and applies `smcp -> ccmp` layout remapping to produce the SC variant.

## How Config YAML Was Resolved

There is no `config_yaml` field in the METADATA.pb source block because an override `config.yaml` exists in the google/fonts family directory at `ofl/bigshouldersdisplaysc/config.yaml`. This override config defines a recipe that:

1. Builds a variable font from `Big-Shoulders/sources/BigShoulders.glyphs`
2. Subspaces to `opsz=72` (display optical size)
3. Applies `smcp -> ccmp` layout remapping to create the Small Caps variant
4. Renames to "Big Shoulders Display SC"

The override was added by Simon Cozens as part of the original onboarding PR #7783. The upstream repo has no config for this SC variant because it is a derived product.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-02-26
- Commit message: "regenerate font files"
- Commit author: XO Type Co
- Source file at commit: `Big-Shoulders/sources/BigShoulders.glyphs` (exists)
- Pre-built SC binary at commit: Does not exist (expected - SC is generated via recipe)
- Override config.yaml exists in google/fonts: Yes

## Confidence

**High**: The commit hash `0b3d09a` is directly referenced in both the google/fonts onboarding commit and the PR #7783 body. It exists in the upstream repo. The SC variant is generated from sources at this commit via the override config.yaml recipe. The same commit hash is shared with other SC variants (Big Shoulders Text SC, Big Shoulders Inline Display SC) that were onboarded in the same batch by Simon Cozens.

## Open Questions

None. The data is complete and verified.
