# Investigation: Barlow Semi Condensed

## Summary

| Field | Value |
|-------|-------|
| Family Name | Barlow Semi Condensed |
| Slug | barlow-semi-condensed |
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

The `.ttf` files in `ofl/barlowsemicondensed/` were last modified by two commits:

1. `89f5431ff` (2018-12-05) — `barlow family updated to v1.408 (#1330) - major fixes`
2. `950449b4e` (2017-10-31) — `barlowsemicondensed: v1.101 added (#1280)`

The original onboarding (PR #1280) was done by Marc Foley with commit message:
> "Take from the upstream repo, https://github.com/jpt/barlow"

The v1.408 update (PR #1330) replaced the binaries. PR #1330 was submitted by Jeremy Tribby (the designer, @jpt) himself with description referencing version 1.408 and the jpt/barlow releases page.

Note that commit `89f5431ff` updated all three Barlow subfamilies simultaneously (Barlow, Barlow Condensed, Barlow Semi Condensed) in the same PR #1330, consistent with them all being built from the same upstream source file.

### Commit Hash Identification

Commit `b4726ddf91525818e85e5fce111c285b9273d764` (2018-11-06, "Fixes #34 and #37") is the last commit in the upstream repo before the google/fonts update (2018-12-05). This is the same commit used for Barlow and Barlow Condensed (all three were updated together in PR #1330 since they share a single source file `sources/Barlow.glyphs`).

### Config YAML

No `config.yaml` exists anywhere in the upstream `jpt/barlow` repository at any commit. The Barlow.glyphs file is a multi-axis source that builds multiple width variants. An override `config.yaml` is provided in the `ofl/barlowsemicondensed/` directory of google/fonts with the following contents:

```yaml
sources:
  - sources/Barlow.glyphs
familyName: Barlow Semi Condensed
buildVariable: false
```

This override was added as part of commit `3218ae2ac` in google/fonts (part of PR #10271):
> "Barlow Semi Condensed: add source block to METADATA.pb"

Per CLAUDE.md policy, when an override `config.yaml` exists in the google/fonts family directory, `config_yaml` is omitted from METADATA.pb (google-fonts-sources auto-detects local overrides).

### Already Completed in PR #10271

This family's source block was already added to METADATA.pb via PR #10271 (commit `3218ae2ac`). The current state is complete:
- `repository_url`: correct
- `commit`: correct (`b4726ddf`)
- Override `config.yaml` in place

### Upstream Repo Cache

Repository is cached at `upstream_repos/fontc_crater_cache/jpt/barlow/`.

## Conclusion

Status is **complete**. The source block was added via google/fonts PR #10271. Repository URL, commit hash, and override config.yaml are all in place. No further action required.
