# Investigation: Betania Patmos GDL

## Summary

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos GDL |
| Slug | betania-patmos-gdl |
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
    source_file: "fonts/ttf/BetaniaPatmosGDL-Regular.ttf"
    dest_file: "BetaniaPatmosGDL-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The font was added to google/fonts on 2026-01-23 in commit `c26502dc7` by Emma Marichal. The commit message explicitly documents the upstream source:

> "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

This is the same upstream repository and commit hash as all other Betania Patmos variants. The font was onboarded 8 days after Betania Patmos (base) but all variants share the same upstream snapshot (commit `08c83ac`, a merge dated 2026-01-15 with message "Merge pull request #4 from emmamarichal/main - build fonts").

The METADATA.pb uses `display_name: "Betania Patmos Guideline"` which clarifies that "GDL" stands for "Guideline" — this is distinct from the separate "Betania Patmos Guide Line" (ofl/betaniapatmosguideline) which is categorized as SYMBOLS and contains ruled lines for handwriting practice.

The METADATA.pb source block contains all required fields: `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, and `branch: "main"`. The config.yaml at that commit specifies `betania-patmos.glyphs` as the source, shared by all five Betania Patmos variants.

The upstream repository is NOT currently cloned to the local fontc_crater_cache.

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields — all correct and verified. No action needed.
