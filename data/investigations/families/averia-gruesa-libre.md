# Investigation: Averia Gruesa Libre

## Summary

| Field | Value |
|-------|-------|
| Family Name | Averia Gruesa Libre |
| Slug | averia-gruesa-libre |
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

Averia Gruesa Libre is a display font by Dan Sayers (i@iotic.com), added to Google Fonts on 2012-03-14 (initial commit `90abd17b4`). The METADATA.pb has no `source { }` block. The font was last updated via PR #836 (`e63e802be`, "hotfix-averiagruesalibre: v1.002 added", 2017-05-08) by Marc Foley. The PR body was empty.

The Averia font family was created through an unusual algorithmic process: Dan Sayers averaged all OFL-licensed fonts from Google Web Fonts (as of November 9, 2011) using FontForge scripts to produce composite glyphs. This unique origin means there are no traditional font design source files.

**No upstream repository found**: Dan Sayers' GitHub account (`dansayers`) has only one unrelated public repo (`dansayers/dissonance`, a JavaScript project). No font source repos exist under his account.

A legacy `librefonts/averiagruesalibre` repo exists in the cache. The repository root contains only TTX (decompiled font table) XML files. The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt` — no editable source files at all.

The VERSIONS.txt confirms: "AveriaGruesaLibre-Regular.ttf: Version 1.001". The METADATA_comments.txt contains font-optimizer subset generation scripts, confirming this is a post-processing archive rather than a design source.

The Averia project website at http://iotic.com/averia/ provides ZIP downloads but no source repository links.

## Conclusion

No upstream repository with build-compatible sources exists for this family. The Averia fonts were algorithmically generated from other fonts rather than hand-designed, and the creator has not published source repositories. The librefonts mirror contains only decompiled TTX files and metadata. No config.yaml is applicable without a proper source repository. Status is no_upstream_repo.
