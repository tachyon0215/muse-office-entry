#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh: Office Jokes": one
line about office life, under 200 characters.

Chosen from three candidates against the judge brief (genuine joke,
surprise turn, recognition, tight wording, freshness): the reply-all
version won because the instruction meant to stop the flood is what
causes it, and the escalation ends somewhere unseen - the thread
earning its own follow-up meeting.
"""
import os
from pathlib import Path

JOKE = (
    "The reply-all said 'please stop replying all,' and by noon it had "
    "400 replies, two apologies, and its own follow-up meeting."
)

TEXT = JOKE + "\n"

MIN_CHARS = 1
MAX_CHARS = 199


def validate(text: str) -> None:
    """Reject anything the gate would reject, before it reaches disk."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    validate(TEXT)
    payload = TEXT.encode("utf-8")
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    written = target.read_bytes()
    if written != payload:
        raise IOError(f"read-back mismatch: wrote {len(payload)} bytes, "
                      f"read {len(written)} bytes")


if __name__ == "__main__":
    main()
