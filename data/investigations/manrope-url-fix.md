# Investigation: Manrope — Broken repository_url

**Date**: 2026-02-25
**Issue**: gfonts_agents-kn6
**Family**: Manrope

## Problem

METADATA.pb has `repository_url: "https://github.com/sharanda/manrope"` which is 404.
The user `sharanda` (Michael Sharanda) still exists on GitHub but has 0 public repos.

## Investigation

### google/fonts history

The last Manrope update was PR #3642 ("Manrope v4.504 stat fix"), merged 2021-08-26,
by Aaron Bell. The PR body explicitly states:

> "Font repro updated to the UFR format (https://github.com/aaronbell/manrope).
> PR'd to upstream."

### Replacement repo

**`https://github.com/aaronbell/manrope`** (HTTP 200)

- Fork of `davelab6/manrope`, which was itself forked from `sharanda/manrope`
- Contains `sources/config.yaml` and `sources/Manrope.glyphs`
- Last commit: `6f81ebecdf65e4463b798cc07b16a4f8d5216917` (2021-07-22) — "Rebuilding Static instances with autohinting"
- The config.yaml has proper gftools-builder configuration with STAT table entries

### Identifying the onboarding commit

PR #3642 was merged on 2021-08-26. The repo's latest commit (6f81ebe) is from
2021-07-22, predating the PR merge. The commit message "Rebuilding Static instances
with autohinting" and the UFR conversion commits (46f712f, 2021-06-30) match the
PR description of converting to UFR format.

The commit `6f81ebecdf65e4463b798cc07b16a4f8d5216917` is the HEAD and the most
likely candidate for the onboarding commit, as it's the latest commit and the
PR was about this UFR conversion.

### Alternative: davelab6/manrope

`https://github.com/davelab6/manrope` (HTTP 200) is the older fork. It does NOT
have a config.yaml and contains the pre-UFR source. Not suitable as the upstream.

## Decision

**Update `repository_url` to `https://github.com/aaronbell/manrope`**

- Commit: `6f81ebecdf65e4463b798cc07b16a4f8d5216917`
- config_yaml: `sources/config.yaml`
- Branch: master (default)

## Risk

The aaronbell/manrope repo is itself a fork and may not be actively maintained.
However, it's the repo explicitly referenced in the google/fonts PR that last
updated Manrope, making it the canonical upstream for the currently deployed version.

## Action

1. Update METADATA.pb `repository_url`, `commit`, and `config_yaml`
2. Update tracking in gfonts_library_sources.json
