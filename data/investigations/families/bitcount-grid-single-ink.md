# Bitcount Grid Single Ink

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcountgridsingleink/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| Config YAML | Override in `ofl/bitcountgridsingleink/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in METADATA.pb, set during the Version 1.001 onboarding. The URL matches the copyright string and is consistent with all other Bitcount variants sharing the same upstream repository (issue #5468).

## How the Commit Hash Was Identified

Bitcount Grid Single Ink has a two-stage onboarding history similar to the other Ink variants:

1. **Initial attempt (v1.0)**: Yanone created the initial onboarding commit `f25802b3e` (2025-01-17), referencing upstream commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a`. This was part of the batch of 12 Bitcount PRs. However, the Ink variants were noted as "not working" in issue #5468.

2. **Successful onboarding (v1.001)**: Emma Marichal re-added the font via commit `3f08adabc` (2025-09-05), corresponding to PR #8962 (merged 2025-09-05). This commit references a newer upstream commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` (2025-09-05, "Merge pull request #37 from petrvanblokland/fix-ligatures"). The v1.001 METADATA.pb was created fresh.

The upstream commit `89e7994f7` is the HEAD of the main branch. Between `af0818eae` and `89e7994f7`, the upstream repo had significant work: version bumps, ligature fixes (PR #37), position axis rework (PR #35), and font rebuilds. The font binary `BitcountGridSingleInk[...].ttf` changed from 276,408 bytes (at `af0818eae`) to 276,416 bytes (at `89e7994f7`), confirming fonts were rebuilt.

## How Config YAML Was Resolved

The upstream `sources/config.yaml` only contains `familyName: Bitcount` and does not configure individual variant builds. A local override config.yaml was created in `ofl/bitcountgridsingleink/config.yaml` (commit `f6c68379a`, 2026-02-16):

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single Ink
buildVariable: true
buildOTF: false
```

Since there is a local override, no `config_yaml` field is set in the METADATA.pb `source {}` block.

## Verification

- Commit `89e7994f7` exists in upstream repo: Yes
- Commit date: 2025-09-05 10:53:08 +0100
- Commit message: "Merge pull request #37 from petrvanblokland/fix-ligatures"
- Font binary corresponds to rebuilt fonts at this commit: Yes (276,416 bytes)
- Designspace file `sources/Bitcount_Template.designspace` exists at commit: Yes
- Override config.yaml present in google/fonts: Yes

## Confidence

**High**: The Ink variants had a failed initial onboarding (v1.0 at `af0818eae`) and were successfully re-onboarded at v1.001 from commit `89e7994f7`. The commit message in google/fonts explicitly references this upstream commit, and the font binary sizes match. The override config.yaml properly references the designspace source file.

## Open Questions

None. The data is fully consistent and verified. The two-stage onboarding (failed v1.0, successful v1.001) is well-documented in issue #5468 and the commit history.
