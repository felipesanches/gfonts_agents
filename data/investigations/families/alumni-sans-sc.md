# Investigation: Alumni Sans SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans SC |
| Slug | alumni-sans-sc |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alumni |
| Commit Hash | 44a7998fa2bfa1b3e119983cdc565dd7f0f03bda |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alumni"
  commit: "44a7998fa2bfa1b3e119983cdc565dd7f0f03bda"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AlumniSansSC[wght].ttf"
    dest_file: "AlumniSansSC[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AlumniSansSC-Italic[wght].ttf"
    dest_file: "AlumniSansSC-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows one onboarding commit:

- `521d1cdf3` — "Alumni Sans SC: Version 1.016 added", merged 2024-05-27

The commit body states:

> "Taken from the upstream repo https://github.com/googlefonts/alumni at commit https://github.com/googlefonts/alumni/commit/44a7998fa2bfa1b3e119983cdc565dd7f0f03bda."

This exactly matches the commit recorded in METADATA.pb. The upstream repo is shared with Alumni Sans (the non-SC variant) and is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/alumni`. The top commit is `44a7998` (message: "one blank line added to the OFL", dated 2021-12-18), confirming the hash is correct.

Note that this is the same repository and commit used for the original Alumni Sans onboarding. Alumni Sans SC is a small-capitals variant derived from the same upstream source files. The SC variant was added to google/fonts in May 2024, but the upstream commit references the same state of the repository that was used for the regular Alumni Sans onboarding in January 2022.

The `sources/config.yml` exists in the upstream repo and is a gftools-builder configuration referencing `AlumniSans.glyphs` and `AlumniSans-Italic.glyphs` with full STAT axis table definitions. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

Cross-reference: The Alumni Sans METADATA.pb (non-SC) currently records a different (incorrect) commit `28754a9295` for the same repository — see the alumni-sans investigation for details. The Alumni Sans SC METADATA.pb correctly preserves `44a7998`, which is the actual onboarding commit.

All fields in the METADATA.pb source block are accurate and verified.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified against the google/fonts onboarding commit message and the upstream repo cache. No changes are needed.
