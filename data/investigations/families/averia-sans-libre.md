# Investigation: Averia Sans Libre

## Summary

| Field | Value |
|-------|-------|
| Family Name | Averia Sans Libre |
| Slug | averia-sans-libre |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_upstream_repo |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

Averia Sans Libre is a 6-style display font family by Dan Sayers (i@iotic.com), added to Google Fonts on 2012-03-14 (initial commit `90abd17b4`). The METADATA.pb has no `source { }` block. The font was last updated via PR #838 (`0f81bc904`, "hotfix-averiasanslibre: v1.002 added", 2017-08-07) by Marc Foley. The PR body was empty. Additional metadata updates were made in commit `1db714082` ("The last batch of ~250 updated METADATA.pb files for stroke and classification"), which added `stroke: "SANS_SERIF"` and `classifications: "DISPLAY"` fields.

Like the other Averia Libre family variants, Averia Sans Libre was created by algorithmically averaging all OFL-licensed sans-serif fonts from Google Web Fonts (as of November 9, 2011), using FontForge.

**No upstream repository found**: Dan Sayers has no font source repositories on GitHub. A `Tookmund/fonts-averia-sans` repo exists, but it is a Debian packaging repo, not an upstream source repository. No "averia-sans-libre" or "averiasanslibre" repositories were found on GitHub.

A legacy `librefonts/averiasanslibre` repo exists in the cache. It contains TTX files for all 6 styles and a `src/` directory with only `METADATA_comments.txt` and `VERSIONS.txt`. No editable source files are present.

## Conclusion

No upstream repository with build-compatible sources exists. The Averia Sans Libre fonts were algorithmically generated and the creator has not published design source repositories. The librefonts mirror contains only decompiled TTX files. No config.yaml is applicable. Status is no_upstream_repo. All four Averia Libre family variants (Averia Gruesa Libre, Averia Libre, Averia Sans Libre, Averia Serif Libre) share this same situation.
