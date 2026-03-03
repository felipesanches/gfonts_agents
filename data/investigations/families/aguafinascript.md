# Aguafina Script

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: missing_config
**Designer**: Sudtipos
**METADATA.pb path**: `ofl/aguafinascript/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/aguafinascript |
| Commit | `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/aguafinascript` is already recorded in the METADATA.pb source block (added in google/fonts commit `9f12d509e`, 2026-02-26). The `librefonts` GitHub organization is a known archive of legacy Google Fonts source repositories. The repo is cached locally at `librefonts/aguafinascript`.

## How the Commit Hash Was Identified

The commit `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d` is recorded in the METADATA.pb source block. It is the HEAD of the upstream repository's `master` branch. The local cache is a shallow clone, so only this one commit is available, but it is the latest (and possibly only) commit in the repository.

**Commit details**:
- Date: 2014-10-17 13:27:47 +0300
- Author: hash3g (hash.3g@gmail.com)
- Message: "update .travis.yml"

**Timeline verification**:
- Font added to Google Fonts: 2011-11-30 (per `date_added` in METADATA.pb)
- Initial bulk import to google/fonts repo: 2015-03-07 (commit `90abd17b4`)
- Last TTF modification in google/fonts: 2015-04-27 (commit `1e499f173`, "Updating ofl/aguafinascript/*ttf with nbspace and fsType fixes" by Dave Crossland)
- Upstream commit: 2014-10-17 -- predates the google/fonts import

The upstream commit predates the google/fonts initial import, which is consistent with it being the state of the source at the time of onboarding.

## How Config YAML Was Resolved

There is **no config.yaml** in the upstream repository and **no override config.yaml** in the google/fonts family directory.

The upstream repo contains only legacy source formats that are incompatible with gftools-builder:
- `src/AguafinaScript-Regular-TTF.sfd` -- FontForge SFD format
- `src/Aguafina-Regular-OTF.vfb` -- FontLab VFB binary format

gftools-builder requires `.glyphs`, `.glyphspackage`, `.ufo`, or `.designspace` source files. Neither SFD nor VFB are supported. The repo also contains TTX table dumps of the compiled font, which are decompiled binary representations rather than editable design sources.

An override config.yaml cannot be created without first converting the sources to a supported format.

## Verification

- **Repository URL valid**: Yes (remote URL matches `https://github.com/librefonts/aguafinascript`)
- **Commit exists in upstream**: Yes (it is HEAD of the shallow clone)
- **Source files at commit**:
  - `src/AguafinaScript-Regular-TTF.sfd` (FontForge SFD)
  - `src/Aguafina-Regular-OTF.vfb` (FontLab VFB binary)
  - Multiple TTX table dumps of the compiled TTF and OTF
  - `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- **Config YAML**: Not present anywhere
- **Source block already in METADATA.pb**: Yes (added in commit `9f12d509e`)

## Conclusion

**Confidence: MEDIUM**

The source block in METADATA.pb correctly points to `https://github.com/librefonts/aguafinascript` at commit `45a8ce76`. The repository is a legacy archive under the `librefonts` organization containing SFD and VFB source files -- neither of which is compatible with gftools-builder. No config.yaml can be created without a source format conversion (e.g., SFD to UFO). The font is effectively in a "legacy binary only" state for build purposes.

The original designer is Sudtipos (Angel Koziupa and Alejandro Paul), a commercial type foundry. The librefonts repo is a mirror/archive rather than the original development repository, so more authoritative sources are unlikely to be publicly available.

## Open Questions

1. Could the SFD source be converted to UFO format to enable gftools-builder compatibility, or should this font remain in its current "legacy binary" state?
2. Is there a more authoritative upstream source from Sudtipos that might contain modern-format sources?
