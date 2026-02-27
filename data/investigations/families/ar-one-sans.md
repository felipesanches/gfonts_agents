# Investigation: AR One Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | AR One Sans |
| Slug | ar-one-sans |
| License Dir | ofl |
| Repository URL | https://github.com/niteeshy/ar-one-sans |
| Commit Hash | 6dc5e6850f2ced9f28e733c9a7860c54246e17a8 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/niteeshy/ar-one-sans"
  commit: "6dc5e6850f2ced9f28e733c9a7860c54246e17a8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/AROneSans[ARRR,wght].ttf"
    dest_file: "AROneSans[ARRR,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The repository URL `https://github.com/niteeshy/ar-one-sans` was established in the METADATA.pb source block from the initial onboarding. The font was onboarded by Viviana Monsalve (vv-monsalve) via commit `29abece3f` ("AR One Sans: Version 1.001;gftools[0.9.33] added", 2023-09-06), which stated: "AR One Sans Version 1.001;gftools[0.9.33] taken from the upstream repo https://github.com/niteeshy/ar-one-sans at commit https://github.com/niteeshy/ar-one-sans/commit/a463b112ca9393f1904765e0f32891b849eb9cf1."

**Commit hash discrepancy**: The original onboarding commit `a463b112ca9393f1904765e0f32891b849eb9cf1` is no longer present in the upstream repository. The repo appears to have been force-pushed, leaving only a single commit `6dc5e6850f2ced9f28e733c9a7860c54246e17a8` (dated 2024-04-14, "Update README.md"), which is 7 months newer than the original onboarding. The current METADATA.pb commit was updated in the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported info from fontc_crater targets.json.

The config file `sources/config.yaml` exists at the current commit and contains a gftools-builder configuration referencing `AROneSans.glyphs` as the source file with ARRR and wght axes defined.

The upstream repo cache at `niteeshy/ar-one-sans` contains only the single remaining commit. The font was added to google/fonts on 2023-09-06 (date_added: "2023-09-06" per METADATA.pb).

## Conclusion

Status is effectively complete: all required fields (repository_url, commit, config_yaml) are present in METADATA.pb. The commit hash `6dc5e685` is the best available reference since the original onboarding commit `a463b112` was lost to a force-push. The config.yaml exists at the recorded commit. No additional action is required unless the original onboarding commit can be recovered from other sources.
