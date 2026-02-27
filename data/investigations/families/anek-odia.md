# Investigation: Anek Odia

## Summary

| Field | Value |
|-------|-------|
| Family Name | Anek Odia |
| Slug | anek-odia |
| License Dir | ofl |
| Repository URL | https://github.com/EkType/Anek |
| Commit Hash | 34074c6b406f4112e20c7ad10254a6e954d0324b |
| Config YAML | sources/AnekOdia/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EkType/Anek"
  commit: "34074c6b406f4112e20c7ad10254a6e954d0324b"
  config_yaml: "sources/AnekOdia/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/AnekOdia/variable/AnekOdia[wdth,wght].ttf"
    dest_file: "AnekOdia[wdth,wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb for Anek Odia already contains a complete source block with repository URL, commit hash, and config_yaml path.

The font was added to google/fonts in commit `059d40cac1819d084d21a60e63f2af92631dfa53` on 2022-02-18 via PR #4307, authored by Yanone using gftools-packager. The commit body explicitly references the upstream commit hash `34074c6b406f4112e20c7ad10254a6e954d0324b` from `https://github.com/EkType/Anek`.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/EkType/Anek`. The referenced commit `34074c6b406f4112e20c7ad10254a6e954d0324b` exists in the cache — it is a merge commit dated 2022-02-14 with message "Merge pull request #3 from yanone/main", which predates the google/fonts merge on 2022-02-18. This confirms the commit hash is correct.

The config file `sources/AnekOdia/builder.yaml` exists at the referenced commit in the upstream repo, following the same pattern as the other Anek sub-families.

## Conclusion

The source block in METADATA.pb is complete and accurate. Repository URL, commit hash, and config_yaml path are all verified. No action needed.
