#!/usr/bin/env python3
"""Safely append a timestamped entry to an exploratory session record."""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path


MARKER = "<!-- explore-software:append-only -->"
SUMMARY = "## Summary"
CONTINUATION_PREFIX = "## Continuation:"


def fail(message: str) -> "None":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(2)


def repository_root(parent: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(parent), "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail("the session file must be inside a Git repository")
    return Path(result.stdout.strip()).resolve()


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def is_closed(text: str) -> bool:
    summary_at = text.rfind(f"\n{SUMMARY}")
    continuation_at = text.rfind(f"\n{CONTINUATION_PREFIX}")
    return summary_at >= 0 and summary_at > continuation_at


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append an immutable raw entry to an exploratory session note."
    )
    parser.add_argument("session_file", type=Path)
    parser.add_argument("--title", required=True, help="Short entry title")
    parser.add_argument(
        "--timestamp",
        help="ISO-8601 timestamp; defaults to the current local time",
    )
    parser.add_argument(
        "--continue",
        dest="continue_session",
        action="store_true",
        help="Begin a continuation after a closed Summary",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    session_file = args.session_file.expanduser()

    if not session_file.exists():
        fail("session file does not exist; create it from the template first")
    if session_file.is_symlink() or not session_file.is_file():
        fail("session file must be a regular, non-symlink file")

    resolved = session_file.resolve()
    root = repository_root(resolved.parent)
    if not is_within(resolved, root):
        fail("resolved session file is outside its Git repository")

    original = resolved.read_text(encoding="utf-8")
    if MARKER not in original:
        fail(f"session file is missing required marker: {MARKER}")

    closed = is_closed(original)
    if closed and not args.continue_session:
        fail("session is closed by a Summary; use --continue to append a continuation")
    if not closed and args.continue_session:
        fail("session is still open; --continue is only valid after a Summary")

    body = sys.stdin.read().strip()
    if not body:
        fail("entry body on standard input is empty")

    if args.timestamp:
        try:
            timestamp = dt.datetime.fromisoformat(args.timestamp).isoformat()
        except ValueError:
            fail("--timestamp must be valid ISO-8601")
    else:
        timestamp = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()

    pieces: list[str] = []
    if original and not original.endswith("\n"):
        pieces.append("\n")
    if closed:
        pieces.append(
            f"\n{CONTINUATION_PREFIX} {timestamp}\n\n"
            f"## Experiments and Findings\n\n{MARKER}\n"
        )
    pieces.append(f"\n## [{timestamp}] {args.title.strip()}\n\n{body}\n")

    with resolved.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("".join(pieces))

    print(f"appended: {resolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
