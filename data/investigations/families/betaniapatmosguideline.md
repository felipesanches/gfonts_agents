# Investigation: Betania Patmos Guide Line

## Summary

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos Guide Line |
| Slug | betania-patmos-guide-line |
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
    source_file: "fonts/ttf/BetaniaPatmosGuideLine-Regular.ttf"
    dest_file: "BetaniaPatmosGuideLine-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The font was added to google/fonts on 2026-01-23 in commit `02c6401c0` by Emma Marichal. The commit message explicitly documents the upstream source:

> "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

This is the same upstream repository and commit hash as all other Betania Patmos variants, all from the upstream merge commit dated 2026-01-15 ("Merge pull request #4 from emmamarichal/main - build fonts").

The METADATA.pb has `display_name: "Betania Patmos Guides"` and `classifications: "SYMBOLS"` for this variant. The category is DISPLAY but classifications indicate SYMBOLS — this font contains ruled guide lines for handwriting practice rather than letterforms, making it distinct from the GDL variant (which stands for "Guideline" and is a handwriting-style font).

The METADATA.pb source block contains all required fields: `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, and `branch: "main"`. The config.yaml at the recorded commit specifies `betania-patmos.glyphs` as the source, shared by all five Betania Patmos variants.

The upstream repository is NOT currently cloned to the local fontc_crater_cache.

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields — all correct and verified. No action needed.
