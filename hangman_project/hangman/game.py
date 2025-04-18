from config_loader import get_attempts_for_difficulty
from word_provider import get_random_word


def play():
    print("Welcome to the Hangman game!")
    attempts = choose_difficulty()
    print(f"In your game you'll have {attempts} attempts!")
    word = get_random_word()
    print(f"[DEBUG] Current word: {word}")
    user_guess = "_" * len(word)



def choose_difficulty():
    difficulty = prompt_difficulty()
    attempts = get_attempts_for_difficulty(difficulty)
    return attempts


def prompt_difficulty() -> str:
    print("""
    Please choose difficulty:
    1) easy -- 10 attempts
    2) medium -- 6 attempts
    3) hard -- 4 attempts
    """)
    choice = input("Your choice (1/2/3): ").strip()
    difficulty_map = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }
    if choice not in difficulty_map:
        print("Invalid choice. Defaulting to medium difficulty.")
    return difficulty_map.get(choice, "medium")