# Investigation: Bai Jamjuree

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bai Jamjuree |
| Slug | bai-jamjuree |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/Bai-Jamjuree |
| Commit Hash | e35cafdf694905d1ac0f27afc587c0e972be1260 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/Bai-Jamjuree"
  commit: "e35cafdf694905d1ac0f27afc587c0e972be1260"
}
```

## Investigation

### Git History in google/fonts

The TTF files have two commits:

- `8192d5fe3` — "baijamjuree: unhinted fonts." (most recent)
- `f27b6e87a` — "baijamjuree: v1.000 added"

The initial onboarding commit (`f27b6e87a`) says:

> Taken from the upstream repo https://github.com/cadsondemak/Bai-Jamjuree at commit
> https://github.com/cadsondemak/Bai-Jamjuree/commit/e35cafdf694905d1ac0f27afc587c0e972be1260

The subsequent commit (`8192d5fe3`) explains:
> baijamjuree: unhinted fonts. In the future, we plan to release this family as an unhinted variable font.

The METADATA.pb commit matches the onboarding commit referenced in the git history.

### Commit Verification

Inspecting the upstream repo at `/mnt/shared/upstream_repos/fontc_crater_cache/cadsondemak/Bai-Jamjuree`:

- Commit `e35cafdf694905d1ac0f27afc587c0e972be1260` — "Merge pull request #9 from m4rc1e/fonts" — confirmed present in the cache.

The upstream repo git log shows:
```
7b83d33 Update index.html
c2d8de0 Fix Font name
e35cafd Merge pull request #9 from m4rc1e/fonts
39d30d7 Adjusted vertical metrics to reduce first line clipping
44cb51a Generated fonts
f80b4d1 Merge pull request #8 from m4rc1e/gf-mastering
```

### Sources in Upstream Repo

The upstream repo contains only a single Glyphs source file at `source/Baijam.glyphs`. At commit `e35cafdf`, there is no `config.yaml` in the upstream repo.

### Override config.yaml

An override `config.yaml` exists in the google/fonts family directory at `ofl/baijamjuree/config.yaml`:

```yaml
sources:
  - source/Baijam.glyphs
```

This correctly points to the Glyphs source in the upstream repo. Since the override config.yaml is present locally, no `config_yaml` field is needed in METADATA.pb (google-fonts-sources auto-detects it).

### Repository Cache

The upstream repo is cached at:
`/mnt/shared/upstream_repos/fontc_crater_cache/cadsondemak/Bai-Jamjuree`

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL and commit hash are verified. An override `config.yaml` in the google/fonts family directory provides the build configuration pointing to the upstream Glyphs source. No action required.
