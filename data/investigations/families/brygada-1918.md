# Brygada 1918

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Capitalics, Mateusz Machalski, Borys Kosmynka, Ania Wielunska, Przemyslaw Hoffer
**METADATA.pb path**: `ofl/brygada1918/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/kosmynkab/Brygada-1918 |
| Commit | `8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/kosmynkab/Brygada-1918` is recorded in the METADATA.pb `source { repository_url }` field and matches the copyright string ("Copyright 2020 The Brygada 1918 Project Authors (https://github.com/kosmynkab/Brygada-1918)"). The gftools-packager commit in PR #3252 also references this URL. The repo owner `kosmynkab` corresponds to Borys Kosmynka, one of the project designers.

## How the Commit Hash Was Identified

The METADATA.pb records commit `8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b`. This is the **only commit** in the entire upstream repository (message: "Generated version 3.006", by Rosalie Wagner, 2021-03-24).

The gftools-packager commit for the latest update in google/fonts (PR #3252, commit `4714790f8`, 2021-03-24) explicitly states: "Brygada 1918 Version 3.006 taken from the upstream repo [...] at commit [...]/8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b." This is a direct match.

The source block was added by commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

**Binary verification**: SHA-256 comparison of `Brygada1918[wght].ttf`:
- Font at `8325dc3` in upstream: `93a23e7c6de5e2c5...` -- MATCHES google/fonts
- Font in google/fonts: `93a23e7c6de5e2c5...`

## How Config YAML Was Resolved

The config file `sources/config.yaml` exists at the recorded commit `8325dc3` with the following content:
```yaml
sources:
  - Brygada1918.glyphs
  - Brygada1918-Italic.glyphs
axisOrder:
  - wght
familyName: Brygada 1918
```

This is a valid gftools-builder configuration for a variable font family with roman and italic sources. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2021-03-24 12:55:22 +0100
- Commit message: "Generated version 3.006"
- Commit author: Rosalie Wagner
- Source files at commit: `sources/Brygada1918.glyphs`, `sources/Brygada1918-Italic.glyphs`, `sources/config.yaml`
- Font binary match: Confirmed
- Packager: Rosalie Wagner (PR #3252, merged 2021-03-24)
- Font update history in google/fonts: v3.004 (PR #2978), v3.005 (PR #3095), v3.006 (PR #3252)

## Confidence

**High**: The commit hash matches exactly between the gftools-packager commit message, METADATA.pb, and binary verification. The upstream repo has only one commit, making this unambiguous. The config.yaml is present and valid.

## Open Questions

None. All data is consistent and verified.
