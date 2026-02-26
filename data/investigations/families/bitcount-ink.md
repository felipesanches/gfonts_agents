# Bitcount Ink

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcountink/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| Config YAML | Override config.yaml in google/fonts family directory |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/petrvanblokland/TYPETR-Bitcount` was present in the METADATA.pb `source { repository_url }` field from the initial onboarding. It matches the copyright string in the font files ("Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)"). The URL was also referenced in issue #5468 (opened by davelab6) and all onboarding PR commit messages.

## How the Commit Hash Was Identified

Bitcount Ink has had two onboarding events in google/fonts:

1. **Version 1.0** (PR #8963, author: Yanone, merged 2025-01-17 via commit `dd01b98`): The gftools-packager message states "Taken from the upstream repo ... at commit af0818eaeb3b0839806ea19134fc18f317cdcf5a". This was the initial onboarding at upstream commit `af0818e`.

2. **Version 1.001** (PR #8963, author: Yanone, merged 2025-09-05 via commit `c020967`): The commit message states "Taken from the upstream repo ... at commit 89e7994f73b7f5ced80e7cf493d40be9e66ff82f". This updated the font to the latest upstream commit.

The METADATA.pb currently records commit `89e7994`, which is the HEAD of the upstream `main` branch. This commit is a merge of PR #37 ("fix-ligatures") in the upstream repo. The commit `af0818e` was the earlier version. Cross-verification confirms that `89e7994` is indeed the correct commit for the currently shipped Version 1.001 font binary.

Note: Between Version 1.0 and Version 1.001, there was also an intermediate "Update with new axes" commit (`f82093f`, author: Simon Cozens, 2025-07-24) that updated the font binary but did not change the METADATA.pb.

## How Config YAML Was Resolved

The upstream repository has a `sources/config.yaml` file, but it is minimal (just `familyName: Bitcount`) and does not contain gftools-builder configuration. The upstream project uses a custom build system (`scripts/build.py` via a Makefile) rather than gftools-builder.

An override `config.yaml` exists in the google/fonts family directory (`ofl/bitcountink/config.yaml`), added by PR #10235 (merged 2026-02-19). This override config specifies:
- Source: `sources/Bitcount_Template.designspace`
- Family name: `Bitcount Ink`
- Build variable: true, OTF: false

Since an override config exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

Note: The fonts in google/fonts were not built with gftools-builder; they were taken as pre-built binaries from the upstream `fonts/ttf/variable/` directory (as indicated by the `files {}` blocks in METADATA.pb referencing `fonts/ttf/variable/BitcountInk[...].ttf`).

## Verification

- Repository URL valid: Yes
- Commit `89e7994` exists in upstream: Yes (HEAD of main branch)
- Commit date: Merge of PR #37 (fix-ligatures)
- Commit `af0818e` also exists (original onboarding commit): Yes
- Source designspace at commit: `sources/Bitcount_Template.designspace` (present at both commits)
- Pre-built font binary at commit: `fonts/ttf/variable/BitcountInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf`
- Override config.yaml in google/fonts: Yes

## Confidence

**High**: The repository URL is confirmed by the copyright string, issue #5468, and all PR commit messages. The commit hash `89e7994` is confirmed by the Version 1.001 update commit message in google/fonts and verified to exist in the upstream repo as HEAD of main. The font family is part of a large Bitcount family (12 variants total from the same upstream repo), all managed consistently.

## Open Questions

None. All source data is well-documented and verified.
