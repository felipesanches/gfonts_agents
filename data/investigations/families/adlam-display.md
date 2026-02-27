# Investigation: ADLaM Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | ADLaM Display |
| Slug | adlam-display |
| License Dir | ofl |
| Repository URL | https://github.com/microsoft/ADLaM-Display |
| Commit Hash | 879176243e9f7161a8aefdab8c36a4a7318ebe15 |
| Config YAML | Sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/microsoft/ADLaM-Display"
  commit: "879176243e9f7161a8aefdab8c36a4a7318ebe15"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/ADLaMDisplay-Regular.ttf"
    dest_file: "ADLaMDisplay-Regular.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
```

## Investigation

### Git History

The TTF files in `ofl/adlamdisplay/` have one commit in google/fonts:

```
40699510e [gftools-packager] ADLaM Display: Version 2.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] added
```

The full body of `40699510e` (dated 2023-07-10 12:48:26 -0700) states:

> ADLaM Display Version 2.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.28] taken from the upstream repo https://github.com/microsoft/ADLaM-Display at commit https://github.com/microsoft/ADLaM-Display/commit/879176243e9f7161a8aefdab8c36a4a7318ebe15.

### Commit Verification

The commit `879176243e9f7161a8aefdab8c36a4a7318ebe15` exists in the upstream repo (cloned at `upstream_repos/fontc_crater_cache/microsoft/ADLaM-Display/`) with:
- Date: 2023-07-10 12:36:52 -0700
- Message: "Build"

The upstream commit is dated just 12 minutes before the google/fonts onboarding commit, strongly confirming this is the exact commit used for onboarding. The gftools-packager tool (referenced in the commit title) automatically records this information.

### Upstream Repository Structure

The `Sources/` directory (capital S) at the recorded commit contains:
- `Sources/ADLaM-Display.glyphs` (primary Glyphs source)
- `Sources/ADLaM-Display CORNERS.glyphs` (corners file)
- `Sources/config.yaml`

The `Sources/config.yaml` contains:
```yaml
sources:
  - ADLaM-Display.glyphs
familyName: "ADLaM Display"
buildOTF: false
```

Note: The capitalized `Sources/` directory name is notable. A google/fonts commit `7190093b1` ("A few fonts have `Sources` instead of `sources` directory") specifically addressed this convention. The METADATA.pb correctly records `config_yaml: "Sources/config.yaml"` with the capital S.

No override `config.yaml` exists in `ofl/adlamdisplay/` in google/fonts.

## Conclusion

No action needed. The METADATA.pb `source {}` block is complete and accurate: repository URL, commit hash, branch, files mappings, and config_yaml are all set and verified. The commit is directly corroborated by the gftools-packager commit message in google/fonts and the near-simultaneous timestamps (12 minutes apart). This family is fully documented.
