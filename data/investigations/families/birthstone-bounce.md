# Investigation: Birthstone Bounce

## Summary

| Field | Value |
|-------|-------|
| Family Name | Birthstone Bounce |
| Slug | birthstone-bounce |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/birthstone-bounce |
| Commit Hash | db48de44b60017495c71a024aa2c079d70869225 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/birthstone-bounce"
  commit: "db48de44b60017495c71a024aa2c079d70869225"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BirthstoneBounce-Regular.ttf"
    dest_file: "BirthstoneBounce-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BirthstoneBounce-Medium.ttf"
    dest_file: "BirthstoneBounce-Medium.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

The fonts were added to google/fonts in commit `8bd4436fd` (September 8, 2021, PR #3793), titled "Birthstone Bounce: Version 1.010; ttfautohint (v1.8.3) added". The commit message states the files were "taken from the upstream repo https://github.com/googlefonts/birthstone-bounce at commit https://github.com/googlefonts/birthstone-bounce/commit/f45812daabb656a9d1d8c19c211fc19c26c95c07."

However, the current METADATA.pb has commit `db48de44b60017495c71a024aa2c079d70869225`, which was set by commit `19cdcec59` (a batch import from fontc_crater targets list). The upstream repository cache at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/birthstone-bounce` is a shallow clone with only a single commit (`db48de44`, "outline fixes in acute and ring", dated September 17, 2021), meaning the original commit `f45812da` referenced in the google/fonts onboarding commit no longer exists in the accessible history.

The commit `db48de44` is 9 days later than the onboarding event, suggesting the upstream repository was updated after onboarding. Since `db48de44` is the only available commit in the shallow clone, it is the closest we can verify.

The `sources/config.yaml` file exists in the upstream repository with content:
```yaml
sources:
    - BirthstoneBounce.glyphs
familyName: Birthstone Bounce
outputDir: "../fonts"
buildVariable: false
```

The source block in METADATA.pb is complete and correctly references this config file.

## Conclusion

The METADATA.pb source block is complete with repository URL, commit hash, and config_yaml path. The commit hash `db48de44b60017495c71a024aa2c079d70869225` is the only available commit in the upstream repo (shallow clone). The original onboarding commit `f45812daabb656a9d1d8c19c211fc19c26c95c07` (referenced in the google/fonts PR #3793 commit body) is no longer reachable in the local cache. Confidence is MEDIUM due to this discrepancy. No further action needed.
