# Investigation: Advent Pro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Advent Pro |
| Slug | advent-pro |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/Advent |
| Commit Hash | d206a139ee9045993fbd1e530b93f28f8bf4e3b1 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/Advent"
  commit: "d206a139ee9045993fbd1e530b93f28f8bf4e3b1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/split/AdventPro[wdth,wght].ttf"
    dest_file: "AdventPro[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/split/AdventPro-Italic[wdth,wght].ttf"
    dest_file: "AdventPro-Italic[wdth,wght].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

**Git history for TTF files in google/fonts:**
- `ce1042736` — "Advent Pro: Version 3.000 added (#5522)" — this is the last TTF update
- Earlier commits: #1210 (OTS fix), #1124 (QU kerning fix), #745 (v2.004), plus legacy bulk imports

**Onboarding commit corroboration:**
The google/fonts commit `ce1042736` (merged 2022-12-01, PR #5522) contains the message:
> "Advent Pro Version 3.000 taken from the upstream repo https://github.com/googlefonts/Advent at commit https://github.com/googlefonts/Advent/commit/d206a139ee9045993fbd1e530b93f28f8bf4e3b1."

The commit hash `d206a139` in METADATA.pb matches exactly what is stated in the packager commit message. The PR body initially referenced a different commit (`036dd5878f3b92c39fd74def865e6b2755bba8ba`) — that was the initial packager run — but the final merged version uses `d206a139`, which is corroborated by the squashed commit body in google/fonts.

**Upstream repo (googlefonts/Advent) at recorded commit:**
- Commit `d206a139ee9045993fbd1e530b93f28f8bf4e3b1` exists in the local cache
- Date: 2022-11-25 16:46:12 +0100
- Message: "Latest binaries"
- Source files present: `sources/config.yaml`, `font_source/UFOs/latest/*.designspace`, multiple `.ufo` directories

**Config YAML:**
`sources/config.yaml` exists in the upstream repo at the recorded commit:
```yaml
sources:
  - AdventPro.designspace
axisOrder:
  - wdth
  - wght
  - ital
familyName: Advent Pro
buildOTF: false
buildTTF: true
buildWebfont: false
buildStatic: false
buildVariable: true
```
This is a valid gftools-builder configuration referencing a `.designspace` source. The `config_yaml: "sources/config.yaml"` field in METADATA.pb is correct.

## Conclusion

No action needed. All three key fields (repository_url, commit, config_yaml) are present and verified. The commit hash is corroborated by the gftools-packager message in the google/fonts commit for PR #5522. The config.yaml exists at the recorded commit and is a valid gftools-builder configuration.
