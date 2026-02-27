# Investigation: Abhaya Libre

## Summary

| Field | Value |
|-------|-------|
| Family Name | Abhaya Libre |
| Slug | abhaya-libre |
| License Dir | ofl |
| Repository URL | https://github.com/mooniak/abhaya-libre-font |
| Commit Hash | f53da70786fe1dba6193bdbd45a2c4159e511079 |
| Config YAML | override in google/fonts (ofl/abhayalibre/config.yaml) |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/mooniak/abhaya-libre-font"
  commit: "f53da70786fe1dba6193bdbd45a2c4159e511079"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History

The TTF files in `ofl/abhayalibre/` have the following commit history in google/fonts:

```
f8dbc7690 abhayalibre: v1.050 added. (#665)
7a4070f65 Update Abhaya Libre to v1.041
2076d77e0 ofl/abhayalibre Updated to v1.030
9552ec151 Add Abhaya Libre (Sinhala + Latin)
```

The most recent font-modifying commit is `f8dbc7690` (dated 2017-02-17), which is PR #665 ("abhayalibre: v1.050 added. Fixes #460."). This PR was submitted by `m4rc1e`.

### Commit Hash Analysis

The commit `f53da70786fe1dba6193bdbd45a2c4159e511079` currently in METADATA.pb is **not** the original onboarding commit. It is the HEAD of the upstream repo as of 2024-05-31, with message "Update to GF repo tempalte and CI". This commit is from 7 years after the last font was onboarded via PR #665 in 2017.

This commit was likely chosen when the source block was retroactively added to METADATA.pb (via google/fonts commits `04009b5bb` and `5862ed413`, "sources info for Abhaya Libre"), as it is the repo HEAD and contains the `sources/config.yaml` referenced in `config_yaml`. However, the fonts currently in google/fonts correspond to the v1.050 state from 2017, not the 2024 repo HEAD.

### Upstream Repository

The repo is cloned at `upstream_repos/fontc_crater_cache/mooniak/abhaya-libre-font/`. The sources directory contains:
- `AbhayaLibre.glyphs` (at HEAD `f53da70`)

### Override Config.yaml

An override `config.yaml` exists in the google/fonts family directory at `ofl/abhayalibre/config.yaml`:

```yaml
sources:
  - sources/glyphs/Abhaya-Masters.glyphs
buildStatic: true
buildVariable: false
```

This override references `sources/glyphs/Abhaya-Masters.glyphs`, which matches the file structure at the time of the original v1.050 onboarding (~2017). The upstream repo's source file was later reorganized to `sources/AbhayaLibre.glyphs`. Since a local override exists, the `config_yaml` field in METADATA.pb pointing to the upstream's `sources/config.yaml` is redundant but not harmful.

### Key Concern

The `commit` field in METADATA.pb points to the 2024 repo HEAD (`f53da70`), not the original onboarding commit from circa 2017. The correct commit would be the HEAD of the upstream repo at the time PR #665 was merged (2017-02-17). However, since the upstream repo shows no git history predating `f53da70` as the earliest cached commit, and the repo may have been rewritten, identifying the exact original commit is difficult without additional research.

## Conclusion

The METADATA.pb `commit` field points to a 2024 repo HEAD, not the actual commit used for the 2017 onboarding. This is a `missing_commit` situation (the recorded commit is present but wrong). The `config_yaml` field pointing to the upstream `sources/config.yaml` is also inconsistent with the override config.yaml in google/fonts, which references the older source path `sources/glyphs/Abhaya-Masters.glyphs`. The `config_yaml` field in METADATA.pb should be removed (since the local override is auto-detected and it references an incompatible source path). A follow-up question to the Mooniak team or Google Fonts engineers would be needed to identify the correct original commit.
