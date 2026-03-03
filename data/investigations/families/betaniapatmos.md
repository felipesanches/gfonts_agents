# Investigation: Betania Patmos

## Summary

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos |
| Slug | betania-patmos |
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
    source_file: "fonts/ttf/BetaniaPatmos-Regular.ttf"
    dest_file: "BetaniaPatmos-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The font was added to google/fonts on 2026-01-15 in commit `9adc7b48d` by Emma Marichal. The commit message explicitly documents the upstream source:

> "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

The repository URL is also confirmed by the copyright string: "Copyright 2024 The Betania Patmos Project Authors (https://github.com/huertatipografica/betania-patmos)".

The upstream commit `08c83ac` is a merge commit dated 2026-01-15 with message "Merge pull request #4 from emmamarichal/main - build fonts". The font was built and onboarded on the same day — a clean workflow.

The METADATA.pb source block contains all required fields: `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, and `branch: "main"`. The config.yaml at that commit specifies `betania-patmos.glyphs` as the source, and is shared by all five Betania Patmos variants (Betania Patmos, GDL, Guide Line, In, and In GDL).

The upstream repository is NOT currently cloned to the local fontc_crater_cache (the `huertatipografica/betania-patmos` directory does not exist in the cache, though other huertatipografica repos are present).

This family is one of five Betania Patmos variants all sharing the same upstream repository and commit hash. Each was onboarded separately to google/fonts as an independent font family.

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields — all correct and verified. No action needed.
