# Investigation Report: Bitcount Single

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bitcount Single |
| Designer | Petr van Blokland |
| License | OFL |
| Date Added | 2025-01-10 |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `af0818eaeb3b0839806ea19134fc18f317cdcf5a` |
| Branch | main |
| Config YAML | Override in google/fonts |
| Status | complete |

## How URL Found

The repository URL is documented in the METADATA.pb `source {}` block and also appears in the copyright string of the font file: "Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)". The URL was included in the original onboarding commit.

## How Commit Determined

The commit hash `af0818eaeb3b0839806ea19134fc18f317cdcf5a` is explicitly stated in the onboarding commit message by Yanone (2025-01-17):

> "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/af0818eaeb3b0839806ea19134fc18f317cdcf5a."

This commit resolves issue #5468. The commit exists in the upstream repo and corresponds to "Update fixAnchors.py".

### Cross-verification

The commit hash was verified in the cached upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount/`. The file `fonts/ttf/variable/BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf` exists at this commit, matching the `source_file` path in METADATA.pb. The METADATA.pb also maps `OFL.txt` from the upstream repo.

## Config YAML Status

The upstream repo has a `sources/config.yaml` at this commit, but its content is minimal:
```yaml
familyName: Bitcount
```

This config references the family name "Bitcount" (the parent project), not "Bitcount Single" specifically. Because of this, an override `config.yaml` was added in the google/fonts family directory (`ofl/bitcountsingle/config.yaml`) with content:
```yaml
sources:
  - sources/Bitcount_Template.designspace
familyName: Bitcount Single
buildVariable: true
buildOTF: false
```

Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from METADATA.pb.

## Verification

- **Upstream repo accessible**: Yes, cached at `/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount/`
- **Commit exists in repo**: Yes - `af0818eae Update fixAnchors.py`
- **Font file at commit**: Yes - `fonts/ttf/variable/BitcountSingle[CRSV,ELSH,ELXP,slnt,wght].ttf` exists
- **Source files at commit**: Yes - `sources/Bitcount_Template.designspace` and UFO sources present
- **Config YAML**: Override config in google/fonts properly configures the build

## Confidence Level

**HIGH** - The commit hash is explicitly documented in the gftools-packager onboarding commit message, verified to exist in the upstream repo, and the font binary path matches.

## Open Questions

None. This family is fully documented with all source information verified.

## Notes

- Bitcount is a large family project with many sub-families (Single, Double, Grid, Ink variants, Prop variants). They all share the same upstream repo.
- Bitcount Single was onboarded at commit af0818eae, while Bitcount Single Ink was later updated to a newer commit (89e7994f7).
- The font binary in google/fonts was taken directly from pre-built fonts in the upstream repo (`fonts/ttf/variable/`), not compiled via gftools-builder.
