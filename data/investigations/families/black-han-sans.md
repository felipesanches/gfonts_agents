# Investigation: Black Han Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Black Han Sans |
| Slug | black-han-sans |
| License Dir | ofl |
| Repository URL | https://github.com/zesstype/Black-Han-Sans |
| Commit Hash | 8809d5944fbf6aa2cd99158cb7ab55629058348a |
| Config YAML | none (binary-only repo, no gftools-builder sources) |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/zesstype/Black-Han-Sans"
  commit: "8809d5944fbf6aa2cd99158cb7ab55629058348a"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set, and there is no `files` block or `branch` field.

This source block was added by commit `c200187d3` ("Black Han Sans: add source block to METADATA.pb") with the note "Config: none (SFD-only sources)" and "Status: missing_config", indicating this was previously investigated and the lack of config was already known.

Commit `8809d5944fbf6aa2cd99158cb7ab55629058348a` is confirmed in the upstream repo cache at `/mnt/shared/upstream_repos/fontc_crater_cache/zesstype/Black-Han-Sans` (dated September 3, 2020, "Update README.md"). The repository contains only binary files: `BlackHanSans.ttf`, `OFL.txt`, `README.md`, and a Korean-named OTF file (`검은고딕.otf`). There are no source files (no `.glyphs`, `.ufo`, `.sfd`, `.designspace`), only compiled binaries.

The git history in google/fonts shows the font was originally added in commit `16680f868` (PR #1459, March 2018 Korean batch). More recent updates include `80a0a8ab2` (November 2024, "last hotfix in copyright") which updated the TTF binary (a copyright string fix), along with several other binary updates in 2024.

The commit hash `8809d5944` (September 3, 2020) predates the current TTF in google/fonts by several years. The most recent TTF modifications appear to have been done directly (hotfix-style) without reference to upstream repository commits, suggesting the effective "source of truth" in upstream may not correspond to the current binary in google/fonts.

The upstream repository is essentially a binary delivery repository with no compilable font sources.

## Conclusion

The source block has a repository URL and commit hash. No `config_yaml` is possible or needed since the upstream repo contains only binary TTF/OTF files and no gftools-builder-compatible sources. The commit hash `8809d5944fbf6aa2cd99158cb7ab55629058348a` is the last meaningful upstream commit but may not correspond to the current TTF in google/fonts (which received copyright hotfixes directly). Status is `missing_config` as no build configuration is possible from the available sources.
