# Investigation: Barlow Condensed

## Summary

| Field | Value |
|-------|-------|
| Family Name | Barlow Condensed |
| Slug | barlow-condensed |
| License Dir | ofl |
| Repository URL | https://github.com/jpt/barlow |
| Commit Hash | b4726ddf91525818e85e5fce111c285b9273d764 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/jpt/barlow"
  commit: "b4726ddf91525818e85e5fce111c285b9273d764"
}
```

## Investigation

### Google Fonts Git History

The `.ttf` files in `ofl/barlowcondensed/` were last modified by two commits:

1. `89f5431ff` (2018-12-05) — `barlow family updated to v1.408 (#1330) - major fixes`
2. `a9741353e` (2017-10-31) — `barlowcondensed: v1.101 added (#1279)`

The original onboarding (PR #1279) was done by Marc Foley with commit message:
> "Taken from the upstream repository, https://github.com/jpt/barlow"

The v1.408 update (PR #1330) replaced the binaries. PR #1330 was submitted by Jeremy Tribby (the designer, @jpt) himself with description referencing version 1.408 and the jpt/barlow releases page.

### Commit Hash Identification

Commit `b4726ddf91525818e85e5fce111c285b9273d764` (2018-11-06, "Fixes #34 and #37") is the last commit in the upstream repo before the google/fonts update (2018-12-05). This is the commit at which the v1.408 binaries in the google/fonts repo would have been built from.

Commits in the upstream `jpt/barlow` repo between 2018-11-06 and 2018-12-06:
- Only `b4726ddf` was found in this window.

### Config YAML

No `config.yaml` exists anywhere in the upstream `jpt/barlow` repository at any commit. The Barlow.glyphs file is a multi-axis source that builds multiple width variants (Condensed, Semi Condensed, regular Barlow). An override `config.yaml` is provided in the `ofl/barlowcondensed/` directory of google/fonts with the following contents:

```yaml
sources:
  - sources/Barlow.glyphs
familyName: Barlow Condensed
buildVariable: false
```

This override was added as part of commit `60824dce4` in google/fonts (part of PR #10271):
> "Barlow Condensed: add source block to METADATA.pb"

Per CLAUDE.md policy, when an override `config.yaml` exists in the google/fonts family directory, `config_yaml` is omitted from METADATA.pb (google-fonts-sources auto-detects local overrides).

### Already Completed in PR #10271

This family's source block was already added to METADATA.pb via PR #10271 (commit `60824dce4`). The current state is complete:
- `repository_url`: correct
- `commit`: correct (`b4726ddf`)
- Override `config.yaml` in place

### Upstream Repo Cache

Repository is cached at `upstream_repos/fontc_crater_cache/jpt/barlow/`.

## Conclusion

Status is **complete**. The source block was added via google/fonts PR #10271. Repository URL, commit hash, and override config.yaml are all in place. No further action required.
