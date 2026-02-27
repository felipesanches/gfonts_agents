# Investigation: Anek Bangla

## Summary

| Field | Value |
|-------|-------|
| Family Name | Anek Bangla |
| Slug | anek-bangla |
| License Dir | ofl |
| Repository URL | https://github.com/EkType/Anek |
| Commit Hash | 34074c6b406f4112e20c7ad10254a6e954d0324b |
| Config YAML | sources/AnekBangla/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EkType/Anek"
  commit: "34074c6b406f4112e20c7ad10254a6e954d0324b"
  config_yaml: "sources/AnekBangla/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/AnekBangla/variable/AnekBangla[wdth,wght].ttf"
    dest_file: "AnekBangla[wdth,wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb for Anek Bangla already contains a complete source block with repository URL, commit hash, and config_yaml path.

The font was added to google/fonts in commit `60d08bb25d216d2394094e3ab5e61f92d354bbd8` on 2022-02-18 via PR #4304, authored by Yanone using gftools-packager. The commit body explicitly references the upstream commit:

> "Anek Bangla Version 1.003 taken from the upstream repo https://github.com/EkType/Anek at commit https://github.com/EkType/Anek/commit/34074c6b406f4112e20c7ad10254a6e954d0324b."

The upstream repository is cached at `upstream_repos/fontc_crater_cache/EkType/Anek`. The referenced commit `34074c6b406f4112e20c7ad10254a6e954d0324b` exists in the cache — it is a merge commit dated 2022-02-14 with message "Merge pull request #3 from yanone/main", which predates the google/fonts merge on 2022-02-18. This confirms the commit hash is correct.

The config file `sources/AnekBangla/builder.yaml` exists at the referenced commit. Its contents:

```yaml
sources:
  - "Masters/AnekBangla.designspace"
outputDir: "../../fonts/AnekBangla"
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
includeSourceFixes: true
```

This is a valid gftools-builder configuration referencing a `.designspace` source file.

## Conclusion

The source block in METADATA.pb is complete and accurate. Repository URL, commit hash, and config_yaml path are all verified. No action needed.
