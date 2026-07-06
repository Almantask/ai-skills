#!/usr/bin/env python3
import sys
import re
import argparse

# Allowed prefix types
ALLOWED_TYPES = {
    'feat', 'bugfix', 'refactor', 'chore', 'test',
    'ci', 'cd', 'docs', 'style', 'perf', 'revert'
}

# Regex to parse the first line of the commit message (the subject)
# Format: type(scope)!: subject
COMMIT_RE = re.compile(
    r'^(?P<type>[a-zA-Z0-9_-]+)(?:\((?P<scope>[a-zA-Z0-9_\-\/]+)\))?(?P<breaking>!)?: (?P<subject>.+)$'
)

def validate_message(commit_msg: str) -> list[str]:
    errors = []
    lines = commit_msg.strip().splitlines()
    if not lines:
        return ["Commit message is empty."]

    subject = lines[0].strip()
    
    # 1. Parse subject structure
    match = COMMIT_RE.match(subject)
    if not match:
        return [
            f"Subject line '{subject}' does not match standard format: '<type>(<scope>): <subject>'",
            "Example: feat(volume): controllable volume"
        ]

    parts = match.groupdict()
    msg_type = parts['type']
    msg_scope = parts['scope']
    msg_subject = parts['subject']

    # 2. Validate prefix type
    if msg_type not in ALLOWED_TYPES:
        errors.append(
            f"Type '{msg_type}' is not allowed. Allowed types are: {', '.join(sorted(ALLOWED_TYPES))}"
        )

    # 3. Enforce lowercase/number start for subject
    if msg_subject and msg_subject[0].isupper():
        errors.append(
            f"Subject text '{msg_subject}' must start with a lowercase letter or number. (Found '{msg_subject[0]}')"
        )

    # 4. Enforce no trailing period
    if msg_subject and msg_subject.endswith('.'):
        errors.append(
            f"Subject text '{msg_subject}' must not end with a period."
        )

    # 5. Length recommendation check (soft check, prints warning instead of failing if desired, or fails)
    # Let's enforce subject length <= 72 characters
    if len(subject) > 72:
        errors.append(
            f"Subject line is too long ({len(subject)} characters). Must be 72 characters or fewer."
        )

    # 6. Check for blank line between subject and body if body exists
    if len(lines) > 1:
        if lines[1].strip() != "":
            errors.append(
                "A blank line must separate the commit subject from the commit body."
            )
        
        # Enforce body line wrap recommendation (e.g. 72 characters)
        for i, line in enumerate(lines[2:], start=3):
            if len(line) > 72:
                errors.append(
                    f"Line {i} in the commit body is too long ({len(line)} characters). Recommend wrapping at 72."
                )

    return errors

def main():
    parser = argparse.ArgumentParser(description="Validate Git Commit Message Style.")
    parser.add_argument(
        '-m', '--message',
        help="The commit message text to validate directly."
    )
    parser.add_argument(
        'file',
        nargs='?',
        help="Path to a file containing the commit message (typical Git commit-msg hook argument)."
    )

    args = parser.parse_args()

    commit_content = ""
    if args.message:
        commit_content = args.message
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                commit_content = f.read()
        except Exception as e:
            print(f"Error reading file '{args.file}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Fallback: Read from stdin
        if not sys.stdin.isatty():
            commit_content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)

    # Configure stdout/stderr to use UTF-8 if supported (to handle any unicode in commit messages)
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            pass

    errors = validate_message(commit_content)
    if errors:
        print("[ERROR] Git commit message validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print("[SUCCESS] Git commit message validation passed.")
        sys.exit(0)

if __name__ == '__main__':
    main()
