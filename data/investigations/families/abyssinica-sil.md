# Investigation: Abyssinica SIL

## Summary

| Field | Value |
|-------|-------|
| Family Name | Abyssinica SIL |
| Slug | abyssinica-sil |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-abyssinica |
| Commit Hash | 1f7e65b0e7367681198c980647b3049559ebefa0 |
| Config YAML | override in google/fonts (ofl/abyssinicasil/config.yaml) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-abyssinica"
  commit: "1f7e65b0e7367681198c980647b3049559ebefa0"
  archive_url: "https://github.com/silnrsi/font-abyssinica/releases/download/v2.300/AbyssinicaSIL-2.300.zip"
  files {
    source_file: "AbyssinicaSIL-2.300/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "AbyssinicaSIL-2.300/AbyssinicaSIL-Regular.ttf"
    dest_file: "AbyssinicaSIL-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

### Git History

The TTF files in `ofl/abyssinicasil/` have multiple commits showing version updates:

```
044faf160 Abyssinica SIL: Version 2.300 added
a87161b4e [gftools-packager] Abyssinica SIL: Version 2.200 added (#5622)
80ffd33a4 Abyssinica SIL: Version 2.100 added (#4660)
6d3047828 ofl/abyssinicasil Updated to v1.500g
3a3c6693d Add Abyssinica SIL
```

The most recent commit is `044faf160` (dated 2024-10-30), with body:

> Abyssinica SIL: Version 2.300 added
>
> Taken from the upstream repo https://github.com/silnrsi/font-abyssinica at commit https://github.com/silnrsi/font-abyssinica/commit/1f7e65b0e7367681198c980647b3049559ebefa0.

### Commit Verification

The commit `1f7e65b0e7367681198c980647b3049559ebefa0` exists in the upstream repo (cloned at `upstream_repos/fontc_crater_cache/silnrsi/font-abyssinica/`) with:
- Date: 2024-10-29 15:33:26 -0500
- Message: "Update font in references and in test files. [nobuild]"

This commit is directly confirmed by the google/fonts commit body for `044faf160`. The commit date (2024-10-29) is one day before the google/fonts onboarding commit (2024-10-30), consistent with a timely packaging workflow.

### Upstream Repository Structure

The upstream repo uses SIL International's `wscript` (Waf build tool), not gftools-builder. The source directory contains:
- `source/AbyssinicaSIL.designspace`
- `source/AbyssinicaSIL-Regular.ufo/`
- SIL custom build scripts (`wscript`, `preflight`, `makedocs`)

Note: The METADATA.pb uses `archive_url` pointing to a GitHub release (v2.300 zip), indicating the fonts were taken from a pre-built release rather than compiled by gftools-packager from source.

### Override Config.yaml

An override `config.yaml` exists in the google/fonts family directory at `ofl/abyssinicasil/config.yaml`:

```yaml
sources:
  - source/AbyssinicaSIL.designspace
familyName: Abyssinica SIL
buildStatic: true
buildOTF: false
```

This override was added in google/fonts commit `f6c68379a` ("Add override config.yaml for 50 font families"). It references `source/AbyssinicaSIL.designspace`, which is confirmed to exist in the upstream repo at the referenced commit. Since the METADATA.pb has no `config_yaml` field, the local override is auto-detected by google-fonts-sources.

## Conclusion

No action needed. The METADATA.pb `source {}` block is complete: repository URL, commit hash, branch, and archive_url are all set and verified. An override `config.yaml` in `ofl/abyssinicasil/` provides gftools-builder compatibility. All data is consistent and corroborated by the google/fonts commit message. This family is fully documented.
