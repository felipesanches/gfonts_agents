# Big Shoulders Inline

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Patric King
**METADATA.pb path**: `ofl/bigshouldersinline/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit | `8ba99c9e347396d828b263b8b818269cb99eb27c` |
| Config YAML | `Big-Shoulders-Inline/sources/config.yml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/xotypeco/big_shoulders` was already present in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font files ("Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)"). All Big Shoulders variants share this upstream repository.

## How the Commit Hash Was Identified

The commit hash `8ba99c9e347396d828b263b8b818269cb99eb27c` was recorded in the METADATA.pb file. The onboarding commit in google/fonts (`99e4ad649`) by Yanone states: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c."

This was part of PR #9028, which was merged on 2025-02-12. The upstream commit `8ba99c9` (dated 2025-02-06) has the message "Update README.md" and was authored by XO Type Co.

Big Shoulders Inline is a newer addition to the catalog (date_added: 2025-02-06), distinct from the older Big Shoulders Inline Display and Big Shoulders Inline Text families. This is the full optical-size+weight variable font (`BigShouldersInline[opsz,wght].ttf`) with both `opsz` (10-72) and `wght` (100-900) axes.

## How Config YAML Was Resolved

The `config_yaml` field in METADATA.pb is set to `Big-Shoulders-Inline/sources/config.yml`, pointing to the upstream config file. This was added by our own batch commit (`34926685b`, "Add config_yaml to METADATA.pb for 15 font families"). No override config.yaml exists in the google/fonts family directory (`ofl/bigshouldersinline/`).

The upstream `config.yml` at commit `8ba99c9` defines:
- Source: `BigShouldersInline.glyphs`
- Family name: Big Shoulders Inline
- Axis order: opsz, wght
- STAT table configuration for the 2-axis variable font

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2025-02-06
- Commit message: "Update README.md"
- Commit author: XO Type Co
- Font binary at commit: `Big-Shoulders-Inline/fonts/variable/BigShouldersInline[opsz,wght].ttf` exists
- Config file at commit: `Big-Shoulders-Inline/sources/config.yml` exists
- Override config.yaml in google/fonts: No (not needed)

## Confidence

**High**: The commit hash `8ba99c9` is directly referenced in the google/fonts onboarding commit. It is a recent commit (2025-02-06) and the font binary and config file both exist at this commit. The issue resolved (#7830) was specifically for adding the Inline family. PR #9028 by Yanone was a straightforward onboarding.

## Open Questions

None. The data is complete and verified.
