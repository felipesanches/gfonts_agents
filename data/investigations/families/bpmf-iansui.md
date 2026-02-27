# Investigation: Bpmf Iansui

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bpmf Iansui |
| Slug | bpmf-iansui |
| License Dir | ofl |
| Repository URL | https://github.com/ButTaiwan/bpmfvs |
| Commit Hash | 20f741c18bb917b63576293906c01e82ddfce032 |
| Config YAML | none |
| Status | missing_config |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/ButTaiwan/bpmfvs"
  commit: "20f741c18bb917b63576293906c01e82ddfce032"
}
```

## Investigation

Bpmf Iansui is a Traditional Chinese handwriting font with Bopomofo phonetic annotations, designed by But Ko, added to Google Fonts on 2026-01-30. It is one of three Bpmf family variants (alongside Huninn and Zihi Kai Std) from the same upstream repository. The base font (Iansui) comes from `github.com/ButTaiwan/iansui`.

### Git History

The font was initially added by google/fonts commit `0fbc58136` (2026-01-30, "Adding Bpmf Iansui") via PR #10172 by Aaron Bell. The font binary was updated by commit `589446f9f` (2026-02-09, "Update BpmfIansui-Regular.ttf - Updating with various fixes"). Further metadata-only fixes followed: `16db82397` (newline fix), `ae7a73564` (copyright fix), `1f665adf7` (URL fix).

The source block was added by google/fonts commit `a93a721ef` ("Bpmf Iansui: add source block to METADATA.pb"), which also added an `upstream_info.md` file.

The commit hash `20f741c18bb917b63576293906c01e82ddfce032` was added by automation commit `9a14639f3` (2026-02-25).

### Upstream Repository

The bpmfvs repo (`ButTaiwan/bpmfvs`) is not cached locally. The fonts were built in Aaron Bell's fork at `https://github.com/aaronbell/bpmfvs`. PR #10172 states: "At present, these are being built in https://github.com/aaronbell/bpmfvs, but will be transitioned upstream to https://github.com/ButTaiwan/bpmfvs once the rest of the fonts' build systems are modernized."

The commit `20f741c18bb` is the HEAD of `ButTaiwan/bpmfvs` from 2025-12-13, which predates the actual build by over a month.

### Build System

Same as all Bpmf families — a custom Ruby-based build system (`make_font.rb`) that is incompatible with gftools-builder. No config.yaml can be created.

### Verification

- Repository URL: Correct as canonical upstream (but fonts were built from Aaron Bell's fork)
- Commit hash: Incorrect — `20f741c` predates the actual build; the correct commit is in `aaronbell/bpmfvs` around 2026-02-09
- Config YAML: Cannot be created (custom Ruby build system)
- Local cache: Neither repo is cached locally
- Note: The `ButTaiwan/iansui` repo (base font source) IS cached at `/mnt/shared/upstream_repos/fontc_crater_cache/ButTaiwan/iansui/`

## Conclusion

Same fundamental situation as Bpmf Huninn. The repository URL points to the canonical upstream but the fonts were built from Aaron Bell's fork. The commit hash is incorrect. Aaron Bell should be asked to confirm the exact commit used in `aaronbell/bpmfvs` for the Feb 9, 2026 update. No config.yaml can be created due to the custom build system. The status should remain `missing_config` permanently.
