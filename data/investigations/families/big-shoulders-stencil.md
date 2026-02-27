# Investigation: Big Shoulders Stencil

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Stencil |
| Slug | big-shoulders-stencil |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 8ba99c9e347396d828b263b8b818269cb99eb27c |
| Config YAML | Big-Shoulders-Stencil/sources/config.yml (in upstream repo) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders-Stencil/sources/config.yml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf"
    dest_file: "BigShouldersStencil[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb and confirmed by the copyright string. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `8ba99c9e347396d828b263b8b818269cb99eb27c`. The google/fonts commit `3b113037a` ("Big Shoulders Stencil: Version 2.001 added") explicitly states:

> "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c."

This family was added on 2025-02-06 (date_added). The commit `8ba99c9` is dated 2025-02-06 in the upstream repo, confirming it is the correct onboarding commit. The commit exists in the upstream repo cache.

### Config YAML

The METADATA.pb `config_yaml` field points to `Big-Shoulders-Stencil/sources/config.yml` in the upstream repo. This file exists at `/mnt/shared/upstream_repos/fontc_crater_cache/xotypeco/big_shoulders/Big-Shoulders-Stencil/sources/config.yml` and configures the build from `BigShouldersStencil.glyphs` with both `opsz` and `wght` axes.

## Conclusion

The source block in METADATA.pb is complete with repository URL, commit hash, and config_yaml path. The config.yml exists in the upstream repo at the specified path. Status is `complete`.
