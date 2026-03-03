# Investigation: Big Shoulders Inline Display

## Summary

| Field | Value |
|-------|-------|
| Family Name | Big Shoulders Inline Display |
| Slug | big-shoulders-inline-display |
| License Dir | ofl |
| Repository URL | https://github.com/xotypeco/big_shoulders |
| Commit Hash | 41153e6fe01d218e933919a1d08c8e45065bc8fe (recorded) / 2f924dd1205484c5e0054b1f3955f434224ba72e (correct) |
| Config YAML | override config.yaml in google/fonts (ofl/bigshouldersinlinedisplay/config.yaml) |
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
    source_file: "Big-Shoulders-Inline/fonts/variable/display/BigShouldersInlineDisplay[wght].ttf"
    dest_file: "BigShouldersInlineDisplay[wght].ttf"
  }
  branch: "master"
}
```

## Investigation

### Repository URL

The repository URL `https://github.com/xotypeco/big_shoulders` is documented in METADATA.pb. All Big Shoulders variants share this upstream repository.

### Commit Hash

The METADATA.pb records commit `41153e6fe01d218e933919a1d08c8e45065bc8fe`, but this is incorrect. The existing `upstream_info.md` in the google/fonts family directory at `ofl/bigshouldersinlinedisplay/upstream_info.md` documents this discrepancy in detail.

The font was updated to Version 2.000 via google/fonts commit `d5baecffa` (PR #3438, "Big Shoulders Inline Display: Version 2.000 added"). That commit's squash body states:

> "Big Shoulders Inline Display Version 2.002 taken from the upstream repo ... at commit https://github.com/xotypeco/big_shoulders/commit/2f924dd1205484c5e0054b1f3955f434224ba72e."

The gftools-packager was run twice during PR #3438:
1. First run (PR body, 2021-05-21): Referenced `41153e6` (May 2021, Viviana Monsalve merge)
2. Final run (squash commit body): Referenced `2f924dd` (September 2021, "Merge pull request #40 from vv-monsalve/master")

Binary blob hash verification from the existing upstream_info.md confirms: the font file `BigShouldersInlineDisplay[wght].ttf` in google/fonts matches the blob at commit `2f924dd` exactly. Both commits exist in the upstream repo cache.

### Config YAML

An override `config.yaml` exists in `ofl/bigshouldersinlinedisplay/config.yaml`. It builds from `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs`, subspaces to `opsz=72` (display), and also builds the SC variant. The `config_yaml` field is correctly omitted from METADATA.pb.

## Conclusion

The METADATA.pb has repository URL and commit hash, but the commit `41153e6` is incorrect. The correct commit is `2f924dd1205484c5e0054b1f3955f434224ba72e`. The source block needs correction to update the commit hash. The override config.yaml is correctly configured.
