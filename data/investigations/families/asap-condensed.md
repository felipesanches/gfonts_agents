# Investigation: Asap Condensed

## Summary

| Field | Value |
|-------|-------|
| Family Name | Asap Condensed |
| Slug | asap-condensed |
| License Dir | ofl |
| Repository URL | https://github.com/Omnibus-Type/Asap |
| Commit Hash | 927ab390d4ece9eaa70a3b16a6124baa9192e34c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Omnibus-Type/Asap"
  commit: "927ab390d4ece9eaa70a3b16a6124baa9192e34c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/AsapCondensed-Black.ttf"
    dest_file: "AsapCondensed-Black.ttf"
  }
  [... additional file mappings ...]
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Asap Condensed was most recently updated via PR #5492, with the gftools-packager commit `b1254ac0b` (2022-11-04, "Asap Condensed: Version 3.001; ttfautohint (v1.8.4.7-5d5b) added") by Rosalie Wagner. The commit body explicitly states: "Asap Condensed Version 3.001; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Omnibus-Type/Asap at commit https://github.com/Omnibus-Type/Asap/commit/927ab390d4ece9eaa70a3b16a6124baa9192e34c."

The upstream repository `Omnibus-Type/Asap` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/Omnibus-Type/Asap`. Commit `927ab390` is confirmed present (dated 2022-10-13 17:17:42 +0200, "Font exported").

The `sources/config.yaml` file exists in the upstream repository and specifies:
- Sources: `Asap.glyphs` and `Asap-Italic.glyphs`
- Axis order: wdth, wght
- Comprehensive STAT table configuration for all widths and weights

Note: This is the shared upstream repository for both Asap and Asap Condensed. The config.yaml is designed for the full Asap family with all width variants (Condensed through Expanded). The METADATA.pb config_yaml field correctly points to `sources/config.yaml` in the Omnibus-Type/Asap repository.

The font directory was first added in 2016 (date_added: "2016-12-07") and has been updated multiple times since then.

## Conclusion

Status is complete. All required fields (repository_url, commit, config_yaml) are present and verified in METADATA.pb. The commit matches the gftools-packager onboarding reference. No further action needed.
