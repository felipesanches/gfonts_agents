# Investigation: Big Shoulders Stencil Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Stencil Display |
| Slug | big-shoulders-stencil-display |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 41153e6fe01d218e933919a1d08c8e45065bc8fe (recorded) / 2f924dd1205484c5e0054b1f3955f434224ba72e (correct) |
| Config YAML | override config.yaml in google/fonts (ofl/bigshouldersstencildisplay/config.yaml) |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "41153e6fe01d218e933919a1d08c8e45065bc8fe"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Stencil/fonts/variable/display/BigShouldersStencilDisplay[wght].ttf"
    dest_file: "BigShouldersStencilDisplay[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`, but this is incorrect. The google/fonts commit `081d4ba5b` (PR #3436, "Big Shoulders Stencil Display: Version 2.000 added") contains:

> "Big Shoulders Stencil Display Version 2.001 taken from the upstream repo ... at commit https://github.com/xotypeco/big_shoulders/commit/2f924dd1205484c5e0054b1f3955f434224ba72e."

The gftools-packager was run twice in PR #3436, similar to the pattern seen across all the Big Shoulders v2 PRs. The squash commit body references `2f924dd` (September 2021) as the final packager run, while `41153e6` was referenced in the earlier PR body (May 2021).

The existing `upstream_info.md` in `ofl/bigshouldersstencildisplay/upstream_info.md` documents this discrepancy and confirms via binary blob verification that `2f924dd` is correct. Both commits exist in the upstream repo cache.

### Config YAML

An override `config.yaml` exists in `ofl/bigshouldersstencildisplay/config.yaml`. It builds from `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`, subspaces to `opsz=72` (display), and also builds the SC variant. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb has repository URL and commit hash, but the commit `41153e6` is incorrect. The correct commit is `2f924dd1205484c5e0054b1f3955f434224ba72e`. The source block needs correction to update the commit hash. The override config.yaml is correctly configured.
