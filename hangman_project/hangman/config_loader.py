import configparser
import os


def get_attempts_for_difficulty(difficulty: str) -> int:
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(__file__), "..", "config.ini")
    config.read(path)
    return int(config["Attempts"][difficulty])