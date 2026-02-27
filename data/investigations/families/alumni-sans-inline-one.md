# Investigation: Alumni Sans Inline One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans Inline One |
| Slug | alumni-sans-inline-one |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alumni-sans-inline |
| Commit Hash | 81ea544e0ce487475c75df9545cd3df946c7ba26 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alumni-sans-inline"
  commit: "81ea544e0ce487475c75df9545cd3df946c7ba26"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AlumniSansInlineOne-Regular.ttf"
    dest_file: "AlumniSansInlineOne-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/AlumniSansInlineOne-Italic.ttf"
    dest_file: "AlumniSansInlineOne-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows one onboarding commit:

- `d2ed457c9` — "Alumni Sans Inline One: Version 1.100; ttfautohint (v1.8.3) added (#4331)", merged 2022-02-25

The commit body explicitly states:

> "Alumni Sans Inline One Version 1.100; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/alumni-sans-inline at commit https://github.com/googlefonts/alumni-sans-inline/commit/81ea544e0ce487475c75df9545cd3df946c7ba26."

This exactly matches the commit recorded in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/alumni-sans-inline` and the top commit is `81ea544` (message: "Description updated", dated 2022-02-24), confirming the hash is correct and is the most recent commit in the upstream repo.

The `sources/config.yml` exists in the upstream repo and contains:
```yaml
sources:
  - AlumniSansInline.glyphs
  - AlumniSansInline-Italic.glyphs
familyName: "Alumni Sans Inline One"
buildVariable: false
# autohintTTF: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

All fields in the METADATA.pb source block are accurate and verified against the gftools-packager onboarding commit message and the upstream repo cache.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No changes are needed.
