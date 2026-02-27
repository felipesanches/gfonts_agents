# Investigation: Aguafina Script

## Summary

| Field | Value |
|-------|-------|
| Family Name | Aguafina Script |
| Slug | aguafina-script |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/aguafinascript |
| Commit Hash | 45a8ce768b4cca138c10ff7a7a9f55778fd02c9d |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/aguafinascript"
  commit: "45a8ce768b4cca138c10ff7a7a9f55778fd02c9d"
}
```

## Investigation

**Git history for TTF files in google/fonts:**
- `1e499f173` — "Updating ofl/aguafinascript/*ttf with nbspace and fsType fixes" (2015-04-27)
- `90abd17b4` — "Initial commit" (2015-03-07, bulk import)

There are no PR-linked commits that reference an upstream URL or commit hash. The font was added in the early bulk import era.

**Upstream repo (librefonts/aguafinascript):**
The repo is cached at `librefonts/aguafinascript`. It is a shallow clone with a single visible commit:
- Commit `45a8ce768b4cca138c10ff7a7a9f55778fd02c9d`
- Date: 2014-10-17 13:27:47 +0300
- Message: "update .travis.yml"

The `librefonts` GitHub organization is a known archive of early Google Fonts sources migrated from legacy infrastructure.

**Source files in upstream repo:**
```
src/AguafinaScript-Regular-TTF.sfd   (FontForge SFD format)
src/Aguafina-Regular-OTF.vfb         (FontLab VFB format, binary)
src/Aguafina-Regular.otf.*ttx        (TTX table dumps)
AguafinaScript-Regular.ttf.*ttx     (TTX table dumps)
DESCRIPTION.en_us.html
METADATA.json
OFL.txt
```

**Config YAML:**
No `config.yaml` exists in the upstream repo, and no override `config.yaml` is present in the google/fonts family directory (`ofl/aguafinascript/`). The available source formats (SFD and VFB) are legacy formats incompatible with gftools-builder, which requires `.glyphs`, `.glyphspackage`, `.ufo`, or `.designspace` files. Building from these sources would require converting them to a modern format first.

**METADATA.pb source block status:**
As of 2026-02-26, a source block was added to METADATA.pb (google/fonts commit `9f12d509e`, authored by Felipe Correa da Silva Sanches) with the repository_url and commit fields. No config_yaml field was set because the sources are SFD/VFB only.

**Font authorship:**
The font was originally designed by Angel Koziupa and Alejandro Paul of Sudtipos (a commercial type foundry). The `librefonts` repo is a mirror/archive rather than an authoritative source. The copyright notes a reserved font name "Aguafina Script". The original Sudtipos sources (likely FontLab VFB) may not be publicly available in a more modern form.

## Conclusion

Status is `no_config_possible` because the upstream repo contains only legacy source formats (SFD and VFB) that are not compatible with gftools-builder. A config.yaml cannot be created without first converting the sources to a modern format (.glyphs, .ufo, or .designspace). The repository_url and commit are already documented in METADATA.pb. No further action is required unless someone undertakes a source conversion effort for this legacy font.
