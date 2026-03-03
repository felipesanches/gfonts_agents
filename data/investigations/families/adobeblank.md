# Adobe Blank

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: missing_config
**Designer**: Dr. Ken Lunde
**METADATA.pb path**: `ofl/adobeblank/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/adobe-fonts/adobe-blank |
| Commit | `19279e6f6707408fd93091d157b7836259bcbd21` |
| Config YAML | -- |
| Branch | -- |

## How the Repository URL Was Found

The repository URL `https://github.com/adobe-fonts/adobe-blank` is already present in the METADATA.pb `source { }` block (added in google/fonts commit `3ee943a94` on 2026-02-26). The `adobe-fonts` GitHub organization is Adobe's official home for open-source fonts, and this URL matches the font's copyright notice ("Copyright 2013, 2015 Adobe Systems Incorporated"). The repository is publicly accessible.

The font was originally onboarded to google/fonts by Dave Crossland in commit `54875d8a8` (2016-03-21, "Adding Adobe Blank") with no PR reference or upstream commit recorded.

## How the Commit Hash Was Identified

The upstream repository contains exactly **one commit**:

- `19279e6f6707408fd93091d157b7836259bcbd21` (2019-12-03, by danrhatigan): "Update README.md"

Since this is the only commit in the repository, it is trivially the only possible reference. However, several anomalies are worth noting:

1. **Date mismatch**: The commit date (2019-12-03) is more than 3 years after the font was added to google/fonts (2016-03-21). This strongly suggests the repository was force-pushed or recreated at some point, erasing the original history.

2. **File size discrepancy**: The upstream `AdobeBlank.ttf` is 72,384 bytes, while the google/fonts `AdobeBlank-Regular.ttf` is 72,408 bytes (24 bytes larger). The SHA-256 hashes differ. The google/fonts TTF has never been modified since its initial onboarding commit `54875d8a8`. The size difference is likely due to the file being renamed from `AdobeBlank.ttf` to `AdobeBlank-Regular.ttf` with corresponding name table updates during onboarding, or the original repo having a slightly different version at the time of onboarding (before the repo was rewritten).

3. **Single-commit repo**: The commit stat shows all 16 files being added (all insertions, no modifications), confirming this was a fresh repo initialization, not an incremental update.

Despite these anomalies, `19279e6` is the only commit available and therefore the only valid reference.

## How Config YAML Was Resolved

**No config.yaml exists and none can be created.** Adobe Blank uses a completely non-standard build process incompatible with gftools-builder:

The font is built using **AFDKO's `makeotf`** with CID-keyed PostScript sources. The build process is documented in `COMMANDS.txt`:

```
makeotf -f cidfont.ps -omitMacNames -ff features -fi cidfontinfo -mf FontMenuNameDB -r -stubCmap4 -ch UnicodeAll-UTF32-H
sfntedit -d VORG,vhea,vmtx AdobeBlank.otf
sfntedit -a DSIG=DSIG.bin AdobeBlank.otf
```

Source files in the repository:
- `cidfont.ps` -- CID-keyed PostScript font data (binary, 24,200 bytes)
- `features` -- OpenType feature file
- `cidfontinfo` -- CID font metadata
- `FontMenuNameDB` -- Font menu name database
- `UnicodeAll-UTF32-H` -- Unicode CMap (4,550 lines)
- `DSIG.bin` -- Digital signature stub

The repo also contains pre-built binaries: `AdobeBlank.otf`, `AdobeBlank.ttf`, `AdobeBlank.eot`, and `.woff` files.

There are **no** `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files anywhere in the repository. The CID-keyed PostScript workflow is fundamentally incompatible with gftools-builder, so no override `config.yaml` can be created. No local override config exists in the google/fonts family directory either.

## Verification

| Check | Result |
|-------|--------|
| Commit exists in upstream repo | Yes |
| Commit date | 2019-12-03 12:28:22 -0500 |
| Commit message | "Update README.md" |
| Commit author | danrhatigan |
| Total commits in repo | 1 (entire repo created in a single commit) |
| TTF in upstream | `AdobeBlank.ttf` (72,384 bytes) |
| TTF in google/fonts | `AdobeBlank-Regular.ttf` (72,408 bytes) |
| TTF modified since onboarding | No (unchanged since `54875d8a8`, 2016-03-21) |
| Source file types | CID-keyed PostScript (not gftools-compatible) |
| config.yaml in upstream | None |
| config.yaml override in google/fonts | None |

## Conclusion

**Confidence: MEDIUM**

The repository URL is confirmed valid and is the canonical source for Adobe Blank under Adobe's official `adobe-fonts` GitHub organization. The commit hash `19279e6f` is unambiguous since it is the only commit in the repository. However, the repository was clearly rewritten after the font was onboarded to google/fonts (the sole commit dates to 2019, while onboarding occurred in 2016), so the original onboarding state cannot be verified from current git history.

The status is `missing_config` because the font uses a CID-keyed PostScript build workflow (AFDKO `makeotf`) that is fundamentally incompatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` sources from which a `config.yaml` could be constructed. This font will likely need to remain outside the standard gftools-builder pipeline permanently.
