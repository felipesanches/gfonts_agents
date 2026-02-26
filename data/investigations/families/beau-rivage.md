# Beau Rivage - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Beau Rivage |
| Repository URL | https://github.com/googlefonts/beau-rivage |
| Commit Hash | a80b72a03f6ea0a5667c58620973efdb72384ffa |
| Config YAML | sources/config.yml |
| Status | complete |
| Category | HANDWRITING |
| Designer | Robert Leuschke |
| Date Added | 2022-02-17 |

## How the Repository URL Was Found

The repository URL was recorded directly in the gftools-packager commit message when the font was first added to Google Fonts. The commit `4d3115f1e` in google/fonts ("Beau Rivage: Version 1.010; ttfautohint (v1.8.3) added", PR #4323, February 2022) explicitly states:

> "Beau Rivage Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/beau-rivage at commit https://github.com/googlefonts/beau-rivage/commit/a80b72a03f6ea0a5667c58620973efdb72384ffa."

The METADATA.pb `source` block also contains the repository URL.

## How the Commit Hash Was Determined

The commit hash `a80b72a03f6ea0a5667c58620973efdb72384ffa` was explicitly referenced in the gftools-packager commit message and PR #4323. The PR was authored by Viviana Monsalve (vv-monsalve) and co-authored by Rosalie Wagner.

The commit in the upstream repo is titled "description moved to documentation dir", dated just before the font was added to Google Fonts.

This was the initial addition of Beau Rivage to Google Fonts - the font binary has not been updated since.

## Config YAML Status

**config.yaml exists** as `sources/config.yml` (note: `.yml` extension, not `.yaml`) at the recorded commit. Its contents:

```yaml
sources:
  - BeauRivage-Pro.glyphs
familyName: "Beau Rivage"
buildVariable: false
# autohintTTF: false
```

This is a valid gftools-builder configuration pointing to `BeauRivage-Pro.glyphs` as the source, building static fonts only (no variable font).

The METADATA.pb `source` block correctly references `config_yaml: "sources/config.yml"`.

## Verification

- **Repository exists**: Yes, cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/beau-rivage/`
- **Commit exists**: Yes, `a80b72a` confirmed ("description moved to documentation dir")
- **Config YAML exists at commit**: Yes, `sources/config.yml` is present and valid
- **Commit hash matches PR reference**: Yes, both the commit message and PR reference `a80b72a03f6ea0a5667c58620973efdb72384ffa`
- **Source block in METADATA.pb**: Complete with repository_url, commit, config_yaml, branch, and file mappings
- **Font files mapped**: `fonts/ttf/BeauRivage-Regular.ttf` -> `BeauRivage-Regular.ttf`
- **Repo structure at commit**: Standard googlefonts layout with sources/, fonts/, documentation/, .github/

## Confidence Level

**High** - All data is fully verified. The commit hash was explicitly referenced by gftools-packager in the initial onboarding commit. The config.yml exists at the recorded commit. The source block is complete.

## Open Questions

None. This family is fully documented and verified.
