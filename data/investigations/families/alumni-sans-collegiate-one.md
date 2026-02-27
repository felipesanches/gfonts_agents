# Investigation: Alumni Sans Collegiate One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans Collegiate One |
| Slug | alumni-sans-collegiate-one |
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
    source_file: "fonts/ttf/AlumniSansCollegiateOne-Regular.ttf"
    dest_file: "AlumniSansCollegiateOne-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/AlumniSansCollegiateOne-Italic.ttf"
    dest_file: "AlumniSansCollegiateOne-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows two onboarding commits:

- `0df02275b` — "Alumni Sans Collegiate One: Version 1.010 added (#4489)"
- `87033c631` — "[gftools-packager] Alumni Sans Collegiate One: Version 1.100 added (#4855)", merged 2022-07-01

The v1.100 commit body explicitly states:

> "Alumni Sans Collegiate One Version 1.100 taken from the upstream repo https://github.com/googlefonts/alumni-sans-collegiate at commit https://github.com/googlefonts/alumni-sans-collegiate/commit/9dc96be1ead732fb1677c88632665e0bbf2e4ee2."

This exactly matches the commit recorded in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/alumni-sans-collegiate` and the top commit is `9dc96be` (message: "sample image updated", dated 2022-06-30), confirming the hash is correct.

The `sources/config.yml` file exists in the upstream repo and contains:
```yaml
sources:
  - AlumniSansCollegiate.glyphs
  - AlumniSansCollegiate-Italic.glyphs
familyName: "Alumni Sans Collegiate One"
buildVariable: false
autohintTTF: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

All fields in the METADATA.pb source block are accurate and verified against the google/fonts commit history and the upstream repo cache.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified against the gftools-packager onboarding commit message and the upstream repo cache. No changes are needed.
