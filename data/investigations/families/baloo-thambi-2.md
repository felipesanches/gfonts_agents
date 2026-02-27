# Investigation: Baloo Thambi 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Thambi 2 |
| Slug | baloo-thambi-2 |
| License Dir | ofl |
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit Hash | ffd6308743a5829fe6980ce86f5629ba0250df98 |
| Config YAML | builder/BalooThambi2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "ffd6308743a5829fe6980ce86f5629ba0250df98"
  config_yaml: "builder/BalooThambi2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooThambi2[wght].ttf"
    dest_file: "BalooThambi2[wght].ttf"
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

The latest TTF was added in google/fonts commit `397ea6e1a` (PR #3986, merged 2021-11-25), with commit message:
> "Baloo Thambi 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98."

This family uses commit `ffd6308`, the same as Baloo Chettan 2 and Baloo Da 2. The commit `ffd6308743a5829fe6980ce86f5629ba0250df98` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`. The commit message reads "Update BalooChettan2[wght].ttf" (dated 2021-11-19), and was the HEAD of the yanone fork at the time these three families were packaged. It reflects kerning fixes applied to Chettan and Thambi, with BalooThambi2 updated in the preceding commit `8844491` ("Update BalooThambi2[wght].ttf").

The commit is also present in `EkType/Baloo2-Variable` (same hash), since it was created in yanone's fork and later merged back into EkType.

The config file `builder/BalooThambi2.yaml` exists at commit `ffd6308` and contains:
```yaml
sources:
  - ../sources/BalooThambi2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Tamil script. The source file `sources/BalooThambi2.glyphs` exists in the repository.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified. This family uses a slightly later commit than most Baloo 2 variants due to kerning fixes applied after the initial batch. No action needed.
