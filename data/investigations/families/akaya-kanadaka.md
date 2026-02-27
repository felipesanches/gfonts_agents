# Investigation: Akaya Kanadaka

## Summary

| Field | Value |
|-------|-------|
| Family Name | Akaya Kanadaka |
| Slug | akaya-kanadaka |
| License Dir | ofl |
| Repository URL | https://github.com/vaishnavimurthy/Akaya-Kanadaka |
| Commit Hash | 24f25461789ee8642e184b43dd6d5d04ea7f49d1 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/vaishnavimurthy/Akaya-Kanadaka"
  commit: "24f25461789ee8642e184b43dd6d5d04ea7f49d1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "TTF/AkayaKanadaka-Regular.ttf"
    dest_file: "AkayaKanadaka-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The font was added to google/fonts via PR #2970, merged on 2021-01-27 by Yanone. The gftools-packager commit message (google/fonts commit `6bfbea71f`) references:

> Akaya Kanadaka Version 1.002; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/vaishnavimurthy/Akaya-Kanadaka.git at commit https://github.com/vaishnavimurthy/Akaya-Kanadaka/commit/72bdbc541ee3311e0eadafc80d7f097d1d8080a9.

The METADATA.pb records commit `24f25461789ee8642e184b43dd6d5d04ea7f49d1`, while the packager message mentions `72bdbc541ee3311e0eadafc80d7f097d1d8080a9`. Investigation shows that `24f25461` is the branch commit ("Enabled fsSelection bit 7 (Use Typo Metrics)", authored 2021-01-21 by Yanone) and `72bdbc54` is the merge commit of PR #14 into the Akaya Kanadaka master branch. A `git diff` between them shows no changes — both commits reference identical TTF content. The METADATA.pb correctly records `24f25461` as the substantive source commit (the tip of the feature branch before merging).

The upstream repository is cached at `upstream_repos/fontc_crater_cache/vaishnavimurthy/Akaya-Kanadaka/`. It contains a `.glyphs` source file at `Source/AkayaKanadaka.glyphs`. There is **no `config.yaml`** in the repository at the referenced commit (verified via `git ls-tree -r 72bdbc541`), and none currently either.

Both commits (`24f25461` and `72bdbc54`) exist and are verified in the cached repository.

## Conclusion

The repository URL and commit hash in METADATA.pb are correct and HIGH confidence. An override `config.yaml` should be created in the google/fonts `ofl/akayakanadaka/` directory to enable gftools-builder builds from the upstream `.glyphs` source file (`Source/AkayaKanadaka.glyphs`).
