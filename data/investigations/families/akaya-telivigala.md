# Investigation: Akaya Telivigala

## Summary

| Field | Value |
|-------|-------|
| Family Name | Akaya Telivigala |
| Slug | akaya-telivigala |
| License Dir | ofl |
| Repository URL | https://github.com/vaishnavimurthy/Akaya-Telivigala |
| Commit Hash | 93b31e45b69178ecfdb48981a5aa8a8b33bb0340 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/vaishnavimurthy/Akaya-Telivigala"
  commit: "93b31e45b69178ecfdb48981a5aa8a8b33bb0340"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "TTF/AkayaTelivigala-Regular.ttf"
    dest_file: "AkayaTelivigala-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The font was most recently updated in google/fonts via PR #3355, merged on 2021-04-30 by Yanone (google/fonts commit `7b4021c0a`). The commit message references:

> Akaya Telivigala Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/vaishnavimurthy/Akaya-Telivigala.git at commit https://github.com/vaishnavimurthy/Akaya-Telivigala/commit/93b31e45b69178ecfdb48981a5aa8a8b33bb0340.

The METADATA.pb commit `93b31e45b69178ecfdb48981a5aa8a8b33bb0340` is the merge commit of PR #5 in the upstream repository ("Merge pull request #5 from yanone/master", dated 2021-04-29). This is the correct commit — it was directly referenced by the gftools-packager message and matches what is in METADATA.pb. The commit exists and is verified in the cached repository.

Earlier google/fonts updates are visible: PR #2971 (Version 1.001, Jan 2021) and PR #2957 (initial, Jan 2021).

The upstream repository is cached at `upstream_repos/fontc_crater_cache/vaishnavimurthy/Akaya-Telivigala/`. It contains a `.glyphs` source file at `Source/AkayaTelivigala.glyphs`. Inspection of the tree at commit `93b31e45` via `git ls-tree` reveals **no `config.yaml`** file. None exists in the repository currently either.

## Conclusion

The repository URL and commit hash in METADATA.pb are correct and HIGH confidence. An override `config.yaml` should be created in the google/fonts `ofl/akayatelivigala/` directory to enable gftools-builder builds from the upstream `.glyphs` source file (`Source/AkayaTelivigala.glyphs`).
