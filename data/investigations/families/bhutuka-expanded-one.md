# Investigation: BhuTuka Expanded One

## Summary

| Field | Value |
|-------|-------|
| Family Name | BhuTuka Expanded One |
| Slug | bhutuka-expanded-one |
| License Dir | ofl |
| Repository URL | https://github.com/erinmclaughlin/BhuTuka-Extended-One |
| Commit Hash | ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6 |
| Config YAML | sources/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/erinmclaughlin/BhuTuka-Extended-One"
  commit: "ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BhuTukaExpandedOne-Regular.ttf"
    dest_file: "BhuTukaExpandedOne-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The font was added to google/fonts on 2022-01-28 in commit `b52c85605` (PR #4222) by Yanone (Jens Kutilek), co-authored by Rosalie Wagner. The commit message from the gftools-packager update explicitly states:

> "BhuTuka Expanded One Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/erinmclaughlin/BhuTuka-Extended-One at commit ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6."

The upstream commit `ac2ad17` is verified locally in the cached repo at `/mnt/shared/upstream_repos/fontc_crater_cache/erinmclaughlin/BhuTuka-Extended-One`. The commit message is: "Merge pull request #4 from yanone/master". This is the only commit in the repository and the HEAD of master, making verification trivial.

The config file is named `builder.yaml` (not `config.yaml`) and is located at `sources/builder.yaml`. Its contents at the recorded commit:

```yaml
sources:
  - BhuTukaExpandedOne-Regular.glyphs
outputDir: "../fonts"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration targeting the Glyphs source file `BhuTukaExpandedOne-Regular.glyphs` in the `sources/` directory.

The METADATA.pb source block is fully populated with `repository_url`, `commit`, `config_yaml: "sources/builder.yaml"`, `branch: "master"`, and `files{}` mappings for OFL.txt, DESCRIPTION.en_us.html, and the TTF file.

The repository URL is also confirmed by the copyright field: "Copyright 2017 The BhuTuka Expanded One Project Authors (https://github.com/erinmclaughlin/BhuTuka-Extended-One)".

## Conclusion

The source metadata is complete. The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` — all correct and verified against the local cached upstream repo. No action needed.
