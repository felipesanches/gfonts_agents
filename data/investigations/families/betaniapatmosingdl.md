# Investigation: Betania Patmos In GDL

## Summary

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos In GDL |
| Slug | betania-patmos-in-gdl |
| License Dir | ofl |
| Repository URL | https://github.com/huertatipografica/betania-patmos |
| Commit Hash | 08c83ac9540b0b2bf86ddf6b632651142f31a93c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/huertatipografica/betania-patmos"
  commit: "08c83ac9540b0b2bf86ddf6b632651142f31a93c"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BetaniaPatmosInGDL-Regular.ttf"
    dest_file: "BetaniaPatmosInGDL-Regular.ttf"
  }
  branch: "main"
}
```

(Note: METADATA.pb also has `display_name: "Betania Patmos In Guideline"` indicating "GDL" stands for "Guideline".)

## Investigation

The font was added to google/fonts on 2026-01-23 in commit `e7a906896` by Emma Marichal. The commit message explicitly documents the upstream source:

> "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

This is the same upstream repository and commit hash as all other Betania Patmos variants. The upstream commit `08c83ac` is a merge commit dated 2026-01-15 with message "Merge pull request #4 from emmamarichal/main - build fonts".

The config.yaml at the recorded commit specifies `betania-patmos.glyphs` as the source file (shared by all five Betania Patmos variants):

```yaml
sources:
  - betania-patmos.glyphs
buildVariable: false
buildStatic: true
buildTTF: true
buildOTF: true
buildWebfont: true
checkCompatibility: false
interpolate: false
cleanUp: true
```

The METADATA.pb source block contains all required fields: `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, and `branch: "main"`. The upstream repository is NOT currently cloned to the local fontc_crater_cache.

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields — all correct and verified. No action needed.
