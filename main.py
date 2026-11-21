"""Writes the one-line demo joke to /output/entry.txt."""
import os

JOKE = "My AI coding agent fixed the live demo crash in nine seconds: it deleted the demo."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
