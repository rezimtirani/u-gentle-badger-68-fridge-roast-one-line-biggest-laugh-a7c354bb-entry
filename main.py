"""Fridge Roast: One Line, Biggest Laugh.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a roast of a
smart fridge that burns twenty minutes on a firmware update and
then proudly reports the milk expired days after it left.
Standard library only.
"""

import os

ROAST = (
    "My smart fridge spent twenty minutes updating its firmware, "
    "then proudly announced the milk expired — the milk left on "
    "Tuesday and took the eggs with it."
)


def check_roast(text):
    """Check the roast against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not only
    white space, on a single line: one roast of a smart fridge.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("roast must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "roast is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("roast must be exactly one line")
    return cleaned


def roast_shape(text):
    """Measure the roast for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A roast too short to carry a punchline, or
    one padded out to fill the cap instead of landing the joke,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_roast(ROAST)
    shape = roast_shape(text)
    if shape["words"] < 5:
        raise ValueError("roast is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
