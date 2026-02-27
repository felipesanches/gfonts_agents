# Investigation: Bubblegum Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bubblegum Sans |
| Slug | bubblegum-sans |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/bubblegumsans |
| Commit Hash | fcf8bdd5e83b65186641b2b67fd957ff061666e3 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/bubblegumsans"
  commit: "fcf8bdd5e83b65186641b2b67fd957ff061666e3"
}
```

## Investigation

The source block was added to METADATA.pb in google/fonts commit `abf3821d9` ("Bubblegum Sans: add source block to METADATA.pb", Felipe Sanches, 2026-02-26). The commit metadata records: "Config: none (SFD-only sources), Status: missing_config, Confidence: MEDIUM".

The upstream repository URL `https://github.com/librefonts/bubblegumsans` is from the `librefonts` GitHub organization, which hosts archived copies of early Google Fonts source projects. The repository is cached at `upstream_repos/fontc_crater_cache/librefonts/bubblegumsans/`.

The commit `fcf8bdd5e83b65186641b2b67fd957ff061666e3` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). Since there is only one commit, the identification is unambiguous.

The source files present in the repository are:
- `src/BubblegumSans-Regular-TTF.sfd` (FontForge SFD format)
- `src/BubblegumSans-Regular-OTF.vfb` (FontLab VFB format)

These are legacy formats not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory.

The font was originally added to google/fonts in the initial commit `90abd17b4` and last had its binary updated in commit `75e7dd823` ("Updating ofl/bubblegumsans/*ttf with nbspace and fsType fixes", 2015-04-27 by Dave Crossland). These updates were done directly in the google/fonts repo, not via gftools-packager from the upstream repo.

## Conclusion

The source metadata (repository_url and commit) is present and correct in METADATA.pb. The status is `missing_config` because the upstream repo only contains SFD/VFB sources which cannot be used with gftools-builder. No override config.yaml is possible without first converting sources to a gftools-compatible format (`.glyphs`, `.ufo`, or `.designspace`). No further action needed unless source conversion is planned.
