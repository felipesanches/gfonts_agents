# Investigation: Beau Rivage

## Summary

| Field | Value |
|-------|-------|
| Family Name | Beau Rivage |
| Slug | beau-rivage |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/beau-rivage |
| Commit Hash | a80b72a03f6ea0a5667c58620973efdb72384ffa |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/beau-rivage"
  commit: "a80b72a03f6ea0a5667c58620973efdb72384ffa"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BeauRivage-Regular.ttf"
    dest_file: "BeauRivage-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

Beau Rivage was added to google/fonts on 2022-02-17 via gftools-packager PR #4323 ("Beau Rivage: Version 1.010; ttfautohint (v1.8.3) added"), authored by Viviana Monsalve (vv-monsalve) and co-authored by Rosalie Wagner.

The gftools-packager commit message in google/fonts commit `4d3115f1ef99d09a91f6890cd25353f7c1cb1231` explicitly states:

> "Beau Rivage Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/beau-rivage at commit https://github.com/googlefonts/beau-rivage/commit/a80b72a03f6ea0a5667c58620973efdb72384ffa."

This is the highest-confidence method for determining the onboarding commit: it was recorded directly by gftools-packager in the initial add commit. The upstream commit `a80b72a` is titled "description moved to documentation dir" and is the HEAD of the upstream repository (no later commits exist).

The `sources/config.yml` file (note: `.yml` extension, not `.yaml`) exists at the recorded commit and contains valid gftools-builder configuration:

```yaml
sources:
  - BeauRivage-Pro.glyphs
familyName: "Beau Rivage"
buildVariable: false
# autohintTTF: false
```

The METADATA.pb correctly references this via `config_yaml: "sources/config.yml"`.

The upstream repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/beau-rivage`. The upstream repo is at HEAD with no later commits after the onboarding commit.

## Conclusion

Status is complete. The METADATA.pb source block has all required fields: `repository_url`, `commit`, `branch`, and `config_yaml`. The commit hash was recorded by gftools-packager directly in the onboarding commit. No action needed.
