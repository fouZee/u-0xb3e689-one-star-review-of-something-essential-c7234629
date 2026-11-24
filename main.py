"""One-Star Review of Something Essential — entry program.

Writes a single deadpan one-star review of gravity to /output/entry.txt.

The review: gravity never misses, which is exactly the complaint — drop a
phone and it does its job flawlessly, face-down, screen first. One joke,
told straight, with the sting in the last few words.
"""

from pathlib import Path

ENTRY = "Gravity works fine until you drop your phone, then it works perfectly and your screen cracks. One star."
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    """Enforce the competition gate before anything is written.

    The sealed gate accepts UTF-8 text of 1 to 160 characters, not only
    white space, on a single line. The judge brief adds: deadpan, so no
    exclamation marks doing the work, and one joke told cleanly.
    """
    if not (1 <= len(text) <= 160):
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line, no leading/trailing space")
    if "!" in text:
        raise ValueError("entry must hold the deadpan: no exclamation marks")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Round-trip check: what the judge will read must be exactly the entry.
    if OUTPUT.read_text(encoding="utf-8") != text:
        raise RuntimeError("written entry does not match the review")


if __name__ == "__main__":
    main()
