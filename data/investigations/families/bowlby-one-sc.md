# Investigation: Bowlby One SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bowlby One SC |
| Slug | bowlby-one-sc |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bowlbyonesc |
| Commit Hash | 9566646d9feaafcdc1c23174931ac4599803442b |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bowlbyonesc"
  commit: "9566646d9feaafcdc1c23174931ac4599803442b"
}
```

## Investigation

Bowlby One SC is a display typeface by Vernon Adams, added to Google Fonts on 2011-07-06. It is an archival font with no active upstream development since 2014.

### Git History

The font TTF was last updated in google/fonts commit `c6a838cef` (2015-04-27, "Updating ofl/bowlbyonesc/*ttf with nbspace and fsType fixes" by Dave Crossland). The initial commit was `90abd17b4`.

The source block was added by google/fonts commit `bb0ae5d66` ("Bowlby One SC: add source block to METADATA.pb"), which documented:
- Repo: librefonts/bowlbyonesc
- Commit: 9566646d
- Config: override config.yaml in google/fonts
- Status: complete
- Confidence: MEDIUM

### Upstream Repository

The repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/bowlbyonesc/`. The repository has only 12 commits, all from 2014. Commit `9566646d` is the tip of master (2014-10-17, "update .travis.yml").

The upstream repo contains a mix of source formats:
- `src/BowlbyOneSC-Regular.sfd` (FontForge format)
- `src/BowlbyOneSC-Regular-TTF.vfb` (FontLab format)
- `src/BowlbyOneSC-Regular.ufo` (UFO format — gftools-builder compatible)
- `src/BowlbyOneSC-TThints.vfb` (FontLab hinting file)

The presence of a UFO source enables building with gftools-builder.

### Override config.yaml

An override `config.yaml` was added to `/mnt/shared/google/fonts/ofl/bowlbyonesc/config.yaml` as part of the source block commit (`bb0ae5d66`). Contents:

```yaml
sources:
  - src/BowlbyOneSC-Regular.ufo
buildVariable: false
```

This override enables gftools-builder to compile the font from the upstream UFO source. The `config_yaml` field is omitted from METADATA.pb because google-fonts-sources auto-detects local override config.yaml files.

### Verification

- Repository URL: Confirmed — `librefonts/bowlbyonesc` is accessible on GitHub
- Commit hash: Confirmed — `9566646d` is the tip of master (2014-10-17, "update .travis.yml")
- Override config.yaml: Present at `ofl/bowlbyonesc/config.yaml` in google/fonts
- UFO source: `src/BowlbyOneSC-Regular.ufo` exists at the recorded commit
- Note: The UFO source dates from 2014; building from it may not perfectly replicate the 2015 nbspace/fsType-fixed binary

## Conclusion

The METADATA.pb source block is complete with repository URL and commit hash correctly set. An override `config.yaml` exists in the google/fonts family directory, enabling gftools-builder to compile from the UFO source. The `config_yaml` field is intentionally omitted from METADATA.pb as the google-fonts-sources tool auto-detects the local override. No additional action needed, though testing the build output against the current binary would confirm whether the UFO source matches the 2015-modified binary.
