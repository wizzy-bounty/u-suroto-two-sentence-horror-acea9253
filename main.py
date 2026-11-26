import os

STORY = "The embalmer pried tomorrow's bus ticket from the dead woman's fist. It was already punched for the seat beside his, and the stub bore his home stop."


def story_text():
    return STORY


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as handle:
        handle.write(story_text().encode("utf-8"))


if __name__ == "__main__":
    main()
