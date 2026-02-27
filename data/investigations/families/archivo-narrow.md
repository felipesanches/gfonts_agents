# Investigation: Archivo Narrow

## Summary

| Field | Value |
|-------|-------|
| Family Name | Archivo Narrow |
| Slug | archivo-narrow |
| License Dir | ofl |
| Repository URL | https://github.com/Omnibus-Type/ArchivoNarrow |
| Commit Hash | 9793ec77b6682a26bc7a6ed523ca65cc3cb90aec |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Omnibus-Type/ArchivoNarrow"
  commit: "9793ec77b6682a26bc7a6ed523ca65cc3cb90aec"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/ArchivoNarrow[wght].ttf"
    dest_file: "ArchivoNarrow[wght].ttf"
  }
  files {
    source_file: "fonts/variable/ArchivoNarrow-Italic[wght].ttf"
    dest_file: "ArchivoNarrow-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Repository

The upstream repository `Omnibus-Type/ArchivoNarrow` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/Omnibus-Type/ArchivoNarrow`. The repository URL, commit hash, and config_yaml are all pre-existing in METADATA.pb.

### Commit Hash

The commit `9793ec77b6682a26bc7a6ed523ca65cc3cb90aec` was verified present in the cached repo: `git cat-file -t 9793ec77` returns `commit`. The commit is dated 2022-11-11 with message "Font exported" (confirmed via checking the ArchivoNarrow repo log).

The google/fonts TTFs were last updated in commit `58d049625` ("[gftools-packager] Archivo Narrow: Version 3.002 added (#5559)") on 2022-11-18. The PR body reads: "Archivo Narrow Version 3.002 taken from the upstream repo https://github.com/Omnibus-Type/ArchivoNarrow at commit https://github.com/Omnibus-Type/ArchivoNarrow/commit/9793ec77b6682a26bc7a6ed523ca65cc3cb90aec." This exactly matches METADATA.pb.

### Source Files

The `sources/` directory contains:
- `ArchivoNarrow.glyphs` — Glyphs format source
- `ArchivoNarrow-Italic.glyphs` — Glyphs format source
- `config.yaml` — gftools-builder configuration

The config.yaml at `sources/config.yaml` contains:

```yaml
sources:
  - ArchivoNarrow.glyphs
  - ArchivoNarrow-Italic.glyphs
axisOrder:
  - wght
familyName: "Archivo Narrow"
stat:
    ArchivoNarrow[wght].ttf:
    - name: Weight
      tag: wght
      ...
```

### Config YAML

`sources/config.yaml` exists in the upstream repo and is correctly referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`.

## Conclusion

All source metadata is complete. Repository URL, commit hash, and config.yaml path are all present and verified. The commit message in google/fonts PR #5559 explicitly confirms the upstream repo and commit. Status is `complete` with HIGH confidence.
