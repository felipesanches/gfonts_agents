# Investigation: Baloo Bhaijaan 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Bhaijaan 2 |
| Slug | baloo-bhaijaan-2 |
| License Dir | ofl |
| Repository URL | https://github.com/EkType/Baloo2-Variable |
| Commit Hash | da4090c1dd5798a3e72d7138e379ee1f94d6349c |
| Config YAML | builder/BalooBhaijaan2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EkType/Baloo2-Variable"
  commit: "da4090c1dd5798a3e72d7138e379ee1f94d6349c"
  config_yaml: "builder/BalooBhaijaan2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooBhaijaan2[wght].ttf"
    dest_file: "BalooBhaijaan2[wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb contains a complete source block. Unlike the other 9 Baloo 2 variants, this family's source block points to the canonical `EkType/Baloo2-Variable` repository (rather than `yanone/Baloo2-Variable`), and references a later commit.

**Two-stage update history:**

1. **First onboarding** — google/fonts commit `a6eb370bf` (PR #3979, 2021-11-25): Version 1.700 added from `yanone/Baloo2-Variable` at commit `da523dfa`. At this point there was no source block in METADATA.pb.

2. **Updated to v1.701** — google/fonts commit `d3d979f3d` (PR #5216, 2022-09-13): Version 1.701 added by Yanone himself from `EkType/Baloo2-Variable` at commit `da4090c1dd5798a3e72d7138e379ee1f94d6349c`. This update added the source block to METADATA.pb for the first time and switched the repository reference to the canonical EkType upstream.

The commit `da4090c1` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/EkType/Baloo2-Variable`. The commit message reads "Merge pull request #5 from yanone/master" (dated 2022-09-09), and is a merge commit of Yanone's regenerated 1.701 fonts into the canonical EkType repository.

The config file `builder/BalooBhaijaan2.yaml` exists at commit `da4090c1` and contains:
```yaml
sources:
  - ../sources/BalooBhaijaan2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Arabic script. The source file `sources/BalooBhaijaan2.glyphs` exists in the repository.

This family stands out as the only one of the 10 Baloo 2 variants where the source block references the canonical `EkType/Baloo2-Variable` repo. The others still reference `yanone/Baloo2-Variable` (the fork). Since `da523dfa` is present in the EkType repo too, all families could in principle be updated to use the canonical EkType URL — but that is outside the scope of this investigation.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified. This family was updated to v1.701 in PR #5216 and now correctly references the canonical EkType repository. No action needed.
