import os

FIRST_SENTENCE = "I still wear my daughter's hospital bracelet because it is the only place her name is spelled right."
SECOND_SENTENCE = "This morning it had tightened until my fingers went numb, and her birth date had changed to today."
STORY = f"{FIRST_SENTENCE} {SECOND_SENTENCE}"


def main() -> None:
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
