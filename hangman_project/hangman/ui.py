from colorama import init, Fore, Style

from .ascii_provider import load_ascii_stage

init(autoreset=True)


class UI:
    def __init__(self):
        self.max_attempts = None

    def display_hangman(self, wrong_guesses: int):
        hangman = load_ascii_stage(wrong_guesses, self.max_attempts)
        print(Fore.RED + f"{hangman}\n")

    def display_welcome(self, attempts: int):
        print(Fore.GREEN + Style.BRIGHT + "Welcome to the Hangman game!")
        print(Fore.YELLOW + f"You have {attempts} attempts.")
        print(Style.DIM + "Type /help to show all available commands\n")

    # Difficulty choice
    def display_difficulty_menu(self):
        print(Fore.CYAN + "Please choose difficulty:")
        print("1) easy -- 10 attempts")
        print("2) medium -- 6 attempts")
        print("3) hard -- 4 attempts")

    def prompt_difficulty_choice(self) -> str:
        return input(Fore.CYAN + "Your choice (1/2/3): " + Style.RESET_ALL).strip()

    def notify_invalid_difficulty(self):
        print(Fore.RED + "Invalid choice. Defaulting to medium difficulty.")

    # Game messages
    def display_current_guess(self, current: str, attempts: int):
        print(Fore.MAGENTA + f"Current guess: {current}")
        print(Fore.MAGENTA + f"Attempts left: {attempts}")

    def prompt_guess(self) -> str:
        return input(Fore.CYAN + "Guess a letter or word: " + Style.RESET_ALL).strip().lower()

    def notify_invalid_input(self):
        print(Fore.RED + "Please enter a single letter, word or command starting with '/'.")

    def notify_already_guessed(self):
        print(Fore.YELLOW + "You've already guessed that letter.")

    def notify_incorrect_letter(self):
        print(Fore.RED + "Incorrect letter guess.")

    def notify_incorrect_word(self):
        print(Fore.RED + "Incorrect word guess.")

    def notify_incorrect_command(self):
        print(Fore.RED + "Invalid command. Type /help to see all available commands")

    # Commands messages
    def display_help(self):
        print(Fore.GREEN + "Available commands:")
        print(Fore.YELLOW + "/help    " + Style.RESET_ALL + "- Show this help message")
        print(Fore.YELLOW + "/quit    " + Style.RESET_ALL + "- Quit the current game")
        print(Fore.YELLOW + "/status  " + Style.RESET_ALL + "- Show current game status")
        print(Fore.YELLOW + "/word    " + Style.RESET_ALL + "- (DEBUG) Reveal the hidden word")

    def display_status(self, current: str, attempts: int, guessed: set, difficulty: str):
        print(Fore.GREEN + "\nCurrent statistics:")
        print(Fore.MAGENTA + f"Your current guess: {current}")
        print(Fore.MAGENTA + f"Attempts left: {attempts}")
        print(Fore.MAGENTA + f"Guessed letters: {', '.join(sorted(guessed))}")
        print(Fore.MAGENTA + f"Game difficulty: {difficulty}\n")

    def display_quit(self):
        print(Fore.CYAN + "Quitting...")

    def display_hidden_word(self, word: str):
        print(Fore.YELLOW + f"Hidden word: {word}")

    # End game states
    def display_win(self, word: str, attempts: int):
        print(Fore.GREEN + Style.BRIGHT + "\nCongratulations, you guessed the word correctly!")
        print(Fore.CYAN + f"The word was: {word}")
        print(Fore.CYAN + f"You had {attempts} attempts left.\n")

    def display_lose(self, word: str, correct: int, total: int):
        print(Fore.RED + Style.BRIGHT + "\nSorry, you weren't able to guess the word.")
        print(Fore.CYAN + f"The word was: {word}")
        print(Fore.CYAN + f"You guessed {correct} out of {total} letters correctly.\n")

    def set_max_attempts(self, max_attempts: int):
        self.max_attempts = max_attempts