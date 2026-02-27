# Investigation: B612 Mono

## Summary

| Field | Value |
|-------|-------|
| Family Name | B612 Mono |
| Slug | b612-mono |
| License Dir | ofl |
| Repository URL | https://github.com/polarsys/b612 |
| Commit Hash | 48ac6ba67ecab8123e8e36d6aa05367db0c7b638 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/polarsys/b612"
  commit: "48ac6ba67ecab8123e8e36d6aa05367db0c7b638"
}
```

## Investigation

### Git History in google/fonts

The TTF files were last modified in two commits:

- `bff0396e9` — "b612mono: v1.008 added." (2019-03-18)
- `0655ae3b2` — "b612 mono: version v1.005 added. (#1759)"

The most recent commit message (`bff0396e9`) says:

> Taken from the upstream repo https://github.com/polarsys/b612 at commit
> https://github.com/polarsys/b612/commit/7b5a653a6ae2bb05479297fed05ddf8c212d5477

The METADATA.pb source block, however, records commit `48ac6ba67ecab8123e8e36d6aa05367db0c7b638`.

### Commit Hash Analysis

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/polarsys/b612`:

- `7b5a653a6ae2bb05479297fed05ddf8c212d5477` (2019-03-12) — "Merge pull request #15 from intactile/master" — this is the release of TTF+UFO files for v1.008.
- `48ac6ba67ecab8123e8e36d6aa05367db0c7b638` (2019-03-18) — "Merge pull request #17 from sunpoet/master" — this only updates links from http to https in documentation.

The METADATA.pb was updated later in commit `edbfb125a` ("sources info for b612mono: v1.008 (PR #1878)") to record `48ac6ba` as the HEAD at the time. The 6-day-newer commit only changes URLs in documentation; the actual font sources are identical to `7b5a653`. Commit `48ac6ba` is therefore a valid and acceptable reference.

### Upstream Repo and Sources

The upstream repo (`polarsys/b612`) uses UFO sources in `sources/ufo/`. At commit `48ac6ba`, the sources directory contains:
- `sources/ufo/B612Mono-Regular.ufo`
- `sources/ufo/B612Mono-Italic.ufo`
- `sources/ufo/B612Mono-Bold.ufo`
- `sources/ufo/B612Mono-BoldItalic.ufo`

The repo uses a custom shell script (`scripts/build.sh`) rather than gftools-builder, so no `config.yaml` is present upstream.

### Override config.yaml

An override `config.yaml` exists in the google/fonts family directory at `ofl/b612mono/config.yaml`:

```yaml
buildVariable: false
sources:
  - sources/ufo/B612Mono-Bold.ufo
  - sources/ufo/B612Mono-BoldItalic.ufo
  - sources/ufo/B612Mono-Italic.ufo
  - sources/ufo/B612Mono-Regular.ufo
```

This correctly points to the UFO sources in the upstream repo. Since the override config.yaml is present locally, no `config_yaml` field is needed in METADATA.pb (google-fonts-sources auto-detects it).

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/polarsys/b612`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL and commit hash are valid. An override `config.yaml` in the google/fonts family directory provides the build configuration using the upstream UFO sources. No action required.
