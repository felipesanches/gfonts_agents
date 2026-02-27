# Investigation: Alumni Sans Collegiate One SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans Collegiate One SC |
| Slug | alumni-sans-collegiate-one-sc |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alumni-sans-collegiate |
| Commit Hash | 9dc96be1ead732fb1677c88632665e0bbf2e4ee2 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alumni-sans-collegiate"
  commit: "9dc96be1ead732fb1677c88632665e0bbf2e4ee2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AlumniSansCollegiateOneSC-Regular.ttf"
    dest_file: "AlumniSansCollegiateOneSC-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/AlumniSansCollegiateOneSC-Italic.ttf"
    dest_file: "AlumniSansCollegiateOneSC-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows one onboarding commit:

- `9b0b4fda4` — "Alumni Sans Collegiate One SC: Version 1.100 added", merged 2024-05-27

The commit body states:

> "Taken from the upstream repo https://github.com/googlefonts/alumni-sans-collegiate at commit https://github.com/googlefonts/alumni-sans-collegiate/commit/9dc96be1ead732fb1677c88632665e0bbf2e4ee2."

This exactly matches the commit recorded in METADATA.pb. The upstream repo is shared with Alumni Sans Collegiate One and is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/alumni-sans-collegiate`. The top commit is `9dc96be` (message: "sample image updated", dated 2022-06-30), confirming the hash is correct.

Note: Alumni Sans Collegiate One SC was added on 2024-05-27, but uses the same upstream commit as Alumni Sans Collegiate One (added in 2022). This is expected — both families are derived from the same upstream source files (`AlumniSansCollegiate.glyphs` and `AlumniSansCollegiate-Italic.glyphs`) at the same repository state.

The `sources/config.yml` exists in the upstream repo at `9dc96be`. Its `familyName` is set to "Alumni Sans Collegiate One" rather than "Alumni Sans Collegiate One SC", but this is handled via the gftools-packager `files` mapping rather than the config. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

All fields in the METADATA.pb source block are accurate and verified against the google/fonts commit history and the upstream repo cache.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No changes are needed.
