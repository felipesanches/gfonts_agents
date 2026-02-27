# Investigation: Baloo Bhaina 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Bhaina 2 |
| Slug | baloo-bhaina-2 |
| License Dir | ofl |
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit Hash | da523dfa21aa0e376253d61c21e39146dc55702a |
| Config YAML | builder/BalooBhaina2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "da523dfa21aa0e376253d61c21e39146dc55702a"
  config_yaml: "builder/BalooBhaina2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooBhaina2[wght].ttf"
    dest_file: "BalooBhaina2[wght].ttf"
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

The latest TTF was added in google/fonts commit `35975c1b3` (PR #3988, merged 2021-11-25), with commit message:
> "Baloo Bhaina 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/da523dfa21aa0e376253d61c21e39146dc55702a."

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`. The commit (dated 2021-10-28) updated multiple variable fonts in the Baloo 2 suite simultaneously.

The commit is also present in `EkType/Baloo2-Variable` (same hash), since it was created in yanone's fork and merged back into EkType.

The config file `builder/BalooBhaina2.yaml` exists at commit `da523dfa` and contains:
```yaml
sources:
  - ../sources/BalooBhaina2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Odia (Oriya) script. The source file `sources/BalooBhaina2.glyphs` exists in the repository.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified against the gftools-packager commit message and the cached upstream repository. No action needed.
