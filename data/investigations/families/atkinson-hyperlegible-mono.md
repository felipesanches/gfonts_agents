# Investigation: Atkinson Hyperlegible Mono

## Summary

| Field | Value |
|-------|-------|
| Family Name | Atkinson Hyperlegible Mono |
| Slug | atkinson-hyperlegible-mono |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible-next-mono |
| Commit Hash | 154d50362016cc3e873eb21d242cd0772384c8f9 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/atkinson-hyperlegible-next-mono"
  commit: "154d50362016cc3e873eb21d242cd0772384c8f9"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AtkinsonHyperlegibleMono-Italic[wght].ttf"
    dest_file: "AtkinsonHyperlegibleMono-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AtkinsonHyperlegibleMono[wght].ttf"
    dest_file: "AtkinsonHyperlegibleMono[wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Atkinson Hyperlegible Mono was added to Google Fonts on 2024-11-20. The onboarding commit in google/fonts is `a4ccc36e5` ("Atkinson Hyperlegible Mono: Version 2.001 added"), which explicitly states the upstream repo and commit. PR #8519 body confirms: "taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next-mono at commit https://github.com/googlefonts/atkinson-hyperlegible-next-mono/commit/154d50362016cc3e873eb21d242cd0772384c8f9."

The commit hash `154d50362016cc3e873eb21d242cd0772384c8f9` is confirmed in the upstream cache at `googlefonts/atkinson-hyperlegible-next-mono` (dated 2024-11-20 14:50:37 +0100, "last fixes"), which is just minutes before the google/fonts onboarding commit, confirming this is the exact commit used.

The `sources/config.yaml` file exists at the referenced commit and specifies:
- Sources: `AtkinsonHyperlegibleMono.glyphs` and `AtkinsonHyperlegibleMono-Italic.glyphs`
- `cleanUp: true`
- Full STAT table configuration for wght and ital axes

The repository name `atkinson-hyperlegible-next-mono` reflects the historical naming (the project was initially called "next mono" before being released as "Atkinson Hyperlegible Mono"). The config_yaml field was added by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

## Conclusion

Status is complete. All required fields (repository_url, commit, config_yaml) are present and verified in METADATA.pb. The commit timestamp aligns precisely with the google/fonts onboarding. No further action needed.
