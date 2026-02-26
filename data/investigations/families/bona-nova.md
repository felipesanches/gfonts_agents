# Investigation Report: Bona Nova

## Summary

Bona Nova is a serif typeface by Capitalics (Mateusz Machalski, Andrzej Heidrich), added to Google Fonts on 2021-04-13. It includes Regular, Bold, and Italic static weights with support for Latin, Cyrillic, Greek, Hebrew, and Vietnamese scripts. The family has a minisite at bonanova.wtf.

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bona Nova |
| Designer | Capitalics, Mateusz Machalski, Andrzej Heidrich |
| Repository URL | https://github.com/kosmynkab/Bona-Nova |
| Commit Hash | `a5cbdfb8741af20ea5bfe252f0128beed6c8beed` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| License | OFL |
| Date Added | 2021-04-13 |

## How URL Found

The repository URL `https://github.com/kosmynkab/Bona-Nova` is stated in:
- The copyright string in METADATA.pb
- The gftools-packager commit message and PR #3275
- The upstream.yaml file (now merged into METADATA.pb)

## How Commit Determined

There is a discrepancy between the PR body and the current METADATA.pb:

### PR #3275 Reference
PR #3275 (authored by Rosalie Wagner, 2021-04-13) states:
> Bona Nova Version 4.001; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/kosmynkab/Bona-Nova at commit fdc7db4c1fcd4d63a922ea8797881a39d3a62caa.

However, commit `fdc7db4c` does **not** exist in the current upstream repository. This is likely because the repository history was rewritten (force-pushed) at some point after onboarding.

### Current METADATA.pb Reference
The commit hash `a5cbdfb8741af20ea5bfe252f0128beed6c8beed` was added to METADATA.pb in the "Batch 1/4" port from fontc_crater targets list (google/fonts commit `19cdcec59`, by Felipe Sanches, 2025-03-31). This commit is the current HEAD (and only visible commit) of the upstream repository.

### Analysis
The upstream repository is a shallow clone with only one visible commit (`a5cbdfb`, "remove fontbakery report"). The original onboarding commit (`fdc7db4c`) referenced in PR #3275 no longer exists in the repo's accessible history, likely due to a force-push that rewrote history. The current HEAD `a5cbdfb` was adopted as the reference commit from the fontc_crater targets list. Given the repo has only one accessible commit, this is the best available reference.

## Config YAML Status

The config file at `sources/config.yaml` exists at the recorded commit and contains:
```yaml
sources:
      - BonaNova.glyphs
      - BonaNova-Italic.glyphs
    familyName: Bona Nova
    buildVariable: False
```

This is a valid gftools-builder configuration for building static fonts from Glyphs sources.

## Verification

- **Commit exists in upstream**: Yes, verified. `a5cbdfb` is the HEAD (and only accessible commit) of the main branch.
- **Config.yaml exists at commit**: Yes, `sources/config.yaml` is present and valid.
- **Source files match METADATA.pb**: The METADATA.pb references `fonts/ttf/BonaNova-Regular.ttf`, `fonts/ttf/BonaNova-Bold.ttf`, and `fonts/ttf/BonaNova-Italic.ttf`.
- **Branch correct**: main, confirmed.
- **Upstream repo cached**: Yes, at `/mnt/shared/upstream_repos/fontc_crater_cache/kosmynkab/Bona-Nova` (shallow clone).
- **Original PR commit lost**: The commit `fdc7db4c` from PR #3275 no longer exists in the repo.

## Confidence Level

**MEDIUM** -- The repository URL is well-documented and verified. The commit hash `a5cbdfb` is the current HEAD and has a valid config.yaml, but it is not the original onboarding commit referenced in PR #3275 (`fdc7db4c`). The original commit was likely lost to a force-push. Since the repo only has one accessible commit, `a5cbdfb` is the best available reference, and it was the commit used by fontc_crater.

## Open Questions

1. Was the upstream repository history rewritten (force-pushed) after the original onboarding? The PR #3275 references commit `fdc7db4c` which no longer exists.
2. Are the font binaries at the current HEAD (`a5cbdfb`) identical to those at the original onboarding commit (`fdc7db4c`), or have there been changes?
3. The upstream repo is a shallow clone -- would unshallowing reveal the original commit history, or was it truly force-pushed away?
