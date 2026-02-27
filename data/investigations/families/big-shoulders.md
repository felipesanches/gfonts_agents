# Investigation: Big Shoulders

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders |
| Slug | big-shoulders |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 8ba99c9e347396d828b263b8b818269cb99eb27c |
| Config YAML | Big-Shoulders/sources/config.yml (in upstream repo) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders/sources/config.yml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders/fonts/variable/BigShoulders[opsz,wght].ttf"
    dest_file: "BigShoulders[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb and matches the copyright string: "Copyright 2019 The Big Shoulders Project Authors (https://github.com/xotypeco/big_shoulders)". All Big Shoulders family variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `8ba99c9e347396d828b263b8b818269cb99eb27c`. The google/fonts commit `7f99323ac` ("Big Shoulders: Version 2.002 added") explicitly states:

> "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c."

This family (the combined opsz+wght variable font) was added to google/fonts on 2025-02-06 (date_added in METADATA.pb). The commit `8ba99c9` is dated 2025-02-06 in the upstream repo, confirming it is the correct onboarding commit.

The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/xotypeco/big_shoulders` and the commit `8ba99c9` exists in the repo.

### Config YAML

The METADATA.pb `config_yaml` field points to `Big-Shoulders/sources/config.yml` in the upstream repo. This file exists at the upstream repository and contains gftools-builder configuration for the Big Shoulders family using `BigShoulders.glyphs` as source. The config builds a variable font with both `opsz` and `wght` axes.

## Conclusion

The source block in METADATA.pb is complete with repository URL, commit hash, and config_yaml path. The config.yml exists in the upstream repo at the specified path. Status is `complete`.
