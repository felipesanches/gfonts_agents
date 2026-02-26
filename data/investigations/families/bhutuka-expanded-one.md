# Investigation Report: BhuTuka Expanded One

## Source Data

| Field | Value |
|-------|-------|
| Family Name | BhuTuka Expanded One |
| Designer | Erin McLaughlin |
| License | OFL |
| Date Added | 2022-01-21 |
| Repository URL | https://github.com/erinmclaughlin/BhuTuka-Extended-One |
| Commit Hash | `ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6` |
| Branch | master |
| Config YAML | `sources/builder.yaml` |
| Status | **Complete** |

## How URL Found

The repository URL is documented in the copyright field of the font file itself ("Copyright 2017 The BhuTuka Expanded One Project Authors (https://github.com/erinmclaughlin/BhuTuka-Extended-One)") and was explicitly stated in the gftools-packager commit message and PR body.

## How Commit Determined

The commit hash was determined from **PR #4222** in google/fonts, submitted by Yanone (Jens Kutilek). Both the commit message and PR body explicitly state:

> "BhuTuka Expanded One Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/erinmclaughlin/BhuTuka-Extended-One at commit ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6."

**Cross-verification**: The upstream repository has only a single commit (`ac2ad17`), which is a merge of PR #4 from Yanone's fork. This is the HEAD of the master branch, making the commit hash trivially verifiable.

## Config YAML Status

The file `sources/builder.yaml` exists at commit `ac2ad17` in the upstream repository. Its contents:

```yaml
sources:
  - BhuTukaExpandedOne-Regular.glyphs
outputDir: "../fonts"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration targeting the Glyphs source file.

## Verification

- **Commit exists in upstream repo**: Yes (it is the only commit and HEAD of master)
- **Config YAML exists at commit**: Yes (`sources/builder.yaml`)
- **Font file path matches**: The METADATA.pb references `fonts/ttf/BhuTukaExpandedOne-Regular.ttf`, which is the output path from the builder config
- **Source block in METADATA.pb**: Complete with repository_url, commit, config_yaml, files mapping, and branch

## Confidence Level

**High** - All data is fully verified. The gftools-packager commit explicitly referenced this exact commit hash, the upstream repo has only one commit making verification trivial, and the builder configuration is present and valid.

## Open Questions

None. This family is fully documented and verified.
