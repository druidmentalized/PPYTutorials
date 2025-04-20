from colorama import init, Fore, Style

from .ascii_provider import load_ascii_stage

init(autoreset=True)


class UI:
    def __init__(self):
        self.max_attempts = None

    def set_max_attempts(self, max_attempts: int):
        self.max_attempts = max_attempts

    def display_separator(self):
        print(Style.DIM + "-" * 50 + "")

    def display_hangman(self, wrong_guesses: int):
        hangman = load_ascii_stage(wrong_guesses, self.max_attempts)
        print(Fore.LIGHTRED_EX + f"{hangman}")

    def display_welcome(self, attempts: int, is_strict: bool):
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Welcome to the Hangman game!")
        print(Fore.LIGHTYELLOW_EX + f"You have {attempts} attempts.")
        print(Fore.LIGHTYELLOW_EX + f"Your game mode is '{("Strict" if is_strict else "Moderate")}'.")
        print(Style.DIM + "Type /help to show all available commands")

    # Difficulty & Strictness choice
    def display_difficulty_menu(self):
        print(Fore.LIGHTGREEN_EX + "Please choose difficulty:")
        print(f"1) easy -- 10 attempts")
        print(f"2) medium -- 6 attempts")
        print(f"3) hard -- 4 attempts")

    def prompt_difficulty_choice(self) -> str:
        return input(Fore.LIGHTGREEN_EX + "Your choice (1/2/3): " + Style.RESET_ALL).strip()

    def notify_invalid_difficulty(self):
        print(Fore.LIGHTRED_EX + "Invalid choice. Defaulting to medium difficulty.")

    def display_strictness_menu(self):
        print(Fore.LIGHTGREEN_EX + "Please choose strictness:")
        print(f"1) Strict -- attempts decreased for every guess")
        print(f"2) Moderate -- attempts decreased only for incorrect guesses")

    def prompt_strictness_choice(self) -> str:
        return input(Fore.LIGHTGREEN_EX + "Your choice (1/2): " + Style.RESET_ALL).strip()

    def notify_invalid_strictness(self):
        return print(Fore.LIGHTRED_EX + "Invalid choice. Defaulting to moderate strictness.")

    # Game messages
    def display_current_guess(self, current: str, attempts: int):
        self.display_separator()
        print(Fore.LIGHTGREEN_EX + f"Current guess: {current}")
        print(Fore.LIGHTGREEN_EX + f"Attempts left: {attempts}")

    def prompt_guess(self) -> str:
        return input(Fore.LIGHTGREEN_EX + "Guess a letter or word: " + Style.RESET_ALL).strip().lower()

    def notify_invalid_input(self):
        print(Fore.LIGHTRED_EX + "Please enter a single letter, word or command starting with '/'.")

    def notify_already_guessed(self):
        print(Fore.LIGHTYELLOW_EX + "You've already guessed that letter.")

    def notify_incorrect_letter(self):
        print(Fore.LIGHTRED_EX + "Incorrect letter guess.")

    def notify_incorrect_word(self):
        print(Fore.LIGHTRED_EX + "Incorrect word guess.")

    def notify_incorrect_command(self):
        print(Fore.LIGHTRED_EX + "Invalid command. Type /help to see all available commands.")

    # Commands messages
    def display_help(self):
        self.display_separator()
        print(Fore.LIGHTGREEN_EX + "Available commands:")
        print(Fore.LIGHTYELLOW_EX + "/help    " + Style.RESET_ALL + "- Show this help message")
        print(Fore.LIGHTYELLOW_EX + "/quit    " + Style.RESET_ALL + "- Quit the current game")
        print(Fore.LIGHTYELLOW_EX + "/status  " + Style.RESET_ALL + "- Show current game status")
        print(Fore.LIGHTYELLOW_EX + "/word    " + Style.RESET_ALL + "- (DEBUG) Reveal the hidden word")

    def display_status(self, current: str, attempts: int, guessed: set, difficulty: str):
        self.display_separator()
        print(Fore.LIGHTGREEN_EX + "Current statistics:")
        print(Fore.LIGHTGREEN_EX + f"Your current guess: {current}")
        print(Fore.LIGHTGREEN_EX + f"Attempts left: {attempts}")
        print(Fore.LIGHTGREEN_EX + f"Guessed letters: {', '.join(sorted(guessed))}")
        print(Fore.LIGHTGREEN_EX + f"Game difficulty: {difficulty}")

    def display_quit(self):
        print(Fore.LIGHTCYAN_EX + "Quitting...")

    def display_hidden_word(self, word: str):
        print(Fore.LIGHTYELLOW_EX + f"Hidden word: {word}")

    # End game states
    def display_win(self, word: str, attempts: int):
        self.display_separator()
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Congratulations, you guessed the word correctly!")
        print(Fore.GREEN + f"The word was: {word}")
        print(Fore.GREEN + f"You had {attempts} attempts left.")

    def display_lose(self, word: str, correct: int, total: int):
        self.display_separator()
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Sorry, you weren't able to guess the word.")
        print(Fore.RED + f"The word was: {word}")
        print(Fore.RED + f"You guessed {correct} out of {total} letters correctly.")
