# Investigation: Averia Serif Libre

## Summary

| Field | Value |
|-------|-------|
| Family Name | Averia Serif Libre |
| Slug | averia-serif-libre |
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

Averia Serif Libre is a 6-style display font family by Dan Sayers (i@iotic.com), added to Google Fonts on 2012-03-14 (initial commit `90abd17b4`). The METADATA.pb has no `source { }` block. The font was last updated via PR #839 (`463ce0ab2`, "hotfix-averiaseriflibre: v1.002 added", 2017-08-07) by Marc Foley. The PR body was empty. Additional metadata updates added `stroke: "SERIF"` and `classifications: "DISPLAY"` fields.

Like the other Averia Libre family variants, Averia Serif Libre was created by algorithmically averaging all OFL-licensed serif fonts from Google Web Fonts (as of November 9, 2011), using FontForge.

**No official upstream repository found**: Dan Sayers' GitHub account (`dansayers`) has only one unrelated public repo. The `IOTic` account has only a traccar-client-android repo. The Averia project website at http://iotic.com/averia/ provides ZIP downloads but no source repository links.

A legacy `librefonts/averiaseriflibre` repo exists in the cache. It contains TTX files for all 6 styles and a `src/` directory with only `METADATA_comments.txt` and `VERSIONS.txt`. No editable source files are present.

A third-party project `eliheuer/averia-libre-vf` contains `.glyphs` sources for Averia Serif Libre (files named `Averia-Serif-Libre-Italic.glyphs` and `Averia-Serif-Libre-Roman.glyphs`), created by Eli Heuer in December 2018 for a variable font conversion. This is not the original design source repository and was created independently of Dan Sayers.

## Conclusion

No official upstream repository with build-compatible sources exists. The Averia Serif Libre fonts were algorithmically generated and the creator has not published design source repositories. The librefonts mirror contains only decompiled TTX files. The `eliheuer/averia-libre-vf` project provides third-party .glyphs sources but is not the authoritative upstream. No config.yaml is applicable. Status is no_upstream_repo. All four Averia Libre family variants share this same situation.
