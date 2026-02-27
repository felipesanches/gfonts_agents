# Investigation: 42dot Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | 42dot Sans |
| Slug | 42dot-sans |
| License Dir | ofl |
| Repository URL | https://github.com/42dot/42dot-Sans |
| Commit Hash | d23e87fe44d5b4f5afaa9dca9d5926d7c414d625 |
| Config YAML | sources/config_variable.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/42dot/42dot-Sans"
  commit: "d23e87fe44d5b4f5afaa9dca9d5926d7c414d625"
  branch: "main"
  config_yaml: "sources/config_variable.yaml"
}
```

## Investigation

### Git History

The TTF files in `ofl/42dotsans/` have a single commit in the google/fonts repository:

```
d60948acd 42dot Sans : v1.00 added
```

The full commit message of `d60948acd` explicitly references the upstream repo and commit:

> Taken from the upstream repo https://github.com/42dot/42dot-Sans at commit https://github.com/42dot/42dot-Sans/commit/d23e87fe44d5b4f5afaa9dca9d5926d7c414d625

### Upstream Repository

The upstream repo is cloned at `upstream_repos/fontc_crater_cache/42dot/42dot-Sans/`. The commit `d23e87fe44d5b4f5afaa9dca9d5926d7c414d625` exists in the repo with message "Adding some metadata" (dated 2024-12-23 05:50:28 -0800).

The `sources/` directory at this commit contains:
- `42dotSans.designspace`
- `42dotSans.glyphspackage/` (Glyphs package source)
- `config_variable.yaml`
- `config_static.yaml`

The `config_variable.yaml` file contains:
```yaml
sources:
  - 42dotSans.designspace
familyName: 42dot Sans
autohintTTF: False
buildOTF: False
buildStatic: False
buildVariable: True
buildWebfont: False
removeOutlineOverlaps: False
```

### Commit Verification

The upstream commit `d23e87fe` is dated 2024-12-23 05:50:28 -0800, which is just 1 minute before the google/fonts onboarding commit `d60948acd` (implied by "42dot Sans : v1.00 added"), confirming the font was packaged immediately from this upstream commit. All data in METADATA.pb is consistent with this commit.

## Conclusion

No action needed. The METADATA.pb `source {}` block is complete and accurate: repository URL, commit hash, branch, and config_yaml are all verified and consistent. This family is fully documented.
