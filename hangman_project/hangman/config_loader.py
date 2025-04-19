import configparser
import os


config = configparser.ConfigParser()
path = os.path.join(os.path.dirname(__file__), "..", "config.ini")
config.read(path)


def get_attempts_for_difficulty(difficulty: str) -> int:
    return int(config["Attempts"][difficulty])

def get_words_file_path() -> str:
    return config["Paths"].get("word_file", "words.txt")

def get_ascii_dir_path() -> str:
    return config["Paths"].get("ascii_dir", "ascii")