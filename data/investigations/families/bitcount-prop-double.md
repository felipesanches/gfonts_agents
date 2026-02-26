# Bitcount Prop Double

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcountpropdouble/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `af0818eaeb3b0839806ea19134fc18f317cdcf5a` |
| Config YAML | Override config.yaml in google/fonts family directory |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/petrvanblokland/TYPETR-Bitcount` was present in the METADATA.pb `source { repository_url }` field from the initial onboarding. It matches the copyright string in the font files ("Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)"). The URL was also referenced in issue #5468 and the onboarding PR #8964 commit message.

## How the Commit Hash Was Identified

Bitcount Prop Double was onboarded in a single event:

1. **Version 1.0** (PR #8964, author: Yanone, merged 2025-06-06 via commit `b5b5577`): The gftools-packager message states "Taken from the upstream repo ... at commit af0818eaeb3b0839806ea19134fc18f317cdcf5a". All initial Bitcount family PRs (resolving issue #5468) reference the same upstream commit `af0818e`.

The METADATA.pb records commit `af0818e`. Unlike the "Ink" variants of the Bitcount family, Bitcount Prop Double has not been updated to a newer upstream commit. The upstream has since progressed to `89e7994` (HEAD), which includes ligature fixes and version bumps. However, the currently shipped binary was taken from `af0818e`.

Cross-verification: The commit `af0818e` exists in the upstream repo with message "Update fixAnchors.py".

## How Config YAML Was Resolved

The upstream repository has a `sources/config.yaml` file, but it is minimal (just `familyName: Bitcount`) and does not contain gftools-builder configuration. The upstream project uses a custom build system (`scripts/build.py` via a Makefile) rather than gftools-builder.

An override `config.yaml` exists in the google/fonts family directory (`ofl/bitcountpropdouble/config.yaml`), added by PR #10235 (merged 2026-02-19). This override config specifies:
- Source: `sources/Bitcount_Template.designspace`
- Family name: `Bitcount Prop Double`
- Build variable: true, OTF: false

Since an override config exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

Note: The fonts in google/fonts were not built with gftools-builder; they were taken as pre-built binaries from the upstream `fonts/ttf/variable/` directory (as indicated by the `files {}` blocks in METADATA.pb referencing `fonts/ttf/variable/BitcountPropDouble[...].ttf`).

## Verification

- Repository URL valid: Yes
- Commit `af0818e` exists in upstream: Yes
- Commit message: "Update fixAnchors.py"
- Source designspace at commit: `sources/Bitcount_Template.designspace` (present)
- Pre-built font binary at commit: `fonts/ttf/variable/BitcountPropDouble[CRSV,ELSH,ELXP,slnt,wght].ttf`
- Override config.yaml in google/fonts: Yes

## Confidence

**High**: The repository URL is confirmed by the copyright string, issue #5468, and the onboarding PR commit message. The commit hash `af0818e` is confirmed by the gftools-packager message in PR #8964 and verified to exist in the upstream repo. This family is part of a large Bitcount family (12 variants total from the same upstream repo).

## Open Questions

1. The upstream repo has progressed from `af0818e` to `89e7994` (17 commits, including ligature fixes and version bumps). The "Ink" variants were updated to the newer commit, but Bitcount Prop Double was not. It may benefit from being updated to the latest upstream commit to incorporate the ligature fixes.
