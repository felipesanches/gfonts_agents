# Bungee Color

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungeecolor/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | `bb29250eb071b59c4e48f44cf146943e2aafae61` |
| Config YAML | Override in google/fonts (`ofl/bungeecolor/config.yaml`) |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` is documented in the METADATA.pb `source { repository_url }` field. This is the same upstream repository used by all Bungee variants (Bungee, Bungee Color, Bungee Hairline, Bungee Inline, Bungee Outline, Bungee Shade, Bungee Spice, Bungee Tint). It was added by Cosimo Lupo (anthrotype) as part of PR #5137 ("Revert BungeeColor-Regular.ttf to COLRv0 only", 2022-08-26).

## How the Commit Hash Was Identified

The commit `bb29250eb071b59c4e48f44cf146943e2aafae61` was set in the METADATA.pb source block by Cosimo Lupo in PR #5137 (commit `e9ba362c8`, 2022-08-26). The PR body states: "replaced the current BungeeColor-Regular.ttf with the upstream one found on djrrb/Bungee repository" and links to `https://github.com/djrrb/Bungee/blob/a8a8a21/fonts/Bungee_Color_Fonts/COLRv0/BungeeColor-Regular_COLRv0.ttf`.

The PR references commit `a8a8a21` for the actual binary file, but the METADATA.pb records `bb29250e`. Analysis shows:
- `a8a8a215` (2022-05-25, "multi-palette COLR/CPAL font") is an ancestor of `bb29250e`
- `bb29250e` (2022-08-16, "SBIX font doesn't work, isn't needed anymore") came 3 months later
- The COLRv0 binary file (`BungeeColor-Regular_COLRv0.ttf`) is **identical** at both commits (verified via SHA-256 comparison)

So `bb29250e` was likely the HEAD of the relevant branch when Cosimo prepared the PR, and the binary was unchanged between the two commits. The recorded hash is a valid (though not minimal) reference.

### Bungee Color History in google/fonts

Bungee Color had a complex history in google/fonts:
1. 2021-12-01: Initial "exploratory addition" (PR #4128, by Rod Sheeter/rsheeter)
2. Multiple iterations with maximum_color tool to add SVG/CBDT color tables
3. 2022-08-26: Reverted to COLRv0-only (PR #5137, by Cosimo Lupo/anthrotype) - this is the current state

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file. An override `config.yaml` was created in the google/fonts family directory (`ofl/bungeecolor/config.yaml`) as part of commit `f6c68379a` ("Add override config.yaml for 50 font families"). The override config contains:

```yaml
sources:
  - sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo
familyName: Bungee Color
buildStatic: true
buildOTF: false
```

The source file `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` was verified to exist at the recorded commit `bb29250e`. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2022-08-16 12:34:24 -0400
- Commit message: "SBIX font doesn't work, isn't needed anymore"
- Source files at commit: `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` (verified)
- Binary file at commit: `fonts/Bungee_Color_Fonts/COLRv0/BungeeColor-Regular_COLRv0.ttf` (verified)
- Font binary in google/fonts: `BungeeColor-Regular.ttf` (COLRv0 color font)
- Font added to Google Fonts: 2022-04-05 (date_added in METADATA.pb)

## Confidence

**High**: The commit hash exists in the upstream repo and the binary file was verified to be identical between the PR-referenced commit (`a8a8a21`) and the METADATA.pb-recorded commit (`bb29250e`). The source block was added by Cosimo Lupo in the same PR that updated the binary, providing strong provenance. The override config.yaml correctly references the source file at the recorded commit.

## Open Questions

1. The METADATA.pb records commit `bb29250e` while the PR body references commit `a8a8a21` for the actual binary. Both produce identical COLRv0 font files, so this is not a functional discrepancy, but it means the recorded commit is not the minimal exact commit the binary was sourced from.
