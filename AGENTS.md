# Agent Instructions

> ⚠️ **Beads note (2026-04-10):** This repo's beads database is SQLite-era and the
> regular `bd` CLI is **unsafe** against it — writes can corrupt state and even
> "read-only" bd commands mutate the DB. Use **`beads-lite`** (read-only) for
> queries and edit `.beads/issues.jsonl` by hand for writes. Full details and
> command mapping: `~/compartilhado/FSanches/beads-usage-policy.md`.

This project uses **beads** for issue tracking, queried via `beads-lite`.

## Quick Reference

```bash
beads-lite ready              # Find available work
beads-lite show <id>          # View issue details
beads-lite history <id>       # Full audit trail for an issue
beads-lite list --all         # List all issues incl. closed
```

**Writes (create / update status / close / reopen):** `beads-lite` is read-only.
To modify issues, edit `.beads/issues.jsonl` by hand — one issue per line.
Do **not** run `bd update`, `bd close`, `bd create`, or `bd sync` against this
repo.

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** — Add new entries to `.beads/issues.jsonl` for anything that needs follow-up
2. **Run quality gates** (if code changed) — Tests, linters, builds
3. **Update issue status** — Edit `.beads/issues.jsonl` to mark finished work closed and in-progress items updated
4. **PUSH TO REMOTE** — This is MANDATORY:
   ```bash
   git pull --rebase
   git add .beads/issues.jsonl  # if you edited it
   git commit -m "issues: update tracker"
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** — Clear stashes, prune remote branches
6. **Verify** — All changes committed AND pushed
7. **Hand off** — Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing — that leaves work stranded locally
- NEVER say "ready to push when you are" — YOU must push
- If push fails, resolve and retry until it succeeds
- Do NOT run `bd sync` — there is no daemon to sync to; the SQLite DB is frozen by design
