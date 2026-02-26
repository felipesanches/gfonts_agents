# Bitcount Grid Single

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Petr van Blokland
**METADATA.pb path**: `ofl/bitcountgridsingle/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `af0818eaeb3b0839806ea19134fc18f317cdcf5a` |
| Config YAML | Override in `ofl/bitcountgridsingle/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was set in METADATA.pb from the initial onboarding commit `7f41474fc` (2025-01-17), authored by Yanone. The commit message states: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit af0818eaeb3b0839806ea19134fc18f317cdcf5a." This is part of the Bitcount family project (issue #5468). All 12 Bitcount variants share the same upstream repository.

## How the Commit Hash Was Identified

The onboarding commit `7f41474fc` in google/fonts (2025-01-17) and the corresponding PR #8961 (merged 2025-06-06) both explicitly reference upstream commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` (2025-01-13, "Update fixAnchors.py"). The METADATA.pb still records this original onboarding commit, which is consistent.

The font binary `BitcountGridSingle[CRSV,ELSH,ELXP,slnt,wght].ttf` (226,168 bytes) in google/fonts corresponds to the binary at commit `af0818eae` in the upstream repo. The upstream repo later rebuilt fonts at commit `b43573a4c` (part of PR #37, merged as `89e7994f7`), which changed the Grid Single binary to 226,176 bytes. The binary in google/fonts matches the original `af0818eae` version.

## How Config YAML Was Resolved

The upstream `sources/config.yaml` only contains `familyName: Bitcount` -- it does not reference the designspace file or configure builds for individual variants. A local override config.yaml was created in `ofl/bitcountgridsingle/config.yaml` (added by commit `f6c68379a`, 2026-02-16, "Add override config.yaml for 50 font families"). The override contains:

```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Grid Single
buildVariable: true
buildOTF: false
```

Since there is a local override, no `config_yaml` field is set in the METADATA.pb `source {}` block, which is correct per policy.

## Verification

- Commit `af0818eae` exists in upstream repo: Yes
- Commit date: 2025-01-13 11:46:24 +0100
- Commit message: "Update fixAnchors.py"
- Font binary in google/fonts matches upstream binary at `af0818eae`: Yes (226,168 bytes)
- Designspace file `sources/Bitcount_Template.designspace` exists at commit: Yes
- Override config.yaml present in google/fonts: Yes

## Confidence

**High**: The repository URL and commit hash are consistently referenced across the onboarding commit message, the PR body (#8961), and METADATA.pb. The font binary size in google/fonts (226,168 bytes) matches the upstream binary at `af0818eae`, confirming the correct onboarding commit. The override config.yaml properly references the designspace source file.

## Open Questions

None. The data is fully consistent and verified.
