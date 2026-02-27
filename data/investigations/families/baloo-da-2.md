# Investigation: Baloo Da 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Da 2 |
| Slug | baloo-da-2 |
| License Dir | ofl |
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit Hash | ffd6308743a5829fe6980ce86f5629ba0250df98 |
| Config YAML | builder/BalooDa2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "ffd6308743a5829fe6980ce86f5629ba0250df98"
  config_yaml: "builder/BalooDa2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooDa2[wght].ttf"
    dest_file: "BalooDa2[wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb already contains a complete source block. The repository URL points to `yanone/Baloo2-Variable`, which is a fork by type engineer Yanone of the canonical EkType upstream repository (`EkType/Baloo2-Variable`).

The latest TTF was added in google/fonts commit `9104fa8b6` (PR #3980, merged 2021-11-25), with commit message:
> "Baloo Da 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98."

This family uses commit `ffd6308`, the same as Baloo Chettan 2 and Baloo Thambi 2. The commit `ffd6308743a5829fe6980ce86f5629ba0250df98` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`. The commit message reads "Update BalooChettan2[wght].ttf" (dated 2021-11-19) — it is the last commit in a series where individual font TTFs were updated after a kerning fix ("Fixed Kerning in Chettan and Thambi, and missing Unicode value in Da"). BalooDa2 was separately updated in the preceding commit (`ad6a1b1` "Update BalooDa2[wght].ttf"), but the gftools-packager used `ffd6308` as the overall HEAD at the time of packaging.

The commit is also present in `EkType/Baloo2-Variable` (same hash), since it was created in yanone's fork and later merged back into EkType.

The config file `builder/BalooDa2.yaml` exists at commit `ffd6308` and contains:
```yaml
sources:
  - ../sources/BalooDa2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Bengali script. The source file `sources/BalooDa2.glyphs` exists in the repository.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified. No action needed.
