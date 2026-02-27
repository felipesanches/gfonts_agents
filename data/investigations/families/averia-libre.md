# Investigation: Averia Libre

## Summary

| Field | Value |
|-------|-------|
| Family Name | Averia Libre |
| Slug | averia-libre |
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

Averia Libre is a 6-style display font family by Dan Sayers (i@iotic.com), added to Google Fonts on 2012-03-14 (initial commit `90abd17b4`). The METADATA.pb has no `source { }` block. The font was last updated via PR #837 (`fc10731b1`, "hotfix-averialibre: v1.002 added", 2017-08-07) by Marc Foley, which modified all 6 font files (Light, LightItalic, Regular, Italic, Bold, BoldItalic). The PR body was empty.

The Averia Libre family was created by algorithmically averaging all OFL-licensed fonts from Google Web Fonts (as of November 9, 2011), using FontForge. This is described in the FONTLOG.txt in the google/fonts family directory.

**No upstream repository found**: Dan Sayers' GitHub account (`dansayers`) has only one unrelated public repo. The `IOTic` GitHub account (his other identity) has only a traccar-client-android repo.

A legacy `librefonts/averialibre` repo exists in the cache. It contains TTX files for all 6 styles and a `src/` directory with only `METADATA_comments.txt` and `VERSIONS.txt`. No editable source files (.glyphs, .ufo, .designspace, .sfd) are present.

A separate `eliheuer/averia-libre-vf` repo exists on GitHub (created December 2018) with `.glyphs` source files, but this covers **Averia Serif Libre** (not Averia Libre), and represents a third-party variable font conversion by Eli Heuer rather than the original design source.

## Conclusion

No upstream repository with build-compatible sources exists. The Averia Libre fonts were algorithmically generated and the creator has not published design source repositories. The librefonts mirror contains only decompiled TTX files. No config.yaml is applicable. Status is no_upstream_repo.
