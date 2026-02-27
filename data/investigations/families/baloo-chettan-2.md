# Investigation: Baloo Chettan 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Chettan 2 |
| Slug | baloo-chettan-2 |
| License Dir | ofl |
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit Hash | ffd6308743a5829fe6980ce86f5629ba0250df98 |
| Config YAML | builder/BalooChettan2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "ffd6308743a5829fe6980ce86f5629ba0250df98"
  config_yaml: "builder/BalooChettan2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooChettan2[wght].ttf"
    dest_file: "BalooChettan2[wght].ttf"
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

The latest TTF was added in google/fonts commit `164f84fea` (PR #3985, merged 2021-11-25), with commit message:
> "Baloo Chettan 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98."

This family uses a different commit (`ffd6308`) compared to the majority of the Baloo 2 suite (which uses `da523df`). The commit `ffd6308743a5829fe6980ce86f5629ba0250df98` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`. The commit message reads "Update BalooChettan2[wght].ttf" (dated 2021-11-19), indicating a per-family update that was part of a series fixing kerning issues in Chettan and Thambi.

The commit is also present in `EkType/Baloo2-Variable` (same hash), since it was created in yanone's fork and later merged back into EkType.

The config file `builder/BalooChettan2.yaml` exists at commit `ffd6308` and contains:
```yaml
sources:
  - ../sources/BalooChettan2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Malayalam script. The source file `sources/BalooChettan2.glyphs` exists in the repository.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified. This family uses a slightly later commit than most Baloo 2 variants due to a kerning fix. No action needed.
