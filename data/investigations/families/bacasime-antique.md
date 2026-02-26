# Bacasime Antique

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: The DocRepair Project, Claus Eggers Sorensen
**METADATA.pb path**: `ofl/bacasimeantique/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/docrepair-fonts/bacasime-antique-fonts |
| Commit | `673db74ee28486bb370847e062a97a5f94cec2e0` |
| Config YAML | `sources/config.yaml` |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/docrepair-fonts/bacasime-antique-fonts` is documented in the METADATA.pb `source` block and in the font copyright string. The google/fonts commit body also explicitly references this repo. The `docrepair-fonts` organization on GitHub hosts several font projects, and this is a legitimate upstream source.

## How the Commit Hash Was Identified

The commit `673db74ee28486bb370847e062a97a5f94cec2e0` is referenced in the google/fonts commit body (by Yanone, on 2023-06-14): "Bacasime Antique Version 2.000 taken from the upstream repo [...] at commit 673db74ee28486bb370847e062a97a5f94cec2e0."

Cross-verification:
- The upstream commit is dated 2023-06-14 17:50:05 +0200.
- The google/fonts commit is dated 2023-06-14 17:50:31 +0200 -- just 26 seconds later.
- This extremely tight timing (same minute) suggests Yanone committed to both the upstream repo and google/fonts essentially simultaneously, likely as part of a scripted or rapid onboarding process.
- The commit is the HEAD of the upstream repo (only 1 commit visible in the shallow clone, and no newer commits on origin/main).
- The commit was pushed directly to google/fonts (not via a PR).

## How Config YAML Was Resolved

The upstream repo contains `sources/config.yaml` at the referenced commit with the following content:

```yaml
buildOTF: false
buildVariable: false
familyName: Bacasime Antique
outputDir: ../fonts
sources:
  - Bacasime-Antique-Regular.designspace
```

This is a valid gftools-builder configuration. The METADATA.pb correctly records the path as `sources/config.yaml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2023-06-14 17:50:05 +0200
- Commit message: "Merge branch 'main' of https://github.com/docrepair-fonts/bacasime-antique-fonts"
- Commit author: Yanone
- Source files at commit: `sources/Bacasime-Antique-Regular.designspace`, `sources/config.yaml`, `sources/masters/BacasimeAntique-Regular.ufo/`, `fonts/ttf/BacasimeAntique-Regular.ttf`
- Commit is HEAD of upstream main branch: Yes (no newer commits)

## Confidence

**High**: The commit hash is consistently referenced in the google/fonts commit body and METADATA.pb. The near-simultaneous timestamps between upstream and google/fonts commits are consistent with a coordinated onboarding by Yanone. The config.yaml path is verified and the commit is the latest in the upstream repo.

## Open Questions

None. The commit message ("Merge branch 'main' of ...") suggests a typical merge commit from a remote pull, likely part of Yanone's onboarding workflow.
