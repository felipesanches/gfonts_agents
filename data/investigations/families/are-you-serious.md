# Investigation: Are You Serious

## Summary

| Field | Value |
|-------|-------|
| Family Name | Are You Serious |
| Slug | are-you-serious |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/are-you-serious |
| Commit Hash | 2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/are-you-serious"
  commit: "2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/AreYouSerious-Regular.ttf"
    dest_file: "AreYouSerious-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

### Repository

The upstream repository `googlefonts/are-you-serious` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/are-you-serious`. The repository URL, commit hash, and config_yaml are all pre-existing in METADATA.pb.

### Commit Hash

The commit `2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8` was verified present in the cached repo: `git cat-file -t 2975e6ba` returns `commit`. The commit is the HEAD of the `are-you-serious` repo, dated 2021-09-16 with message "Name fixed" by Viviana Monsalve.

The google/fonts TTF was last updated in commit `b6f5c2bd7` ("Are You Serious: Version 1.100 added (#3776)") on 2021-08-31. The PR body reads: "Are You Serious Version 1.100 taken from the upstream repo https://github.com/googlefonts/are-you-serious at commit https://github.com/googlefonts/are-you-serious/commit/21eb86d2baf500684d3b8600bc53f6ce27721495."

Note: The PR message references commit `21eb86d2`, but this commit does not exist in the cached repo (the repo history only goes back to `2975e6ba`). The METADATA.pb records commit `2975e6bae` ("Name fixed", 2021-09-16), which is more recent than the google/fonts merge date (2021-08-31). This is unusual — METADATA.pb shows a post-onboarding commit. Commit `2975e6bae` added AUTHORS.txt, CONTRIBUTORS.txt, OFL.txt, DESCRIPTION.en_us.html, font files and source files all in one commit ("Name fixed"), suggesting this was an initial repository setup commit (the repo was newly created for google/fonts onboarding). The gftools-packager commit reference to `21eb86d2` may be an artifact of a draft state that was force-pushed or rebased before the merge.

### Source Files

The `sources/` directory contains:
- `AreYouSerious.glyphs` — Glyphs format source
- `config.yml` — gftools-builder configuration

```yaml
sources:
  - AreYouSerious.glyphs
familyName: "Are You Serious"
buildVariable: false
autohintTTF: false
```

### Config YAML

`sources/config.yml` exists in the upstream repo and is correctly referenced in METADATA.pb as `config_yaml: "sources/config.yml"`.

## Conclusion

All source metadata is complete. Repository URL, commit hash, and config.yaml path are all present and verified. There is a minor discrepancy between the gftools-packager commit reference (`21eb86d2`) and METADATA.pb (`2975e6ba`), but `2975e6ba` is verified present and is the HEAD of the repo. Status is `complete` with HIGH confidence.
