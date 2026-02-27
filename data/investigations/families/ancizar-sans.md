# Investigation: Ancizar Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Ancizar Sans |
| Slug | ancizar-sans |
| License Dir | ofl |
| Repository URL | https://github.com/UNAL-OMD/UNAL-Ancizar |
| Commit Hash | 54a5aa2153b4485ff2710612d47183c346e6b842 |
| Config YAML | sources/config-sans.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/UNAL-OMD/UNAL-Ancizar"
  commit: "54a5aa2153b4485ff2710612d47183c346e6b842"
  config_yaml: "sources/config-sans.yaml"
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
    source_file: "fonts/variable/AncizarSans[wght].ttf"
    dest_file: "AncizarSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AncizarSans-Italic[wght].ttf"
    dest_file: "AncizarSans-Italic[wght].ttf"
  }
  branch: "main"
}
```

## Investigation

Ancizar Sans was added to google/fonts at commit `544bd4e40` (April 16, 2025, "Ancizar Sans: Version 8.100 added"), authored by Yanone. The commit message explicitly states: "Taken from the upstream repo https://github.com/UNAL-OMD/UNAL-Ancizar at commit https://github.com/UNAL-OMD/UNAL-Ancizar/commit/54a5aa2153b4485ff2710612d47183c346e6b842. Resolves #9095."

The commit hash `54a5aa2153b4485ff2710612d47183c346e6b842` was verified in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/UNAL-OMD/UNAL-Ancizar/`. The commit message is "New Sans binaries" (April 16, 2025, 15:50), confirming this is the correct onboarding commit used to produce the variable font binaries.

The `sources/config-sans.yaml` exists in the upstream repo and contains:

```yaml
sources:
  - AncizarSans.glyphs
  - AncizarSans-Italic.glyphs
buildVariable: true
buildStatic: true
buildTTF: false
buildOTF: false
buildWebfont: false
buildSmallCap: false
```

This is a valid gftools-builder configuration. The Glyphs source files `AncizarSans.glyphs` and `AncizarSans-Italic.glyphs` are present in the `sources/` directory.

## Conclusion

Status is complete. All required fields (`repository_url`, `commit`, `config_yaml`) are correctly populated in METADATA.pb. The commit hash matches the onboarding commit referenced in the google/fonts commit message. No action needed.
