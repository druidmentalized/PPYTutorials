import random

from .config_loader import get_words_file_path


def get_random_word() -> str:
    words_path = get_words_file_path()
    with open(words_path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)
