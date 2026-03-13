# gfonts_agents — Project Guidelines

## Shared Policies
All cross-project policies are in `/mnt/shared/GoogleFonts/CLAUDE.md`.
Read that file at the start of every session. Those policies apply here.

---

## Context

The Google Fonts project stores binary font files (.ttf) in the `google/fonts` repository (https://github.com/google/fonts). Each was generated from source project files in upstream repositories.

### Goals

1. **Primary goal**: Collect 100% of upstream repository URLs and document them in METADATA.pb files
2. Verify that `repository_url` fields point to valid repositories
3. Verify that commit hashes in METADATA.pb match the commits originally used for onboarding
4. Verify that upstream repos have a `config.yaml` file with gftools-builder configuration

## Tech Stack

- Static site (HTML, CSS, vanilla JavaScript)
- No build tools or frameworks
- Must be compatible with GitHub Pages

## Development

Run locally with `./run.sh` (uses Python's http.server).

## Auto-Push Policy (STRICT)

Always `git push origin main` after committing to this repo. Do not wait to be asked. Push website updates, investigation reports, and data changes immediately after each commit — don't batch them.

## Continuous Investigation (STRICT)

After finishing each batch of investigations, immediately start the next batch without waiting for user instruction. Continue until full coverage of the entire Google Fonts library is achieved.

## Token Budget (STRICT)

Always reserve 20% of the weekly token quota (and at least 5% of the current week's remaining quota) for non-investigation queries. Be mindful of token consumption when running investigation batches. Weekly quota resets Friday 6:00 AM GMT+0.

## Daily Draft PRs

Open a draft PR to google/fonts for each day of investigation research. Update it gradually with additional commits throughout the day. User reviews at end of each day.

## Dashboard Sync

Keep the "Beads Issues" tab always synced. Run `scripts/sync_beads.sh` after beads changes.

## Git Lock for Parallel Agents

When running parallel subagents that commit/push, use a file-based lock (`/tmp/gfonts_agents_git.lock`) to prevent simultaneous git operations. Subagents write reports only; the main agent handles all commits and pushes sequentially.

## Message Logging & Friday Status

See hub CLAUDE.md for the full policy. Writes to `data/message_log.json` in this repo.
