# Investigation: Alex Brush

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alex Brush |
| Slug | alex-brush |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alex-brush |
| Commit Hash | 1a50bd10383f6c5416f5b4806a9368fd2009ea8c |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alex-brush"
  commit: "1a50bd10383f6c5416f5b4806a9368fd2009ea8c"
  files {
    source_file: "fonts/ttf/AlexBrush-Regular.ttf"
    dest_file: "AlexBrush-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

Alex Brush is a long-standing family in google/fonts, with history going back to the initial commit in 2015. The most recent font update was via PR #5686 ("Alex Brush: Version 1.111", google/fonts commit `3f9fd6d69`). The commit message confirms:

> Alex Brush Version 1.111; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/googlefonts/alex-brush at commit https://github.com/googlefonts/alex-brush/commit/1a50bd10383f6c5416f5b4806a9368fd2009ea8c.

The METADATA.pb was updated in multiple stages:
- `3f9fd6d69` (PR #5686): Added `repository_url` and `commit` to the source block
- `66f91f10f` (2024-04-03, "Merge upstream.yaml into METADATA.pb"): Added `files` and `branch` fields
- `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"): Added `config_yaml: "sources/config.yml"`

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/alex-brush/`. The commit `1a50bd10383f6c5416f5b4806a9368fd2009ea8c` exists and is verified in the cached repository.

The `sources/config.yml` file (note: `.yml` extension, not `.yaml`) exists at the referenced commit, confirmed via `git ls-tree`. Current content:
```yaml
sources:
  - AlexBrush.glyphs
familyName: "Alex Brush"
buildVariable: false
# autohintTTF: false
```

The config references `AlexBrush.glyphs` as the source and sets `buildVariable: false` (static font only, appropriate for a handwriting family).

## Conclusion

METADATA.pb is complete and correct: repository URL, commit hash, and config_yaml path are all present and verified. The `config_yaml` path correctly uses `.yml` (not `.yaml`), which matches the actual filename in the upstream repo. No action needed.
