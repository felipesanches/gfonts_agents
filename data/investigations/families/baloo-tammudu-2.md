# Investigation: Baloo Tammudu 2

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baloo Tammudu 2 |
| Slug | baloo-tammudu-2 |
| License Dir | ofl |
| Repository URL | https://github.com/yanone/Baloo2-Variable |
| Commit Hash | da523dfa21aa0e376253d61c21e39146dc55702a |
| Config YAML | builder/BalooTammudu2.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/yanone/Baloo2-Variable"
  commit: "da523dfa21aa0e376253d61c21e39146dc55702a"
  config_yaml: "builder/BalooTammudu2.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BalooTammudu2[wght].ttf"
    dest_file: "BalooTammudu2[wght].ttf"
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

The latest TTF was added in google/fonts commit `ece08a067` (PR #3987, merged 2021-11-25), with commit message:
> "Baloo Tammudu 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/da523dfa21aa0e376253d61c21e39146dc55702a."

Notably, the commit `da523dfa` is actually named "Update BalooTammudu2[wght].ttf" in the yanone repo — it is the commit that specifically updated this family's TTF. This is the most recent commit that touched any file in the Baloo2-Variable repository as of the batch onboarding date.

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` is confirmed present in the local cache at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable`. The commit is also present in `EkType/Baloo2-Variable` (same hash).

The config file `builder/BalooTammudu2.yaml` exists at commit `da523dfa` and contains:
```yaml
sources:
  - ../sources/BalooTammudu2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This family covers the Telugu script. The source file `sources/BalooTammudu2.glyphs` exists in the repository.

## Conclusion

The source block in METADATA.pb is complete and correct. Repository URL, commit hash, and config_yaml are all properly set and verified. The referenced commit (`da523dfa`) is the HEAD commit of the yanone/Baloo2-Variable repository at the time of onboarding and directly corresponds to this family's TTF update. No action needed.
