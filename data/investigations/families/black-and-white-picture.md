# Investigation Report: Black And White Picture

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Black And White Picture |
| Designer | AsiaSoft Inc. |
| License | OFL |
| Date Added | 2018-02-27 |
| Repository URL | None |
| Commit | None |
| Branch | None |
| Config YAML | None |
| Status | no_upstream_repo |

## How URL Found

No upstream repository URL has been found. The METADATA.pb has no `source {}` block.

### Search for upstream repository

The font was added as part of PR #1459 ("korean families r01: added") by Marc Foley on 2018-03-13. The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com". This indicates Aaron Bell (Saja Type Works) was the font engineer who prepared the binaries, but the source files likely came from AsiaSoft Inc.

The copyright string reads: "Copyright (c) 1992-2018 AsiaSoft Inc. Seoul Korea All Rights Reserved." This is a corporate font from AsiaSoft Inc., a Korean company. No public GitHub repository or other source repository could be identified for this font.

A search of the upstream repo cache found no repositories related to "blackandwhitepicture" or "asiasoft".

## How Commit Determined

No commit hash exists because no upstream repository has been identified.

## Config YAML Status

No config.yaml exists. The font binary (`BlackAndWhitePicture-Regular.ttf`) is a static TTF file (not a variable font), and no source files (`.glyphs`, `.ufo`, `.designspace`, `.sfd`) are known to exist publicly.

## Verification

- **Upstream repo accessible**: No upstream repo found
- **Font binary history**: The font binary was only modified once after the initial add - in a batch metadata deploy operation (76adaf1d2). The original binary from the 2018 Korean batch has remained unchanged.

## Confidence Level

**HIGH** (for the no_upstream_repo status) - This appears to be a corporate font from AsiaSoft Inc. with no public source repository. The copyright dates back to 1992, suggesting this is a proprietary font released under OFL for Google Fonts without public source files.

## Open Questions

1. Does AsiaSoft Inc. have any public repository for this font? The company appears to specialize in Korean fonts but no GitHub or other public VCS presence was found.
2. Were source files ever provided to Google Fonts team privately? The font was "mastered by Aaron Bell" which may mean he processed received binaries.

## Notes

- This is one of a batch of Korean fonts added in March 2018 by Marc Foley (PR #1459), mastered by Aaron Bell.
- The batch included many Korean fonts from various designers/companies.
- The font is a display font with a scratchy, nostalgic black-and-white photo texture.
- The DESCRIPTION mentions a matching Latin font (Flavors) built into the font.
- At 9.6 MB, this is a large font file (typical for Korean fonts with thousands of glyphs).
- Without a public upstream repo, this family cannot be rebuilt from source.
