# Investigation: Alumni Sans Pinstripe

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans Pinstripe |
| Slug | alumni-sans-pinstripe |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alumni-sans-pinstripe |
| Commit Hash | 26cf834f2eca219b017478be9ea1387c78756e78 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alumni-sans-pinstripe"
  commit: "26cf834f2eca219b017478be9ea1387c78756e78"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AlumniSansPinstripe-Regular.ttf"
    dest_file: "AlumniSansPinstripe-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/AlumniSansPinstripe-Italic.ttf"
    dest_file: "AlumniSansPinstripe-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows one onboarding commit:

- `9d68dcf8e` — "Alumni Sans Pinstripe: Version 1.010; ttfautohint (v1.8.4.7-5d5b) added (#4759)", merged 2022-06-17

The commit body explicitly states:

> "Alumni Sans Pinstripe Version 1.010; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/googlefonts/alumni-sans-pinstripe at commit https://github.com/googlefonts/alumni-sans-pinstripe/commit/26cf834f2eca219b017478be9ea1387c78756e78."

This exactly matches the commit recorded in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/alumni-sans-pinstripe` and the top commit is `26cf834` (message: "v1.010 fonts added", dated 2022-06-09), confirming the hash is correct and is the most recent commit in the upstream repo.

The `sources/config.yml` exists in the upstream repo and contains:
```yaml
sources:
  - AlumniSansPinstripe.glyphs
  - AlumniSansPinstripe-Italic.glyphs
familyName: "Alumni Sans Pinstripe"
buildVariable: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

All fields in the METADATA.pb source block are accurate and verified against the gftools-packager onboarding commit message and the upstream repo cache.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No changes are needed.
