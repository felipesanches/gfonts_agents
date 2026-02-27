# Investigation: Cabin Sketch

## Summary

| Field | Value |
|-------|-------|
| Family Name | Cabin Sketch |
| Slug | cabin-sketch |
| License Dir | ofl |
| Repository URL | https://github.com/impallari/CabinSketch |
| Commit Hash | f74674fd7ba37fdfcdad88b58d8d3983a320a68d |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/impallari/CabinSketch"
  commit: "f74674fd7ba37fdfcdad88b58d8d3983a320a68d"
}
```

## Investigation

The repository URL `https://github.com/impallari/CabinSketch` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)", 2024-01-14). The URL matches the impallari GitHub account, which belongs to Pablo Impallari, the designer behind Impallari Type.

The commit hash `f74674fd7ba37fdfcdad88b58d8d3983a320a68d` was added in google/fonts commit `3bb35f256` ("Cabin Sketch: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit message notes: "Config: override config.yaml in google/fonts, Status: complete, Confidence: HIGH".

The commit `f74674fd` is HEAD of the upstream repository's master branch (message: "FONTLOG: updated", Marc Foley, 2016-11-10). The timeline is consistent:
- Upstream commit `f74674f` was made on 2016-11-10
- PR #459 was submitted and merged on 2016-12-05, adding v1.100 to google/fonts
- No further commits were made to the upstream repo after this

The upstream repo is cached at `upstream_repos/fontc_crater_cache/impallari/CabinSketch/`. The commit exists in the repo and the upstream contains `fonts/CabinSketch-Bold.ttf` and `fonts/CabinSketch-Regular.ttf` matching the files in google/fonts.

The upstream repository does not contain a `config.yaml`. An override `config.yaml` was created in the google/fonts family directory (`ofl/cabinsketch/config.yaml`) by Felipe Sanches in commit `3bb35f256`. Contents:

```yaml
sources:
  - sources/CabinSketch.glyphs
buildVariable: false
```

The source file `sources/CabinSketch.glyphs` exists at commit `f74674fd` (Glyphs format, gftools-compatible). Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and override config.yaml are all in place. Status is `complete`. The commit is HEAD of the upstream repo with no subsequent commits, and the timeline aligns exactly with PR #459 by Marc Foley.
