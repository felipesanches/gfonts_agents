# Cormorant SC - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cormorant SC |
| **Designer** | Christian Thalmann |
| **Repository URL** | https://github.com/CatharsisFonts/Cormorant |
| **Commit** | `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` |
| **Branch** | master |
| **Config YAML** | `sources/build.yaml` |
| **Date Added** | 2017-01-18 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` is the shared upstream repo for all Cormorant variants. It is documented in:

1. METADATA.pb source block
2. Copyright strings: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
3. PR #4892 body: "Cormorant SC Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"

## How Commit Determined

The commit `cc1bfb51ce6568cb3abf9199ab718d543f6fa189` is explicitly referenced in:

1. **METADATA.pb source block**: `commit: "cc1bfb51ce6568cb3abf9199ab718d543f6fa189"`
2. **google/fonts commit 34b64bb41** (PR #4892, by m4rc1e): "Cormorant SC Version 4.000 taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/cc1bfb51ce6568cb3abf9199ab718d543f6fa189"
3. **PR #4892 body**: Same explicit reference

This commit is "Merge pull request #67 from m4rc1e/gf-mastering". Cormorant SC has NOT been updated to the newer commit (6d210fd) unlike Cormorant Garamond and Cormorant Infant. This is because the newer commit (PR #75) focused on building variable fonts for Garamond and Infant, and Cormorant SC remains as static fonts.

## Config YAML Status

At commit `cc1bfb51`, only one config file exists: `sources/build.yaml`. This config is specifically for building the main Cormorant variable fonts:
```yaml
sources:
  - Cormorant.glyphs
  - Cormorant-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Cormorant
buildStatic: False
buildWebfont: False
...
```

**Note on config_yaml accuracy**: The `build.yaml` config at this commit builds the main Cormorant family, not Cormorant SC specifically. The Cormorant SC static fonts (`fonts/ttf/CormorantSC-*.ttf`) were pre-built binaries included in the upstream repo at that commit. There was no separate SC-specific build config at cc1bfb5.

At the newer HEAD commit (6d210fd), separate per-family configs exist (config-cormorant.yaml, config-garamond.yaml, config-infant.yaml, config-unicase.yaml, config-upright.yaml) but there is still no SC-specific config. The SC fonts are produced as a byproduct of the main Cormorant build through the `buildSmallCap` mechanism.

No override config.yaml exists in the google/fonts family directory.

## Verification

- **Upstream repo cached**: Yes, at `/mnt/shared/upstream_repos/fontc_crater_cache/CatharsisFonts/Cormorant/`
- **Commit exists**: Yes, verified with `git log`
- **Config file exists at commit**: Yes, `sources/build.yaml` exists at cc1bfb5 (though it builds main Cormorant, not SC specifically)
- **Font files match**: METADATA.pb maps 5 static files from `fonts/ttf/CormorantSC-*.ttf`, all present at the commit
- **Repository accessible**: Yes

## Confidence Level

**HIGH** - All data is explicitly documented in commit messages, PR body, and METADATA.pb. The commit and URL are confirmed through multiple independent sources.

The `config_yaml` pointing to `build.yaml` is the best available option since no SC-specific config existed at that commit. The SC static fonts were pre-built binaries in the upstream repo.

## Open Questions

- Cormorant SC has not been updated to variable fonts like Cormorant Garamond and Cormorant Infant were. At the upstream HEAD (6d210fd), there is still no SC-specific config, suggesting SC variable fonts were not part of the vf-and-gf effort. This may be intentional (small caps may be handled differently) or may be a future task.
