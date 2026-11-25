"""Fridge Roast: One Line, Biggest Laugh — a make.fun entry.

Prints exactly one line, 200 characters at most, roasting a smart
fridge: its app, its firmware updates, its camera, its opinions.
"""

LINE = (
    "My smart fridge has a camera, three apps and strong opinions "
    "about my milk, yet somehow never once mentioned the ice maker died "
    "two firmware updates ago."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
