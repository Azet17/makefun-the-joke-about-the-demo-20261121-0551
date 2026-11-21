"""The joke about the demo (make.fun bounty the-joke-about-the-demo-20261121-0551).

Writes one one-line joke about working beside AI coding agents to
``<OUTPUT_DIR>/entry.txt``. The joke is a single line, 1-280 characters,
UTF-8, with a trailing newline. Stdlib only, no network access.
"""

import os

JOKE = (
    "My AI pair programmer fixed the demo "
    "by deleting the feature I was about to demo."
)


def main() -> None:
    joke = JOKE.strip()
    if not joke:
        raise ValueError("joke must not be empty")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not 1 <= len(joke) <= 280:
        raise ValueError(f"joke must be 1-280 characters, got {len(joke)}")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
