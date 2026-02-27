# Investigation: BioRhyme Expanded

## Summary

| Field | Value |
|-------|-------|
| Family Name | BioRhyme Expanded |
| Slug | biorhyme-expanded |
| License Dir | ofl |
| Repository URL | https://github.com/aoifemooney/makingbiorhyme |
| Commit Hash | b3c0488559ad7c42e11b71e65d255344faff63b9 |
| Config YAML | sources/config.yaml (in upstream repo) |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/aoifemooney/makingbiorhyme"
  commit: "b3c0488559ad7c42e11b71e65d255344faff63b9"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/aoifemooney/makingbiorhyme` is documented in METADATA.pb. The upstream repo is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/aoifemooney/makingbiorhyme` as a shallow clone.

### Commit Hash

The METADATA.pb records commit `b3c0488559ad7c42e11b71e65d255344faff63b9`. This was set via a dedicated commit `2e8dadbdf` ("BioRhyme Expanded: add source block to METADATA.pb") which states:

```
- Repo: aoifemooney/makingbiorhyme
- Commit: b3c04885 (only commit in repo)
- Config: sources/config.yaml
- Status: complete
- Confidence: MEDIUM
```

The upstream repo is a shallow clone with only one visible commit: `b3c0488` dated 2023-09-18 ("Merge pull request #25 from emmamarichal/gh-pages"). The font binaries were originally added to google/fonts much earlier — commit `57523b5f6` ("hotfix-biorhymeexpanded: v1.001 added (#983)") dated 2017-05-23.

The commit `b3c0488` is the only commit accessible in the shallow clone, and the `config.yaml` file (which enables a gftools build) was added as part of this 2023 PR. The BioRhyme Expanded fonts in google/fonts are static fonts built from the expanded width axis of the BioRhyme variable font, which did not exist when the fonts were first onboarded in 2017.

The MEDIUM confidence reflects that `b3c0488` postdates the original onboarding and the original static fonts may have been compiled differently, but this is the only documented upstream state with a buildable config.

### Config YAML

The `config.yaml` exists at `sources/config.yaml` in the upstream repo. It configures a build from `BioRhyme.glyphs` with both `wdth` and `wght` axes. The `familyName` is set to `BioRhyme` (not BioRhyme Expanded), suggesting the config builds the full BioRhyme family including the expanded widths — the static `BioRhyme Expanded` instances would be derived from the width axis.

The `config_yaml` field in METADATA.pb correctly references `sources/config.yaml`.

## Conclusion

The source block in METADATA.pb has repository URL, commit hash, and config_yaml path. The commit `b3c0488` is the only commit in the shallow upstream clone and was set when the source block was added. The config.yaml exists and enables a gftools build. Confidence is MEDIUM because the commit significantly postdates the original 2017 onboarding, but no earlier commit is accessible. Status is `complete`.
