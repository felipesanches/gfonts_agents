# Investigation: Asta Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Asta Sans |
| Slug | asta-sans |
| License Dir | ofl |
| Repository URL | https://github.com/42dot/Asta-Sans |
| Commit Hash | 62b8301ac4b2e2ddf62eadca79b91fa944618848 |
| Config YAML | sources/config_variable.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/42dot/Asta-Sans"
  commit: "62b8301ac4b2e2ddf62eadca79b91fa944618848"
  branch: "main"
  config_yaml: "sources/config_variable.yaml"
}
```

## Investigation

Asta Sans is a Korean variable font by the type foundry 42dot, added to Google Fonts on 2024-12-23. The font was formerly called "42dot Sans" before being renamed to "Asta Sans" in google/fonts commit `db2611132` ("Rename font family from 42dotSans to AstaSans", 2025-04-30 05:31:42 +0000).

The source block in METADATA.pb contains the repository URL `https://github.com/42dot/Asta-Sans` and commit hash `62b8301ac4b2e2ddf62eadca79b91fa944618848`. The commit is confirmed in the upstream cache at `42dot/Asta-Sans` (dated 2025-04-29 12:36:32 +0900, "Merge pull request #6 from Sandoll-DS/patch-1", which updated `sources/config_variable.yaml`).

The upstream repository has two config files:
- `sources/config_static.yaml` — for static font builds
- `sources/config_variable.yaml` — for variable font builds (the one referenced in METADATA.pb)

The source files include `AstaSans.designspace` and `AstaSans.glyphspackage` in the `sources/` directory.

The family covers Korean (Kore primary_script) with a weight axis (wght) ranging from 300 to 800.

## Conclusion

Status is complete. All required fields (repository_url, commit, config_yaml) are present and verified in METADATA.pb. The commit hash corresponds to the head of the repository at the time of the rename (2025-04-29), which is the most recent version. No further action needed.
