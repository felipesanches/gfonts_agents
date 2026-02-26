# Bruno Ace SC

**Date investigated**: 2026-02-26
**Status**: complete (with commit hash concern)
**Designer**: Astigmatic
**METADATA.pb path**: `ofl/brunoacesc/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/Bruno-ace |
| Commit (recorded) | `58dc219db32ffd9eaf573f2dc3be2e342410e15a` |
| Commit (actual build) | `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181` |
| Config YAML | `sources/brunoacesc-regular.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/Bruno-ace` is shared with the Bruno Ace family, as both families are built from the same upstream repo. It is recorded in the METADATA.pb `source { repository_url }` field and matches the copyright string ("Copyright 2023 The Bruno Ace Project Authors (https://github.com/googlefonts/Bruno-ace)"). The gftools-packager commit `223112643` and PR #6073 both reference this URL.

## How the Commit Hash Was Identified

The METADATA.pb currently records commit `58dc219db32ffd9eaf573f2dc3be2e342410e15a`. As with the Bruno Ace family (same repo), binary comparison reveals this is **incorrect**:

- The gftools-packager commit `223112643` in google/fonts states: "Bruno Ace SC Version 1.100 taken from the upstream repo [...] at commit [...]/4eb5f7fc38a1548b353b4ee03b1f7043b48ae181."
- PR #6073 body references commit `58dc219` (initial PR state).
- During the PR process, Yanone updated the upstream repo, and the actual fonts were compiled from commit `4eb5f7f`.

**Binary verification**: SHA-256 comparison of `BrunoAceSC-Regular.ttf`:
- Font at `58dc219` in upstream: `58fbd0514d27b4f5...` -- does NOT match google/fonts
- Font at `4eb5f7f` in upstream: `97fc6885b4c03457...` -- MATCHES google/fonts
- Font in google/fonts: `97fc6885b4c03457...`

The same error was introduced by commit `f80b31006` which changed both Bruno Ace and Bruno Ace SC metadata simultaneously.

## How Config YAML Was Resolved

The config file `sources/brunoacesc-regular.yaml` exists at both commits with identical content:
```yaml
sources:
  - BrunoAceSC-Regular.glyphs
buildTTF: true
buildOTF: false
buildStatic: true
buildWebfont: false
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit `58dc219` exists in upstream repo: Yes (but NOT the correct onboarding commit)
- Commit `4eb5f7f` exists in upstream repo: Yes (this IS the correct onboarding commit)
- `4eb5f7f` date: 2023-03-28, message: "Update BrunoAceSC-Regular.ttf"
- Config YAML at both commits: Present and identical
- Font binary match: `4eb5f7f` only
- Packager: Yanone (PR #6073, merged 2023-03-28)

## Confidence

**High** for repository URL. **Low** for the currently recorded commit hash -- binary evidence definitively shows the fonts were built from `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`, not the currently recorded `58dc219db32ffd9eaf573f2dc3be2e342410e15a`. The METADATA.pb commit hash should be corrected to `4eb5f7f`.

## Open Questions

1. Same issue as Bruno Ace: the METADATA.pb commit hash should be corrected from `58dc219` to `4eb5f7f` to match the actual font binaries delivered to google/fonts.
