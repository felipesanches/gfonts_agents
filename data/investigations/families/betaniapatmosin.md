# Investigation: Betania Patmos In

## Summary

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos In |
| Slug | betania-patmos-in |
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
    source_file: "fonts/ttf/BetaniaPatmosIn-Regular.ttf"
    dest_file: "BetaniaPatmosIn-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The font was added to google/fonts on 2026-01-23 in commit `caf0f148c` by Emma Marichal. The commit message explicitly documents the upstream source:

> "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

This is the same upstream repository and commit hash as all other Betania Patmos variants, all from the upstream merge commit dated 2026-01-15 ("Merge pull request #4 from emmamarichal/main - build fonts"). Betania Patmos In was onboarded on 2026-01-23, same day as the GDL and Guide Line variants (Betania Patmos base was onboarded 8 days earlier on 2026-01-15).

The METADATA.pb source block contains all required fields: `repository_url`, `commit`, `config_yaml: "sources/config.yaml"`, and `branch: "main"`. The config.yaml at the recorded commit specifies `betania-patmos.glyphs` as the source, shared by all five Betania Patmos variants.

The upstream repository is NOT currently cloned to the local fontc_crater_cache.

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields — all correct and verified. No action needed.
