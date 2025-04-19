import os

from .config_loader import get_ascii_dir_path

ascii_dir = get_ascii_dir_path()


def load_ascii_stage(wrong_guesses: int, max_attempts: int) -> str:
    all_files = [f for f in os.listdir(ascii_dir) if f.startswith("stage_") and f.endswith(".txt")]
    total_stages = len(all_files) - 1

    ratio = wrong_guesses / max_attempts if max_attempts else 1
    stage_index = min(round(ratio * total_stages), total_stages)

    stage_path = os.path.join(ascii_dir, f"stage_{stage_index}.txt")
    if not os.path.exists(stage_path):
        return f"[Missing ASCII art for stage {stage_index}]"

    with open(stage_path, "r", encoding="utf-8") as file:
        return file.read()