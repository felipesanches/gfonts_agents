# Investigation: Bellota Text

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bellota Text |
| Slug | bellota-text |
| License Dir | ofl |
| Repository URL | https://github.com/kemie/Bellota-Font |
| Commit Hash | db900d27103a2e9b37b76ef32386fbf9691ecac6 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/kemie/Bellota-Font"
  commit: "db900d27103a2e9b37b76ef32386fbf9691ecac6"
}
```

## Investigation

Bellota Text was added to google/fonts on 2020-01-16 in commit `d22365f72284a6af8f644aecbe74a680c55c2014` ("Added Bellota and Bellota Text") by Yanone. PR #2309 in google/fonts was submitted with the body "Upstream PR is merged." — referring to PR #5 in the upstream repo, which was merged just 13 minutes before the google/fonts submission.

The upstream commit `db900d27103a2e9b37b76ef32386fbf9691ecac6` is a merge commit titled "Merge pull request #5 from yanone/master", dated 2020-01-16 15:43:54 +0100. The google/fonts addition was at 15:56:07 +0100 (same day, same author Yanone). This timing confirms the commit: Yanone merged the upstream PR, then immediately submitted to google/fonts.

The upstream repository has no `config.yaml` at any commit. However, an **override config.yaml** exists in the google/fonts family directory at `ofl/bellotatext/config.yaml`:

```yaml
sources:
  - src/Bellota.glyphs
familyName: Bellota Text
buildVariable: false
```

Since the local override exists, the `config_yaml` field is correctly omitted from METADATA.pb (google-fonts-sources auto-detects local overrides).

At the recorded commit, the upstream repo has `src/Bellota.glyphs` and multiple `src/Bellota-*.ufo` files as buildable sources. Note that Bellota Text and Bellota share the same upstream repository. The repo is cached at `upstream_repos/fontc_crater_cache/kemie/Bellota-Font`.

The upstream repo has received many additional commits since onboarding (Bellota 5.0, Cyrillic additions, etc.). Any future updates would require a separate review process.

## Conclusion

Status is complete. The METADATA.pb source block has `repository_url` and `commit`. The `config_yaml` field is correctly omitted because a local override config.yaml exists in the google/fonts family directory. No action needed.
