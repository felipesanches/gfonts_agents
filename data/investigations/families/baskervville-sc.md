# Investigation: Baskervville SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Baskervville SC |
| Slug | baskervville-sc |
| License Dir | ofl |
| Repository URL | https://github.com/anrt-type/ANRT-Baskervville |
| Commit Hash | 0629447774568fd957d98736487afb000be38b55 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/anrt-type/ANRT-Baskervville"
  commit: "0629447774568fd957d98736487afb000be38b55"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BaskervvilleSC[wght].ttf"
    dest_file: "BaskervvilleSC[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Google Fonts Git History

The `.ttf` files in `ofl/baskervvillesc/` have been modified in three commits:

1. `72f3e5c39` — `update fonts with the right OFL url`
2. `fe282bb64` (2025-04-23) — `Baskervville SC: Version 1.100 added`
3. `db6a2c3f9` — `Baskervville SC: Version 1.003; ttfautohint (v1.8.4.7-5d5b) added`

The Version 1.100 commit message reads:
> "Taken from the upstream repo https://github.com/anrt-type/ANRT-Baskervville at commit https://github.com/anrt-type/ANRT-Baskervville/commit/0629447774568fd957d98736487afb000be38b55."

This is a clean, complete commit URL with the full hash — no truncation.

The original Version 1.003 commit message reads:
> "Taken from the upstream repo https://github.com/anrt-type/ANRT-Baskervville at commit https://github.com/anrt-type/ANRT-Baskervville/commit/11a43fe1ef8b4c23aff9f24c218412d15cca54fd."

### Commit Hash Verification

Commit `0629447774568fd957d98736487afb000be38b55` (2025-04-22, "rebuilt fonts with SC") exists in the upstream repo. It predates the google/fonts update (2025-04-23) by exactly one day, which is consistent with a standard onboarding workflow.

This is the commit that introduced the SC (Small Caps) variable font to the repo (`rebuilt fonts with SC`), which directly corresponds to the Baskervville SC family being added to google/fonts.

### Config YAML

`sources/config.yaml` exists in the upstream repo and was present at commit `0629447774568fd957d98736487afb000be38b55`. Contents:

```yaml
sources:
    - Baskervville.glyphs
    - Baskervville-Italic.glyphs
familyName: Baskervville
autohintOTF: false
buildSmallCap: true
```

Note that `familyName` is "Baskervville" (not "Baskervville SC"), but `buildSmallCap: true` instructs gftools-builder to generate the Small Caps variant, which produces the Baskervville SC font. The METADATA.pb correctly records `config_yaml: "sources/config.yaml"`.

This same commit and `sources/config.yaml` is also referenced by the non-SC Baskervville family (`ofl/baskervville/METADATA.pb`), as both families are built from the same upstream source.

### METADATA.pb History

The `config_yaml` field was added to METADATA.pb in batch commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"), imported from the fontc_crater targets.json. The repository_url and commit were added earlier via the gftools-packager-style commit `fe282bb64`.

### Upstream Repo Cache

Repository is cached at `upstream_repos/fontc_crater_cache/anrt-type/ANRT-Baskervville/`.

## Conclusion

Status is **complete**. All fields in the METADATA.pb source block are correct:
- `repository_url`: https://github.com/anrt-type/ANRT-Baskervville
- `commit`: 0629447774568fd957d98736487afb000be38b55 (2025-04-22, one day before onboarding)
- `config_yaml`: sources/config.yaml (exists at the referenced commit, includes `buildSmallCap: true`)

No further action required.
