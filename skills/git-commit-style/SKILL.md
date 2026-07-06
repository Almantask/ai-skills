---
name: git-commit-style
description: Format and validate git commit messages using structured prefixes like chore, bugfix, refactor, feat, test, ci, cd, and docs. Use when writing commit messages, committing code changes, or configuring git commit-msg validation hooks.
---

# Git Commit Message Style

Ensure all repository commits use structured, descriptive prefixes to maintain clean, readable history.

## Quick start

To validate a commit message string:
```powershell
python scripts/validate_commit_msg.py --message "feat(volume): controllable volume"
```

To validate an existing commit message file (e.g. inside a Git hook):
```powershell
python scripts/validate_commit_msg.py path/to/COMMIT_EDITMSG
```

## Git Commit Rules

When writing a commit, follow these rules:

1. **Prefix**: Begin with a lowercase type prefix (`feat`, `bugfix`, `refactor`, `chore`, `test`, `ci`, `cd`, `docs`, `style`, `perf`, `revert`).
2. **Breaking Indicator (Optional)**: Place an exclamation mark `!` after the prefix or scope to denote a breaking change (e.g. `feat!: change API structure`).
3. **Delimiter**: Add a colon followed by a space `: `.
4. **Subject**: Summarize the change starting with a lowercase letter or number. Do not end with a period. Keep the subject line under 72 characters.
5. **Separation**: Leave a blank line between the subject and the body (if a body exists).
6. **Body/Footer**: Wrap lines at 72 characters. Use the footer to reference issues/PRs (e.g. `Fixes #123`).

## Reference

- For a list of detailed prefix descriptions and good/bad examples, see [EXAMPLES.md](EXAMPLES.md).
