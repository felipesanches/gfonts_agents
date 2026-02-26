# Bruno Ace

**Date investigated**: 2026-02-26
**Status**: complete (with commit hash concern)
**Designer**: Astigmatic
**METADATA.pb path**: `ofl/brunoace/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/Bruno-ace |
| Commit (recorded) | `58dc219db32ffd9eaf573f2dc3be2e342410e15a` |
| Commit (actual build) | `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181` |
| Config YAML | `sources/brunoace-regular.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/Bruno-ace` is recorded in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font ("Copyright 2023 The Bruno Ace Project Authors (https://github.com/googlefonts/Bruno-ace)"). The gftools-packager commit `3169bfdfe` in google/fonts and PR #6072 both reference this URL.

## How the Commit Hash Was Identified

The METADATA.pb currently records commit `58dc219db32ffd9eaf573f2dc3be2e342410e15a`. However, binary comparison reveals this is **incorrect**:

- The gftools-packager commit `3169bfdfe` in google/fonts states: "Bruno Ace Version 1.100 taken from the upstream repo [...] at commit [...]/4eb5f7fc38a1548b353b4ee03b1f7043b48ae181."
- PR #6072 body references commit `58dc219` (which was the state of the repo when the PR was initially created).
- During the PR process, Yanone updated the upstream repo with 6 additional commits (adding missing glyphs, removing softhyphen, updating compiled fonts), culminating in `4eb5f7f`.
- The squash-merged commit in google/fonts correctly records `4eb5f7f` as the commit from which the fonts were actually taken.

**Binary verification**: SHA-256 comparison of `BrunoAce-Regular.ttf`:
- Font at `58dc219` in upstream: `2f882bb0568e2aab...` -- does NOT match google/fonts
- Font at `4eb5f7f` in upstream: `2ebb34cae30afcb6...` -- MATCHES google/fonts
- Font in google/fonts: `2ebb34cae30afcb6...`

The METADATA.pb was updated by commit `f80b31006` ("sources info for Bruno Ace (incl. SC)", 2025-04-02) which changed the commit from `4eb5f7f` to `58dc219` and added the `config_yaml` field. This change appears to have been based on the PR body text rather than the actual squash-merge commit message, introducing an error.

## How Config YAML Was Resolved

The config file `sources/brunoace-regular.yaml` exists at both commit `58dc219` and `4eb5f7f` in the upstream repo with identical content:
```yaml
sources:
  - BrunoAce-Regular.glyphs
buildTTF: true
buildOTF: false
buildStatic: true
buildWebfont: false
```

Note: The latest commit in the repo (`b6fea3b`) renamed the YAML files, but the files existed with the correct names at both relevant commits. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit `58dc219` exists in upstream repo: Yes (but is NOT the correct onboarding commit)
- Commit `4eb5f7f` exists in upstream repo: Yes (this IS the correct onboarding commit)
- `58dc219` date: 2023-03-23, message: "Update README.md" -- only a README change
- `4eb5f7f` date: 2023-03-28, message: "Update BrunoAceSC-Regular.ttf" -- compiled font update
- Config YAML at both commits: Present and identical
- Font binary match: `4eb5f7f` only
- Packager: Yanone (PR #6072, merged 2023-03-28)

## Confidence

**High** for repository URL. **Low** for the currently recorded commit hash -- binary evidence definitively shows the fonts were built from `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`, not the currently recorded `58dc219db32ffd9eaf573f2dc3be2e342410e15a`. The METADATA.pb commit hash should be corrected to `4eb5f7f`.

## Open Questions

1. The METADATA.pb commit hash should be corrected from `58dc219` to `4eb5f7f` to match the actual font binaries. This was likely an error introduced in commit `f80b31006` which used the PR body text (initial state) rather than the squash-merge commit message (final state).
