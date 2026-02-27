# Investigation: Bad Script

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bad Script |
| Slug | bad-script |
| License Dir | ofl |
| Repository URL | https://github.com/alexeiva/badscript |
| Commit Hash | dca2962433a2b5817f1e716d6731a743440fbd79 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/alexeiva/badscript"
  commit: "dca2962433a2b5817f1e716d6731a743440fbd79"
  files {
    source_file: "fonts/ttf/BadScript-Regular.ttf"
    dest_file: "BadScript-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The TTF files have the following commits (newest first):

- `0827c33ed` — "Bad Script: Version 2.000; ttfautohint (v1.8.4.7-5d5b) added" (most recent)
- `235f2c1aa` — "badscript: disabled Use Typo Metrics flag"
- `006c20a1d` — "badscript: updated win asc and win desc"
- `6bd3f5e01` — "badscript: inherited old vertical metrics from v1.002"
- `b44c3c58f` — "v2.000: added"
- `90abd17b4` — "Initial commit"

The most recent font commit message (`0827c33ed`) says:

> Taken from the upstream repo https://github.com/alexeiva/badscript at commit
> https://github.com/alexeiva/badscript/commit/dca2962433a2b5817f1e716d6731a743440fbd79.

This matches exactly what is recorded in METADATA.pb.

### Commit Verification

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/alexeiva/badscript`:

- Commit `dca2962433a2b5817f1e716d6731a743440fbd79` (2024-11-08) — "Merge pull request #6 from emmamarichal/master"

The commit is confirmed present in the cache. The upstream commit (2024-11-08) predates the google/fonts onboarding, which is consistent.

### Config YAML Verification

The `config.yaml` at `sources/config.yaml` in the upstream repo contains:

```yaml
sources:
  - BadScript.glyphs
familyName: Bad Script
cleanUp: true
```

This is a valid gftools-builder configuration. The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly references this file.

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/alexeiva/badscript`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and config_yaml path are all verified. No action required.
