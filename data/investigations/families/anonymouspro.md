# Investigation: Anonymous Pro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Anonymous Pro |
| Slug | anonymous-pro |
| License Dir | ofl |
| Repository URL | https://github.com/fontmgr/AnonymousPro |
| Commit Hash | de345fb4214f487b804a2c44aba59e30f866519b |
| Config YAML | none |
| Status | missing_config |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/fontmgr/AnonymousPro"
  commit: "de345fb4214f487b804a2c44aba59e30f866519b"
}
```

## Investigation

### Repository

The METADATA.pb source block references `fontmgr/AnonymousPro`. This repository is NOT cached in `/mnt/shared/upstream_repos/fontc_crater_cache/`. A different repository exists at `librefonts/anonymouspro` (its remote is `https://github.com/librefonts/anonymouspro`), but that is a separate repo containing TTX-format exported font data, not the `fontmgr` repository.

The source block was added to google/fonts in commit `b77cf8eb3` ("Anonymous Pro: add source block to METADATA.pb") with confidence LOW.

### Commit Hash

The commit `de345fb4214f487b804a2c44aba59e30f866519b` is recorded in METADATA.pb but cannot be verified locally since the `fontmgr/AnonymousPro` repo is not in the cache. Confidence is LOW — this was discovered via PR history research, not direct verification.

The google/fonts TTF was last modified in commit `152b05bd8` ("hotfix-anonymouspro: v1.003 added (#815)") on 2017-08-07. The commit message contains no reference to an upstream repo URL or commit hash.

### Source Files

The cached `librefonts/anonymouspro` repo contains only TTX-format data (exported font tables), not buildable sources. This is not the authoritative upstream for Anonymous Pro. The actual Mark Simonson Anonymous Pro sources (SFD/FontForge) are on his website; the `fontmgr/AnonymousPro` GitHub repo likely also contains only binary fonts.

### Config YAML

No config.yaml is applicable. Anonymous Pro originates from FontForge `.sfd` sources which are not gftools-builder compatible.

## Conclusion

The METADATA.pb source block points to `fontmgr/AnonymousPro` with commit `de345fb4`, but this repo is not in the local cache and the commit cannot be verified. Confidence is LOW. The upstream is binary-only (no gftools-buildable sources), so status is `missing_config` with no config.yaml possible.
