# Investigation: Aoboshi One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Aoboshi One |
| Slug | aoboshi-one |
| License Dir | ofl |
| Repository URL | https://github.com/matsuba723/Aoboshi |
| Commit Hash | 97f6481745f4184f60e61a9a628e48f7ea5bdcf2 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/matsuba723/Aoboshi"
  commit: "97f6481745f4184f60e61a9a628e48f7ea5bdcf2"
  files {
    source_file: "fonts/ttf/AoboshiOne-Regular.ttf"
    dest_file: "AoboshiOne-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

### Repository

The upstream repository `matsuba723/Aoboshi` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/matsuba723/Aoboshi`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `97f6481745f4184f60e61a9a628e48f7ea5bdcf2` was verified present in the cached repo: `git cat-file -t 97f64817` returns `commit`. The commit is dated 2020-12-16 with message "Rebuilding font for test" by Natsumi Matsuba.

The google/fonts TTF was last updated in commit `cf2da3975` ("Aoboshi One: Version 1.000; ttfautohint (v1.8.3) added (#2918)") on 2021-01-28. The PR body reads: "Aoboshi One Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/matsuba723/Aoboshi.git at commit https://github.com/matsuba723/Aoboshi/commit/97f6481745f4184f60e61a9a628e48f7ea5bdcf2." This exactly matches METADATA.pb.

### Source Files

The `sources/` directory contains:
- `aoboshi.glyphs` — Glyphs format source

No config.yaml exists in the upstream repo. However, an override `config.yaml` was previously created in the google/fonts family directory (`ofl/aoboshione/config.yaml`) with contents:

```yaml
sources:
  - sources/aoboshi.glyphs
```

Per project policy, when an override config.yaml exists in google/fonts, the `config_yaml` field is omitted from METADATA.pb and google-fonts-sources detects the local override automatically.

### Config YAML

An override `config.yaml` exists at `ofl/aoboshione/config.yaml` in google/fonts. No `config_yaml` field is set in METADATA.pb (correct per policy).

## Conclusion

All source metadata is complete. Repository URL and commit hash are present and verified. An override config.yaml exists in google/fonts referencing the Glyphs source. Status is `complete` with HIGH confidence.
