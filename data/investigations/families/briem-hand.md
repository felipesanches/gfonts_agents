# Investigation Report: Briem Hand

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Briem Hand |
| Designer | Gunnlaugur SE Briem, Eben Sorkin |
| License | OFL |
| Date Added | 2024-03-27 |
| Repository URL | https://github.com/SorkinType/Briem-Hand |
| Commit Hash | `7b991840508c9a90632354034ed0a72002836c05` |
| Branch | main |
| Config YAML | `sources/config.yaml` (in upstream) |
| Status | Complete |

## How URL Found

The repository URL `https://github.com/SorkinType/Briem-Hand` is recorded in the METADATA.pb `source {}` block and matches the copyright string. The repo is owned by SorkinType (Eben Sorkin), who is one of the listed designers.

## How Commit Determined

The commit hash `7b991840508c9a90632354034ed0a72002836c05` was ported from the fontc_crater targets list in google/fonts commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list").

### Complex Onboarding History

This family has a complex history with multiple versions added to google/fonts:

1. **Version 1.003 (first attempt)** - commit `eef42261c` (2024-03-27): upstream commit `3f9aa7c9dab4d104991c127dc7384e6e5d48c0bb`
2. **Version 1.003 (second attempt)** - commit `6df879b16` (2024-03-28): upstream commit `24564101f1b8b5bd66ead0edf82c2bbef0d2ff3a`
3. **Version 1.003 (third attempt)** - commit `2f2518247` (2024-03-28): upstream commit `bd68ecf84950b0c2e975716cce88c1b43b99d138`
4. **Version 1.002** - commit `099159dd0` (2023-11-30): "[gftools-packager] Briem Hand: Version 1.002 added" - upstream commit hash was empty in the message
5. **Fix astroke** - commit `2beab1628` (2024-05-15): by Simon Cozens, rebuilt font
6. **And again** - commit `d619ba521` (2024-05-15): by Simon Cozens, another fix
7. **One more missing join (bf)** - commit `379bcfca1` (2024-05-16): by Simon Cozens, latest font binary change

The METADATA.pb also includes an `archive_url` field pointing to release v1.004: `https://github.com/SorkinType/Briem-Hand/releases/download/v1.004/Briem-Hand-v1.004.zip`

### Analysis of the Recorded Commit

The recorded commit `7b99184` is dated 2024-10-30 ("Missing metrics") in the upstream repo. This is **after** the last font binary change in google/fonts (2024-05-16). The commit was sourced from fontc_crater targets, which may reference a different (more recent) upstream state than what was actually used for the font binaries currently in google/fonts.

The font binary was last modified by Simon Cozens directly on google/fonts (commits 2beab1628, d619ba521, 379bcfca1 in May 2024), suggesting the font may have been rebuilt from sources rather than copied from pre-built upstream binaries.

## Config YAML Status

- `sources/config.yaml` exists in the upstream repository at the recorded commit
- It is correctly referenced in the METADATA.pb `config_yaml` field
- No override config.yaml exists in google/fonts
- The config.yaml is extensive, defining a complex recipe-based build that includes multiple font families (Briem Hand, Briem Hand Guides, Briem Classic) with various weights

## Verification

1. **Commit exists in upstream**: Confirmed. `7b991840508c9a90632354034ed0a72002836c05` exists in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/SorkinType/Briem-Hand`
2. **Commit date**: 2024-10-30, which is after the last font file change in google/fonts (2024-05-16)
3. **Config YAML valid**: `sources/config.yaml` exists at this commit with a recipe-based build from `BriemHand.glyphs`
4. **3 newer commits exist**: The upstream repo has 3 commits after the recorded one (latest: `a346311`)
5. **fontc_crater source**: The commit hash was sourced from fontc_crater targets

## Confidence Level

**MEDIUM** - The repository URL is correct. The commit hash `7b99184` exists and has a valid config.yaml, but it postdates the last font binary update in google/fonts (May 2024 vs October 2024). The fontc_crater target may reference a commit used for CI testing rather than the exact commit that produced the currently deployed binaries. The font was actively modified directly in google/fonts by Simon Cozens (May 2024), which further complicates tracing the exact source state.

## Open Questions

1. Which upstream commit was actually used to build the font binaries currently in google/fonts? The May 2024 Simon Cozens commits suggest direct rebuilds, possibly from a state between the v1.003 commits (March 2024) and the recorded commit (October 2024).
2. The archive_url points to v1.004 - is this the version currently deployed, or should it match a specific upstream commit?
3. Should the commit hash be updated to match the state that actually produced the current binaries, or should it track the fontc_crater target reference?
