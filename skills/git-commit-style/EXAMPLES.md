# Git Commit Style Examples & Guidelines

This reference details the prefix conventions, provides code integration examples, and demonstrates good vs. bad commit messages.

## Prefix Type Reference

| Prefix | Usage |
| :--- | :--- |
| `feat` | Adding a new user-facing or developer-facing feature |
| `bugfix` | Resolving a bug or error (prefer `bugfix` over `fix`) |
| `refactor` | Code restructuring without behavior changes (no new features or bug fixes) |
| `chore` | Maintenance tasks, library upgrades, configuration tweaks, or minor cleanups |
| `test` | Adding, updating, or correcting test cases |
| `ci` | Changes to Continuous Integration configurations (GitHub Actions, GitLab CI, etc.) |
| `cd` | Changes to Continuous Deployment setups or deployment scripts |
| `docs` | Documentation modifications (README, API docs, comments) |
| `style` | Layout, formatting, or stylistic adjustments (no logic change, e.g. semicolon addition) |
| `perf` | Optimizations targeting run-time performance, memory usage, or bundle size |
| `revert` | Reverting a previous commit |

## Examples

### Good Commit Messages
- `bugfix: fix volume slider alignment` (lowercase, clear description)
- `ci: removed unused variables` (describes pipeline/lint cleanup)
- `docs: readme updated` (documentation update)
- `refactor!: migrate to v2 database schema` (breaking change denoted by `!`)

### Bad Commit Messages
- `Fix volume slider alignment` (capitalized, does not start with allowed prefix)
- `feat(volume): Controllable Volume.` (capitalized subject, ends with a period)
- `bug: fixed volume slider` (`bug` is not in the allowed prefix list; use `bugfix`)
- `feat(audio) add controllable volume` (missing colon after the scope)
- `refactor: optimize DB queries` (optimizations should use `perf` prefix instead of `refactor`)

---

## Setting up a Git Commit-Msg Hook

To automatically validate commit messages before they are finalized, install a `commit-msg` hook in your repository.

### For Windows (PowerShell/CMD or Bash)

Create or edit `.git/hooks/commit-msg` and add the following:

```bash
#!/bin/sh
# Call the validator script, passing the path to the commit message file
python C:/Users/ITWORK/.gemini/config/skills/git-commit-style/scripts/validate_commit_msg.py "$1"
```

If using PowerShell explicitly in the hook:

```powershell
#!/usr/bin/env pwsh
python C:/Users/ITWORK/.gemini/config/skills/git-commit-style/scripts/validate_commit_msg.py $args[0]
```

If the validation script exits with `1` (failure), Git will abort the commit.
