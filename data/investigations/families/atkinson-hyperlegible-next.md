# Investigation: Atkinson Hyperlegible Next

## Summary

| Field | Value |
|-------|-------|
| Family Name | Atkinson Hyperlegible Next |
| Slug | atkinson-hyperlegible-next |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/atkinson-hyperlegible-next |
| Commit Hash | 7925f50f649b3813257faf2f4c0b381011f434f1 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/atkinson-hyperlegible-next"
  commit: "7925f50f649b3813257faf2f4c0b381011f434f1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AtkinsonHyperlegibleNext[wght].ttf"
    dest_file: "AtkinsonHyperlegibleNext[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AtkinsonHyperlegibleNext-Italic[wght].ttf"
    dest_file: "AtkinsonHyperlegibleNext-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Atkinson Hyperlegible Next was added to Google Fonts on 2025-01-07. The onboarding commit in google/fonts is `66eef7072` ("Atkinson Hyperlegible Next: Version 2.001 added"), which states the upstream repo and original onboarding commit. PR #8813 body confirms: "Taken from the upstream repo https://github.com/googlefonts/atkinson-hyperlegible-next at commit https://github.com/googlefonts/atkinson-hyperlegible-next/commit/5d633f80fc654ef5fffa7cfc257528685158dcef."

**Commit hash discrepancy**: The original onboarding used commit `5d633f80fc654ef5fffa7cfc257528685158dcef`, but the current METADATA.pb contains `7925f50f649b3813257faf2f4c0b381011f434f1` (dated 2025-02-21, "Fix Cairo in CI"). The METADATA.pb was updated by the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which ported data from the fontc_crater targets.json. The fontc_crater targets list apparently used the newer commit `7925f50f` instead of the original onboarding commit.

The current commit `7925f50f` is 45 days newer than the font onboarding date (2025-01-07). The upstream cache at `googlefonts/atkinson-hyperlegible-next` shows only the latest commit (shallow clone), so the original commit `5d633f80` cannot be verified locally.

The `sources/config.yaml` exists at the current commit and specifies:
- Sources: `AtkinsonHyperlegibleNext.glyphs` and `AtkinsonHyperlegibleNext-Italic.glyphs`
- `cleanUp: true`
- Full STAT table configuration for wght and ital axes

## Conclusion

Status is complete in terms of having all required METADATA.pb fields populated. However, the commit hash `7925f50f` in METADATA.pb is newer than the original onboarding commit `5d633f80` referenced in PR #8813. This is a known issue from the fontc_crater batch import. The correct commit should ideally be `5d633f80fc654ef5fffa7cfc257528685158dcef`, but since the repo is only available as a shallow clone locally, this cannot be verified without a full clone. Flagged as MEDIUM confidence due to this commit discrepancy.
