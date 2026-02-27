# Investigation: Bagel Fat One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bagel Fat One |
| Slug | bagel-fat-one |
| License Dir | ofl |
| Repository URL | https://github.com/JAMO-TYPEFACE/BagelFat |
| Commit Hash | d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b |
| Config YAML | Sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/JAMO-TYPEFACE/BagelFat"
  commit: "d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/BagelFatOne-Regular.ttf"
    dest_file: "BagelFatOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The TTF files have two commits:

- `420218575` — "Update BagelFatOne-Regular.ttf" (2023-05-24) — manual update: "Adding missing glyph from GF Kernel"
- `d9406e5bf` — "[gftools-packager] Bagel Fat One: Version 1.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] added" (2023-05-18)

The gftools-packager commit message (`d9406e5bf`) says:

> Bagel Fat One Version 1.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] taken from the upstream repo
> https://github.com/JAMO-TYPEFACE/BagelFat at commit
> https://github.com/JAMO-TYPEFACE/BagelFat/commit/5ff1333d3384611f499419a844e2b3006dc7cacd.

However, METADATA.pb records `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b`, which is different from the originally packaged commit `5ff1333`.

### Commit Hash Analysis

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/JAMO-TYPEFACE/BagelFat`:

- `d8dd4e8b5dd0e74fbf87a78290ee9a9aaed1270b` (2023-05-24) — "Merge pull request #3 from aaronbell/main"

The commit `5ff1333d3384611f499419a844e2b3006dc7cacd` referenced in the gftools-packager message is NOT present in the local cache.

Notably, both the upstream commit `d8dd4e8` (2023-05-24) and the manual TTF update in google/fonts (`420218575`, also 2023-05-24) share the same date. This strongly suggests that the missing-glyph fix was made upstream (in `d8dd4e8`, merge of PR #3 from aaronbell) and simultaneously applied as a manual TTF update in google/fonts. The METADATA.pb was then updated to record this newer commit as the canonical onboarding point.

The METADATA.pb's commit `d8dd4e8` is therefore the more accurate reference — it corresponds to the actual TTF files served in production.

### Config YAML Verification

The `config.yaml` at `Sources/config.yaml` in the upstream repo contains:

```yaml
sources:
  - BagelFat.glyphs
familyName: "Bagel Fat One"
buildOTF: false
```

This is a valid gftools-builder configuration. The `config_yaml: "Sources/config.yaml"` field in METADATA.pb correctly references this file.

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/JAMO-TYPEFACE/BagelFat`

## Conclusion

The METADATA.pb source block is complete. The repository URL and config_yaml path are verified. The commit hash `d8dd4e8` is confirmed in the upstream cache and corresponds to the date of the final TTF update in google/fonts, making it the correct onboarding reference. Confidence is MEDIUM due to the discrepancy between the gftools-packager commit message (`5ff1333`) and the METADATA.pb commit (`d8dd4e8`), though the evidence points to `d8dd4e8` being correct. No action required.
