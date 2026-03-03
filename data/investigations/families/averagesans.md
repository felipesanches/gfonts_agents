# Investigation: Average Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Average Sans |
| Slug | average-sans |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/averagesans |
| Commit Hash | 79216d6e944c1c35f1b8f4a1a9f50ad9ee73868c |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/averagesans"
  commit: "79216d6e944c1c35f1b8f4a1a9f50ad9ee73868c"
}
```

## Investigation

Average Sans is a sans-serif font by Eduardo Tunni, added to Google Fonts on 2012-10-26. The font was last updated via PR #835 (`76f813683`, "hotfix-averagesans: v1.002 added", 2017-08-07) by Marc Foley. The source block in METADATA.pb was added by commit `937245125` ("Average Sans: add source block to METADATA.pb").

The upstream repository `librefonts/averagesans` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/averagesans`. The commit `79216d6e` is the head of the repo (dated 2014-07, "update .travis.yml").

**Source file format**: The repository contains:
- `src/AverageSans-Regular-OTF.vfb` (FontLab binary)
- `src/AverageSans-Regular-TTF.sfd` (FontForge SFD)
- Multiple TTX (decompiled font table) XML files

No `.glyphs`, `.ufo`, or `.designspace` sources exist. No `config.yaml` exists in the repository or in the google/fonts family directory (`ofl/averagesans/`). These formats are not compatible with gftools-builder.

Eduardo Tunni's GitHub account (`etunni`) hosts many font repos including `average` (the serif sister family with `.glyphs` sources), but no Average Sans repository. The librefonts mirror is the only known archive.

## Conclusion

Repository URL and commit hash are documented in METADATA.pb. No config.yaml is possible without source conversion from VFB/SFD to a modern format. Status remains missing_config. Eduardo Tunni may have modern source files for Average Sans (similar to Average serif which has .glyphs sources), but none have been published to GitHub. Contact would be needed to determine if modern sources exist.
