# Bungee Hairline

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: David Jonathan Ross
**METADATA.pb path**: `ofl/bungeehairline/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/djrrb/Bungee |
| Commit | `eb03cf69adab5094f6b84e95357789cdf3bfeb99` |
| Config YAML | Override in google/fonts (`ofl/bungeehairline/config.yaml`) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/djrrb/Bungee` is documented in the METADATA.pb `source { repository_url }` field. It is the same upstream repository used by all Bungee variants. It was referenced in the google/fonts commit `93c3a3d13` ("Bungee Hairline: Version 2.000 added"): "Taken from the upstream repo https://github.com/djrrb/Bungee". The METADATA.pb also includes a minisite URL at `https://djr.com/bungee`.

## How the Commit Hash Was Identified

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` is explicitly referenced in the google/fonts commit `93c3a3d13` ("Bungee Hairline: Version 2.000 added"): "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99."

This is the same commit hash used for the regular Bungee family (commit `6bc4f73e2`), which makes sense since both were updated as part of the v2.000 release. The commit exists in the upstream repo with date 2024-05-30 and message "Bump fontbakery".

The METADATA.pb also references a release archive URL: `https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip`, indicating the binary was taken from the v2.000 release ZIP.

## How Config YAML Was Resolved

The upstream repository does not contain a `config.yaml` file. An override `config.yaml` was created in the google/fonts family directory (`ofl/bungeehairline/config.yaml`) as part of commit `f6c68379a` ("Add override config.yaml for 50 font families"). The override config contains:

```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Hairline.ufo
familyName: Bungee Hairline
buildStatic: true
buildOTF: false
```

The source file `sources/2-build/Bungee_Basic/Bungee-Hairline.ufo` was verified to exist at the recorded commit `eb03cf69`. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2024-05-30 07:17:37 +0200
- Commit message: "Bump fontbakery"
- Source files at commit: `sources/2-build/Bungee_Basic/Bungee-Hairline.ufo` (verified)
- Font binary in google/fonts: `BungeeHairline-Regular.ttf` (static)
- Binary taken from release archive: `Bungee-fonts.zip` (v2.000 release)
- Font originally added to Google Fonts: 2016-06-20
- Version 2.000 update: google/fonts commit `93c3a3d13`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts commit message that brought in the v2.000 update. This is the same commit used for the regular Bungee family, consistent with both being part of the same v2.000 release. The commit exists in the upstream repo and the source files are present. The override config.yaml correctly points to the source file at the recorded commit.

## Open Questions

None. All data is well-documented and verified. The Bungee Hairline family shares the same upstream repo and commit hash as the regular Bungee family, both updated as part of the v2.000 release.
