# Investigation: Ancizar Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | Ancizar Serif |
| Slug | ancizar-serif |
| License Dir | ofl |
| Repository URL | https://github.com/UNAL-OMD/UNAL-Ancizar |
| Commit Hash | 063bdd3121fef76289b035226acdc1b4e885f31a |
| Config YAML | sources/config-serif.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/UNAL-OMD/UNAL-Ancizar"
  commit: "063bdd3121fef76289b035226acdc1b4e885f31a"
  config_yaml: "sources/config-serif.yaml"
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/specimen.jpg"
    dest_file: "article/specimen.jpg"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AncizarSerif[wght].ttf"
    dest_file: "AncizarSerif[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AncizarSerif-Italic[wght].ttf"
    dest_file: "AncizarSerif-Italic[wght].ttf"
  }
  branch: "main"
}
```

## Investigation

Ancizar Serif was added to google/fonts at commit `599dc5827` (April 16, 2025, "Ancizar Serif: Version 8.100 added"), authored by Yanone. The commit message explicitly states: "Taken from the upstream repo https://github.com/UNAL-OMD/UNAL-Ancizar at commit https://github.com/UNAL-OMD/UNAL-Ancizar/commit/063bdd3121fef76289b035226acdc1b4e885f31a. Resolves #9095."

The commit hash `063bdd3121fef76289b035226acdc1b4e885f31a` was verified in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/UNAL-OMD/UNAL-Ancizar/`. The commit message is "New Serif binaries" (April 16, 2025, 16:02), confirming this is the correct onboarding commit. Note that this commit is 11 minutes after the Ancizar Sans commit (`54a5aa2`, 15:50), reflecting separate final binary updates for the two families on the same day.

The `sources/config-serif.yaml` exists in the upstream repo and contains:

```yaml
sources:
  - AncizarSerif.glyphs
  - AncizarSerif-Italic.glyphs
buildVariable: true
buildStatic: true
buildTTF: false
buildOTF: false
buildWebfont: false
buildSmallCap: false
```

This is a valid gftools-builder configuration. The Glyphs source files `AncizarSerif.glyphs` and `AncizarSerif-Italic.glyphs` are present in the `sources/` directory.

Both Ancizar Sans and Ancizar Serif share the same upstream repository (`UNAL-OMD/UNAL-Ancizar`) but use different config YAML files (`config-sans.yaml` and `config-serif.yaml` respectively).

## Conclusion

Status is complete. All required fields (`repository_url`, `commit`, `config_yaml`) are correctly populated in METADATA.pb. The commit hash matches the onboarding commit referenced in the google/fonts commit message. No action needed.
