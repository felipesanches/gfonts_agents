# Investigation: Atkinson Hyperlegible

## Summary

| Field | Value |
|-------|-------|
| Family Name | Atkinson Hyperlegible |
| Slug | atkinson-hyperlegible |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible |
| Commit Hash | 1cb311624b2ddf88e9e37873999d165a8cd28b46 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/atkinson-hyperlegible"
  commit: "1cb311624b2ddf88e9e37873999d165a8cd28b46"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AtkinsonHyperlegible-Regular.ttf"
    dest_file: "AtkinsonHyperlegible-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/AtkinsonHyperlegible-Bold.ttf"
    dest_file: "AtkinsonHyperlegible-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/AtkinsonHyperlegible-Italic.ttf"
    dest_file: "AtkinsonHyperlegible-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/AtkinsonHyperlegible-BoldItalic.ttf"
    dest_file: "AtkinsonHyperlegible-BoldItalic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

Atkinson Hyperlegible was added to Google Fonts on 2021-04-30. The original onboarding commit in google/fonts is `1b22086d1` ("Atkinson Hyperlegible: Version 1.006; ttfautohint (v1.8.3) added", PR #3362), whose body explicitly states: "taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible at commit https://github.com/googlefonts/atkinson-hyperlegible/commit/1cb311624b2ddf88e9e37873999d165a8cd28b46."

The commit hash `1cb311624b2ddf88e9e37873999d165a8cd28b46` was added to METADATA.pb by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31). It is confirmed present in the upstream cache at `googlefonts/atkinson-hyperlegible` (dated 2021-04-29 22:23:13 -0500, "OFL single line").

The repository URL was added earlier by Simon Cozens in commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb", 2024-04-03).

The `sources/config.yml` file (note: `.yml` extension, not `.yaml`) exists in the upstream repo at the referenced commit and specifies:
- Sources: `AtkinsonHyperlegible.glyphs` and `AtkinsonHyperlegible-Italic.glyphs`
- `buildVariable: false` (static font build)

## Conclusion

Status is complete. All required fields (repository_url, commit, config_yaml) are present and verified in METADATA.pb. The commit matches the original gftools-packager onboarding reference from PR #3362. No further action needed.
