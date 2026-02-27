# Investigation: Adobe Blank

## Summary

| Field | Value |
|-------|-------|
| Family Name | Adobe Blank |
| Slug | adobe-blank |
| License Dir | ofl |
| Repository URL | https://github.com/adobe-fonts/adobe-blank |
| Commit Hash | 19279e6f6707408fd93091d157b7836259bcbd21 |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/adobe-fonts/adobe-blank"
  commit: "19279e6f6707408fd93091d157b7836259bcbd21"
}
```

## Investigation

### Git History

The TTF files in `ofl/adobeblank/` have one commit in google/fonts:

```
54875d8a8 Adding Adobe Blank
```

The commit `54875d8a8` (dated 2016-03-21) has a simple commit message with no PR reference or upstream commit hash recorded. This was added by Dave Crossland before gftools-packager was adopted.

### Upstream Repository

The upstream repo is cloned at `upstream_repos/fontc_crater_cache/adobe-fonts/adobe-blank/`. The repo contains only a single commit:

- `19279e6f6707408fd93091d157b7836259bcbd21` (2019-12-03): "Update README.md"

This is the sole commit in the repository. The commit post-dates the font's addition to google/fonts (2016-03-21) by over 3 years, indicating the upstream repo was likely force-pushed or recreated at some point. The original git history at the time of onboarding is not recoverable.

### Source File Analysis

The upstream repo contains:
- `cidfont.ps` — CID-keyed PostScript font data
- `features` — OpenType feature file
- `cidfontinfo` — CID font metadata
- `FontMenuNameDB` — Font menu name database
- `UnicodeAll-UTF32-H` — Unicode CMap
- `DSIG.bin` — Digital signature binary
- `COMMANDS.txt` — Build instructions
- Pre-built binaries: `AdobeBlank.otf`, `AdobeBlank.ttf`, `AdobeBlank.eot`, `.woff` files

The `COMMANDS.txt` documents the build process using AFDKO's `makeotf` tool:
```
makeotf -f cidfont.ps -omitMacNames -ff features -fi cidfontinfo -mf FontMenuNameDB -r -stubCmap4 -ch UnicodeAll-UTF32-H
sfntedit -d VORG,vhea,vmtx AdobeBlank.otf
sfntedit -a DSIG=DSIG.bin AdobeBlank.otf
```

There are **no** `.glyphs`, `.ufo`, or `.designspace` files. Adobe Blank uses a specialized CID-keyed PostScript workflow incompatible with gftools-builder. No override `config.yaml` exists in `ofl/adobeblank/` in google/fonts.

### Repository URL Identification

The METADATA.pb source block was added retroactively (after the initial 2016 addition). The `adobe-fonts` GitHub organization is Adobe's official repository for open-source fonts, and `adobe-fonts/adobe-blank` is the obvious canonical source for this font. The repository URL is confirmed as `https://github.com/adobe-fonts/adobe-blank`.

## Conclusion

The METADATA.pb `source {}` block has repository_url and commit set. No `config_yaml` can be added because the upstream repo uses a CID-keyed PostScript build process (AFDKO `makeotf`) that is incompatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` sources available. Status is `no_config_possible`. Additionally, the recorded commit (2019-12-03) post-dates the font's addition to google/fonts (2016-03-21), meaning the actual onboarding commit cannot be verified from available git history. No further action needed for the metadata documentation effort unless Adobe provides modern sources.
