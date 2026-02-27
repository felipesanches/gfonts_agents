# Investigation: Annie Use Your Telescope

## Summary

| Field | Value |
|-------|-------|
| Family Name | Annie Use Your Telescope |
| Slug | annie-use-your-telescope |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/annieuseyourtelescope |
| Commit Hash | 0895f3f4e7336525aee1a0ce0126bb13bfc80e35 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/librefonts/annieuseyourtelescope"
  commit: "0895f3f4e7336525aee1a0ce0126bb13bfc80e35"
}
```

## Investigation

### Repository

The upstream repository `librefonts/annieuseyourtelescope` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/librefonts/annieuseyourtelescope`. The repository URL is pre-existing in METADATA.pb.

### Commit Hash

The commit `0895f3f4e7336525aee1a0ce0126bb13bfc80e35` was verified present in the cached repo: `git cat-file -t 0895f3f4` returns `commit`. The commit is dated 2014-10-17 with message "update .travis.yml" by author hash3g — this is the HEAD of the repo and its most recent commit.

The google/fonts TTF was last modified in commit `df8d76c2f` ("hotfix-annieuseyourtelescope: v1.003 added (#814)") on 2017-08-07, authored by Marc Foley. No PR body or commit message references a specific upstream commit hash.

### Source Files

Inspection of `src/` in the cached repo reveals only:
- `AnnieUseYourTelescope.vfb` — FontLab binary format

No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist. The `.vfb` FontLab binary is not supported by gftools-builder.

### Config YAML

No config.yaml is present in the upstream repo. Because the only source file is a `.vfb` binary, no gftools-builder-compatible config.yaml can be created.

## Conclusion

The METADATA.pb source block exists with repository URL and commit hash. Status is `missing_config` because the upstream repo contains only a FontLab `.vfb` binary source, which gftools-builder does not support. No config.yaml is possible for this family. No further action can be taken without the designer providing gftools-compatible sources.
