# Investigation: Big Shoulders Stencil Text

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Stencil Text |
| Slug | big-shoulders-stencil-text |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 41153e6fe01d218e933919a1d08c8e45065bc8fe (recorded) / 2f924dd1205484c5e0054b1f3955f434224ba72e (correct) |
| Config YAML | override config.yaml in google/fonts (ofl/bigshouldersstenciltext/config.yaml) |
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
    source_file: "Big-Shoulders-Stencil/fonts/variable/text/BigShouldersStencilText[wght].ttf"
    dest_file: "BigShouldersStencilText[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`, but this is incorrect. The google/fonts commit `4ea17f133` (PR #3435, "Big Shoulders Stencil Text: Version 2.000 added") states:

> "Big Shoulders Stencil Text Version 2.001 taken from the upstream repo ... at commit https://github.com/xotypeco/big_shoulders/commit/2f924dd1205484c5e0054b1f3955f434224ba72e."

The existing `upstream_info.md` in `ofl/bigshouldersstenciltext/upstream_info.md` provides detailed binary SHA256 verification confirming `2f924dd` as the correct commit. The same pattern of dual gftools-packager runs exists: the initial PR referenced `41153e6` (May 2021), but the final merged commit referenced `2f924dd` (September 2021). Both commits exist in the upstream repo cache.

### Config YAML

An override `config.yaml` exists in `ofl/bigshouldersstenciltext/config.yaml`. It builds from `Big-Shoulders-Stencil/sources/BigShouldersStencil.glyphs`, subspaces to `opsz=10` (text), and also builds the SC variant. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb has repository URL and commit hash, but the commit `41153e6` is incorrect. The correct commit is `2f924dd1205484c5e0054b1f3955f434224ba72e`. The source block needs correction to update the commit hash. The override config.yaml is correctly configured.
