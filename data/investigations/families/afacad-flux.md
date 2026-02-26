# Afacad Flux

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Kristian Moller, Dicotype
**METADATA.pb path**: `ofl/afacadflux/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Dicotype/Afacad |
| Commit | `b294b1f8610ff16a3846a255b1a6a2e6788a056e` |
| Config YAML | `sources/config_flux.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb source block when the font was first onboarded. The onboarding commit `ef30d6c3` (2024-07-05) stated: "Taken from the upstream repo https://github.com/Dicotype/Afacad at commit 4655a472cef57467e1604ce80336ab87ea72facc." The copyright field in the font binary also references this same GitHub URL. This is the shared repository for all Afacad variants (Afacad, Afacad Flux).

## How the Commit Hash Was Identified

The commit hash has a notable history with multiple updates:

1. **Original onboarding** (google/fonts commit `ef30d6c3`, 2024-07-05): The font was taken from upstream commit `4655a472cef57467e1604ce80336ab87ea72facc`. This commit no longer exists in the upstream repository, likely due to a force-push or rebase of the main branch.

2. **Batch port from fontc_crater** (google/fonts commit `19cdcec59`, 2025-03-31): The commit hash was updated from `4655a472` to `b294b1f8610ff16a3846a255b1a6a2e6788a056e`, based on fontc_crater's target.json data (from fontc_crater commit `ee7a65d4`). This commit is the current HEAD of the upstream repo.

3. **PR #7851** (google/fonts commit `187711d44`, 2025-05-22): This PR's body referenced yet another commit `a3d77cea32b6f29801c5c1771fbad276d817c97a` (also not found in the upstream repo), but the PR only changed the `config_yaml` field -- it did not modify the commit hash.

The current METADATA.pb commit `b294b1f8` is from 2024-10-03 ("Update README.md") and is the latest commit in the upstream repo. It is NOT the original onboarding commit; it came from fontc_crater data. The original onboarding commit `4655a472` is no longer verifiable.

## How Config YAML Was Resolved

The config YAML path `sources/config_flux.yaml` was set by PR #7851 (google/fonts commit `187711d44`, 2025-05-22). Previously, the batch port commit `19cdcec59` had incorrectly set it to `sources/config.yaml`, which is the config for the main Afacad family, not Afacad Flux. The Afacad upstream repo contains two config files:

- `sources/config.yaml` -- for the main Afacad family
- `sources/config_flux.yaml` -- for Afacad Flux, referencing `AfacadFlux.glyphs` as its source

The `config_flux.yaml` file specifies `familyName: Afacad Flux` and includes axis ordering for slnt and wght. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is HEAD of the shallow clone)
- Commit date: 2024-10-03 10:40:24 +0200
- Commit message: "Update README.md"
- Source files at commit:
  - `sources/AfacadFlux.glyphs`
  - `sources/Afacad.glyphs`
  - `sources/Afacad-Italic.glyphs`
  - `sources/config.yaml`
  - `sources/config_flux.yaml`
  - Multiple `sources/instance_ufos/*.ufo.json` files

## Confidence

**Medium**: The repository URL and config_yaml path are well-established and verified. However, the commit hash `b294b1f8` is NOT the original onboarding commit -- it is the latest HEAD from fontc_crater data, dated 2024-10-03, which is three months after the original onboarding on 2024-07-05. The commit "Update README.md" is unlikely to have changed font source files, but the original onboarding commit `4655a472` cannot be recovered to verify this. Since the upstream repo is shallow-cloned (depth 1), full history verification is not possible without unshallowing.

## Open Questions

1. Why was the original onboarding commit `4655a472` lost from the upstream repo? Was the repo force-pushed or rebased?
2. Were any source changes made between the original onboarding (2024-07-05) and the current METADATA.pb commit (2024-10-03) that would affect the built font, or were the only changes to documentation files like README.md?
3. Should the commit hash be considered "good enough" given that the original cannot be recovered?
