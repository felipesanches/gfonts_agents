# Investigation: Aref Ruqaa

## Summary

| Field | Value |
|-------|-------|
| Family Name | Aref Ruqaa |
| Slug | aref-ruqaa |
| License Dir | ofl |
| Repository URL | https://github.com/aliftype/aref-ruqaa |
| Commit Hash | 175e1ed565e75aba8059675b80dadc0a184d53e6 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/aliftype/aref-ruqaa"
  commit: "175e1ed565e75aba8059675b80dadc0a184d53e6"
}
```

## Investigation

### Repository

The upstream repository `aliftype/aref-ruqaa` is cached at `/mnt/shared/upstream_repos/fontc_crater_cache/aliftype/aref-ruqaa`. The repository URL is pre-existing in METADATA.pb.

Note: The METADATA.pb copyright line references `alif-type/aref-ruqaa` (old URL), but the source block correctly uses the current `aliftype/aref-ruqaa` URL.

### Commit Hash

The commit `175e1ed565e75aba8059675b80dadc0a184d53e6` was verified present in the cached repo: `git cat-file -t 175e1ed5` returns `commit`. The commit is dated 2021-03-18 with message "1.003" by Khaled Hosny. It matches version 1.003 of the font.

The google/fonts TTF was last updated in commit `de3320b54` ("arefruqaa: v1.003 (#3215)") on 2021-03-25. The commit message does not contain an explicit upstream commit hash, but the version number "1.003" and date correlation confirm commit `175e1ed5` as the onboarding commit.

### Source Files

Inspection of the upstream repo at commit `175e1ed5` via `git ls-tree -r 175e1ed5 -- sources/` reveals:
- `sources/ArefRuqaa.fea` — OpenType feature file
- `sources/EulerText-Bold.ufo/` — UFO format (a separate experimental source, not Aref Ruqaa)
- `sources/ArefRuqaa-Bold.sfdir/` — FontForge SFDir format
- (other sfdir files for the Bold master)

At commit `175e1ed5`, the Aref Ruqaa sources are in FontForge `.sfdir` format. The current HEAD of the repo has been migrated to a `.glyphspackage` format, but that migration happened after the onboarding commit.

### Config YAML

No config.yaml exists at commit `175e1ed5`. The sources at that commit are FontForge `.sfdir` format, which is not supported by gftools-builder. While the current HEAD has Glyphs sources, using a different commit would not reflect what was actually onboarded.

An override config.yaml could potentially be created using the current (post-onboarding) glyphspackage sources, but this would require investigation into what version of the font they produce vs what is in google/fonts.

## Conclusion

The METADATA.pb source block has repository URL and commit hash. Status is `missing_config` because at the recorded commit `175e1ed5`, the sources are in FontForge `.sfdir` format, which gftools-builder does not support. The repo has since been migrated to Glyphs format, but creating a config.yaml pointing to post-onboarding sources requires additional review.
