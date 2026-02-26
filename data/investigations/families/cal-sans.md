# Investigation Report: Cal Sans

## Source Data

| Field | Value |
|---|---|
| Family Name | Cal Sans |
| Designer | Mark Davis, Cal.com Inc. |
| License | OFL |
| Repository URL | https://github.com/calcom/font |
| Commit Hash | `b833fb1129ba8c62c29b1d9f70861c77204affe2` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Status | complete |

## How URL Found

The repository URL `https://github.com/calcom/font` is recorded in the METADATA.pb `source {}` block and matches the copyright notice: "Copyright 2021 The Cal Sans Project Authors (https://github.com/calcom/font)". The font was added relatively recently (2025-03-19).

## How Commit Determined

The commit `b833fb1129ba8c62c29b1d9f70861c77204affe2` was explicitly referenced in the initial onboarding commit `59e4eb6ee` in google/fonts:

> Taken from the upstream repo https://github.com/calcom/font at commit https://github.com/calcom/font/commit/b833fb1129ba8c62c29b1d9f70861c77204affe2.

This is the HEAD of the upstream repository's main branch ("Merge pull request #7 from 0xflotus/patch-1"). The font has had no updates since initial onboarding.

## Config YAML Status

The config file `sources/config.yaml` exists at the recorded commit in the upstream repo. It contains:

```yaml
sources:
  - Cal-Sans.glyphs
familyName: "Cal Sans"
cleanUp: True
```

This is a static font (single weight, Regular only), built from `Cal-Sans.glyphs` source.

## Verification

- **Commit exists in upstream repo**: Yes, verified as HEAD of main branch
- **Config YAML exists at commit**: Yes, `sources/config.yaml` confirmed
- **Repository URL accessible**: Yes
- **gftools-packager commit message**: Explicitly cites the commit hash in the onboarding commit `59e4eb6ee`
- **Font file path in METADATA.pb**: `fonts/ttf/CalSans-Regular.ttf` matches the expected build output

## Confidence Level

**High** - All data is consistent and directly cross-verified through the gftools-packager onboarding commit message.

## Open Questions

None. All source data is complete and verified.
