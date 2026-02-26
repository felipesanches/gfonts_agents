# Investigation Report: Braah One

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Braah One |
| Designer | Ashish Kumar |
| License | OFL |
| Date Added | 2023-03-24 |
| Repository URL | https://github.com/artandtype/Braah |
| Commit Hash | `2b7ba2ea006af5a55313158531b6f0b71eca5ff8` |
| Branch | master |
| Config YAML | Override in google/fonts |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/artandtype/Braah` is recorded in the METADATA.pb `source {}` block and matches the copyright string in the font files. It was set by the gftools-packager commit that added the font.

## How Commit Determined

The commit hash `2b7ba2ea006af5a55313158531b6f0b71eca5ff8` was explicitly referenced in the gftools-packager commit message:

- google/fonts commit `20db4c2da`: "[gftools-packager] Braah One: Version 1.001; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.29] added"
  - Body: "taken from the upstream repo https://github.com/artandtype/Braah at commit https://github.com/artandtype/Braah/commit/2b7ba2ea006af5a55313158531b6f0b71eca5ff8"
  - Associated with PR #6302, submitted by emmamarichal

This was the Version 1.001 update. The initial Version 1.000 was from a different commit (`d10ec8d1efc1d3ed756348ea4b94f71849f6ec26`).

## Config YAML Status

- No `config.yaml` exists in the upstream repository at the recorded commit
- An override `config.yaml` exists in `ofl/braahone/config.yaml` in google/fonts, auto-generated from the `sources/BraahOne.glyphs` file
- The override was added in commit `3b645f8db`: "Adding 119 automatically generated `config.yaml` files"
- The `config_yaml` field is correctly omitted from the METADATA.pb source block (override detected automatically)

Override config.yaml contents:
```yaml
buildVariable: false
sources:
  - sources/BraahOne.glyphs
```

## Verification

1. **Commit exists in upstream**: Confirmed. `2b7ba2ea006af5a55313158531b6f0b71eca5ff8` exists in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/artandtype/Braah`
2. **File paths match**: METADATA.pb references `fonts/ttf/BraahOne-Regular.ttf` which exists at that commit
3. **Source files**: `sources/BraahOne.glyphs` is present at the commit, matching the override config
4. **gftools-packager reference matches**: The commit hash in METADATA.pb matches the gftools-packager commit message exactly
5. **PR #6302**: Confirms the update was submitted by emmamarichal, referencing issue #6227

## Confidence Level

**HIGH** - The commit hash was directly recorded by gftools-packager during the Version 1.001 onboarding. It exists in the upstream repo and matches the font binary files used. The override config.yaml correctly references the Glyphs source file.

## Open Questions

None. This family is fully documented.
