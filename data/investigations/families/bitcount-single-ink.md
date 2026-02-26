# Investigation Report: Bitcount Single Ink

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bitcount Single Ink |
| Designer | Petr van Blokland |
| License | OFL |
| Date Added | 2025-01-10 |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit | `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` |
| Branch | main |
| Config YAML | `sources/config.yaml` (upstream) |
| Status | complete |

## How URL Found

The repository URL is documented in the METADATA.pb `source {}` block and in the copyright string: "Copyright 2024 The Bitcount Project Authors (https://github.com/petrvanblokland/TYPETR-Bitcount)". This is the same upstream repo as Bitcount Single.

## How Commit Determined

Bitcount Single Ink has had two onboarding events:

1. **Initial add (2025-01-17)**: Commit `9cc1c52fc` by Yanone added Version 1.0, taken from upstream commit `af0818eaeb3b0839806ea19134fc18f317cdcf5a` (the same as Bitcount Single).

2. **Update to Version 1.001 (2025-09-11)**: Commit `cdcbeee55` by Emma Marichal updated to Version 1.001, taken from upstream commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`.

The current METADATA.pb records the newer commit `89e7994f7`, which is the most recent update.

### Cross-verification

The commit `89e7994f7` was verified in the upstream repo. It corresponds to "Merge pull request #37 from petrvanblokland/fix-ligatures". Between the initial commit (af0818eae) and this updated commit, there are 17 commits including ligature fixes, axis range corrections, font version bumps, and documentation updates.

The onboarding commit message explicitly states:
> "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f."

## Config YAML Status

The upstream repo has `sources/config.yaml` at commit `89e7994f7` with content:
```yaml
familyName: Bitcount
```

This is referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`. Note that unlike Bitcount Single, there is no override config.yaml in the google/fonts directory for Bitcount Single Ink. The upstream config only sets `familyName: Bitcount`, which may not be specific enough for the "Single Ink" sub-family.

However, the font binary was taken pre-built from the upstream repo (`fonts/ttf/variable/BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf`), so the config.yaml is primarily for reference rather than active building.

## Verification

- **Upstream repo accessible**: Yes, cached at `/mnt/shared/upstream_repos/fontc_crater_cache/petrvanblokland/TYPETR-Bitcount/`
- **Commit exists in repo**: Yes - `89e7994f7 Merge pull request #37 from petrvanblokland/fix-ligatures`
- **Font file at commit**: Yes - `fonts/ttf/variable/BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf`
- **Source files at commit**: Yes - `sources/Bitcount_Template.designspace` and UFO sources present
- **Config YAML**: Exists at `sources/config.yaml` in upstream (minimal content)

## Confidence Level

**HIGH** - Both the initial add and the update have explicit commit references in their gftools-packager commit messages. The current commit (89e7994f7) matches the Version 1.001 update.

## Open Questions

None. All source data is verified and documented.

## Notes

- This family shares the same upstream repo as Bitcount Single and all other Bitcount variants.
- The update from Version 1.0 to 1.001 was driven by PR #37 in the upstream repo which fixed ligature issues.
- A subsequent "bump version" commit (711bcf6c1) by Emma slightly updated the binary again, but this appears to be a metadata-only change and the METADATA.pb commit hash was not changed.
