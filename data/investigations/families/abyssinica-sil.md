# Abyssinica SIL

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: SIL International
**METADATA.pb path**: `ofl/abyssinicasil/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/silnrsi/font-abyssinica |
| Commit | `1f7e65b0e7367681198c980647b3049559ebefa0` |
| Config YAML | override in google/fonts |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field: `https://github.com/silnrsi/font-abyssinica`. The commit message of the font-adding commit in google/fonts (`044faf160453`, "Abyssinica SIL: Version 2.300 added") also explicitly references this URL: "Taken from the upstream repo https://github.com/silnrsi/font-abyssinica at commit ...".

SIL International (silnrsi on GitHub) is the credited designer and maintains this repository as part of their font development infrastructure.

## How the Commit Hash Was Identified

The commit hash `1f7e65b0e7367681198c980647b3049559ebefa0` was pre-existing in the METADATA.pb `source { commit }` field.

This commit is directly corroborated by the google/fonts commit `044faf1604539782d7d35614b98972fb050be910` (dated 2024-10-30), whose body states: "Taken from the upstream repo https://github.com/silnrsi/font-abyssinica at commit https://github.com/silnrsi/font-abyssinica/commit/1f7e65b0e7367681198c980647b3049559ebefa0."

The METADATA.pb also references an archive URL: `https://github.com/silnrsi/font-abyssinica/releases/download/v2.300/AbyssinicaSIL-2.300.zip`, indicating the fonts were taken from a GitHub release rather than built from source.

**Previous versions**: The google/fonts commit history shows this font has been updated multiple times:
- v2.100 via PR #4660
- v2.200 via PR #5622 (gftools-packager)
- v2.300 via direct commit `044faf160`

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repo at the referenced commit. SIL International uses their own build system based on `wscript` (Waf build tool), not gftools-builder.

An override `config.yaml` exists in the google/fonts family directory at `ofl/abyssinicasil/config.yaml`. Its contents:

```yaml
sources:
  - source/AbyssinicaSIL.designspace
familyName: Abyssinica SIL
buildStatic: true
buildOTF: false
```

This override was added in commit `f6c68379a` ("Add override config.yaml for 50 font families"). It references `source/AbyssinicaSIL.designspace`, which is confirmed to exist in the upstream repo at the referenced commit.

The upstream repo's source structure includes:
- `source/AbyssinicaSIL.designspace` (design space file)
- `source/AbyssinicaSIL-Regular.ufo/` (UFO source)
- SIL's custom build scripts (`wscript`, `preflight`, `makedocs`)

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-10-29 15:33:26 -0500
- Commit message: "Update font in references and in test files. [nobuild]"
- Source files at commit: `source/AbyssinicaSIL.designspace`, `source/AbyssinicaSIL-Regular.ufo/` (with many glif files)

## Confidence

**High**: The repository URL is confirmed by METADATA.pb, the google/fonts commit message, and the font copyright. The commit hash is explicitly referenced in both METADATA.pb and the google/fonts commit body for the v2.300 update. The override config.yaml correctly points to an existing `.designspace` file in the upstream repo at the referenced commit. All evidence is consistent and mutually corroborating.

## Open Questions

None. This family is fully documented. The commit hash, repository URL, and config override are all verified and consistent. The font was onboarded using a release archive (v2.300) rather than built from source, but the override config.yaml provides a gftools-builder-compatible build path.
