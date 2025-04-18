import os
import random

def get_random_word() -> str:
    path = os.path.join(os.path.dirname(__file__), "..", "words.txt")
    with open(path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip()]
    return random.choice(words)