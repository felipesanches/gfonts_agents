# Bitcount Prop Single Ink

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcountpropsingleink/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| Config YAML | `sources/config.yaml` (set in METADATA.pb) |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/petrvanblokland/TYPETR-Bitcount` was present in the METADATA.pb `source { repository_url }` field from the initial onboarding. It matches the copyright string in the font files ("Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)"). The URL was also referenced in issue #5468 and all onboarding PR commit messages.

## How the Commit Hash Was Identified

Bitcount Prop Single Ink has the most complex history among the five families investigated here:

1. **Version 1.0** (PR #8967, author: Yanone, merged 2025-01-23 via commit `bc28f2f`): The gftools-packager message states "Taken from the upstream repo ... at commit af0818eaeb3b0839806ea19134fc18f317cdcf5a".

2. **Source block ported** (commit `19cdcec`, author: Felipe Sanches, 2025-03-31): The "[Batch 1/4] port info from fontc_crater targets list" commit added source metadata including `config_yaml: "sources/config.yaml"` to the METADATA.pb.

3. **Bitcount 1.001 rebuild** (commit `9205630`, author: Simon Cozens, 2025-06-16): Binary rebuild for Bitcount Single Ink and Prop Single Ink.

4. **Name table fix rebuild** (commit `566bead`, author: Simon Cozens, 2025-06-19): Another rebuild to fix name table version.

5. **Position axes fix** (commit `a8916f4`, author: Simon Cozens, 2025-06-19): Yet another rebuild (message: "And again").

6. **Article update** (commit `7580126`, author: Emma Marichal, 2025-07-11): Added article images.

7. **Axis range correction** (commit `18bc295`, author: Garret Rieger, 2025-07-14): Corrected XPN*/YPN* axis ranges in METADATA.pb to match the font.

8. **Version 1.001/1.002 update** (PR #9821, author: Emma Marichal, merged 2025-09-11 via commit `529068a`): The commit message states "Taken from the upstream repo ... at commit 89e7994f73b7f5ced80e7cf493d40be9e66ff82f". Updated the METADATA.pb to reference the latest upstream commit.

9. **Article completion** (commit `981e34f`, author: Emma Marichal, 2025-09-11): Completed article with COLRv1 font content.

The METADATA.pb currently records commit `89e7994`, which is the HEAD of the upstream `main` branch. Cross-verification confirms that `89e7994` is the correct commit for the currently shipped font binary.

## How Config YAML Was Resolved

The METADATA.pb has `config_yaml: "sources/config.yaml"` set in the source block. This was ported from the fontc_crater targets list in the "[Batch 1/4]" commit.

However, the upstream `sources/config.yaml` is minimal (just `familyName: Bitcount`) and does not contain full gftools-builder configuration. The upstream project uses a custom build system (`scripts/build.py` via a Makefile) rather than gftools-builder.

Unlike the other four Bitcount families investigated here, Bitcount Prop Single Ink does **not** have an override `config.yaml` in the google/fonts family directory. This is an inconsistency -- the other four families (Bitcount Ink, Bitcount Prop Double, Bitcount Prop Double Ink, Bitcount Prop Single) all have override configs added by PR #10235.

The fonts in google/fonts were not built with gftools-builder; they were taken as pre-built binaries from the upstream `fonts/ttf/variable/` directory (as indicated by the `files {}` blocks in METADATA.pb referencing `fonts/ttf/variable/BitcountPropSingleInk[...].ttf`).

## Verification

- Repository URL valid: Yes
- Commit `89e7994` exists in upstream: Yes (HEAD of main branch)
- Commit `af0818e` also exists (original onboarding commit): Yes
- Source designspace at commit: `sources/Bitcount_Template.designspace` (present at both commits)
- Pre-built font binary at commit: `fonts/ttf/variable/BitcountPropSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf`
- Upstream `sources/config.yaml`: Present but minimal (only `familyName: Bitcount`)
- Override config.yaml in google/fonts: **No** (inconsistent with other Bitcount families)

## Confidence

**High**: The repository URL is confirmed by the copyright string, issue #5468, and all PR commit messages. The commit hash `89e7994` is confirmed by the Version 1.001/1.002 update commit message (PR #9821) and verified to exist in the upstream repo as HEAD of main. This family is part of a large Bitcount family (12 variants total from the same upstream repo).

## Open Questions

1. Bitcount Prop Single Ink lacks an override `config.yaml` in the google/fonts family directory, unlike the other four Bitcount families investigated here (Bitcount Ink, Bitcount Prop Double, Bitcount Prop Double Ink, Bitcount Prop Single). It instead points to the upstream `sources/config.yaml` which only contains `familyName: Bitcount`. This may need to be corrected for consistency -- either by adding an override config or by removing the `config_yaml` field from METADATA.pb and adding an override config similar to the other families.
