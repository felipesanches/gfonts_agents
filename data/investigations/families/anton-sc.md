# Investigation: Anton SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Anton SC |
| Slug | anton-sc |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/AntonFont |
| Commit Hash | beb92fcad87808357123bb66881b4032dc96efe7 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/AntonFont"
  commit: "beb92fcad87808357123bb66881b4032dc96efe7"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AntonSC-Regular.ttf"
    dest_file: "AntonSC-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Repository

The upstream repository `googlefonts/AntonFont` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/AntonFont`. The repository URL and commit hash are pre-existing in METADATA.pb.

### Commit Hash

The commit `beb92fcad87808357123bb66881b4032dc96efe7` was verified present in the cached repo: `git cat-file -t beb92fca` returns `commit`. The commit is dated 2024-04-04 with message "Fix weight axis" by Simon Cozens. It is the HEAD (only commit) in the repo at the time of investigation.

The google/fonts TTF was last updated in commit `7023dbc93` ("Anton SC: Version 2.116; ttfautohint (v1.8.4.7-5d5b) added") on 2024-05-27. The commit body confirms: "Taken from the upstream repo https://github.com/googlefonts/AntonFont at commit https://github.com/googlefonts/AntonFont/commit/beb92fcad87808357123bb66881b4032dc96efe7." This exactly matches METADATA.pb.

### Source Files

The `sources/` directory contains:
- `Anton.glyphs` — Glyphs format source
- `build.sh` — build script
- `config.yaml` — gftools-builder configuration

```yaml
sources:
  - Anton.glyphs
```

### Config YAML

`sources/config.yaml` exists in the upstream repo and is referenced in METADATA.pb `config_yaml: "sources/config.yaml"`. The config references `Anton.glyphs` as the source. Anton SC is compiled from the Anton.glyphs file using gftools-builder.

## Conclusion

All source metadata is complete. Repository URL, commit hash, and config.yaml are all present and verified. Status is `complete` with HIGH confidence.
