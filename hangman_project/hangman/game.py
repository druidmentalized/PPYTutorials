from colorama import Fore

from .ui import UI
from .config_loader import get_attempts_for_difficulty
from .word_provider import get_random_word

def choose_difficulty(ui: UI) -> str:
    ui.display_difficulty_menu()
    choice = ui.prompt_difficulty_choice()
    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    difficulty = mapping.get(choice)
    if difficulty is None:
        ui.notify_invalid_difficulty()
        difficulty = "medium"
    return difficulty


class Game:
    def __init__(self):
        temp_ui = UI(max_attempts=10)
        self.difficulty = choose_difficulty(temp_ui)
        self.attempts = get_attempts_for_difficulty(self.difficulty)
        self.max_attempts = self.attempts
        self.ui = UI(max_attempts=self.max_attempts)

        self.word = get_random_word()
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.current_guess_state = '_' * len(self.word)
        self.commands = {
            '/help': self.ui.display_help,
            '/quit': self.command_quit,
            '/status': lambda: self.ui.display_status(
                self.current_guess_state, self.attempts, self.guessed_letters, self.difficulty
            ),
            '/word': lambda: self.ui.display_hidden_word(self.word),
        }

    def play(self) -> bool:
        self.ui.display_welcome(self.attempts)
        win = False
        while self.attempts > 0 and not win:
            self.ui.display_current_guess(self.current_guess_state)
            self.ui.display_attempts_left(self.attempts)
            guess = self.ui.prompt_guess()

            if guess.startswith('/'):
                self.commands.get(
                    guess.lower(),
                    lambda: print(Fore.RED + "Invalid command. Type /help to see all available commands")
                )()
                should_decrease = False
            elif guess.isalpha():
                should_decrease = (
                    self.handle_letter(guess) if len(guess) == 1 else self.handle_word(guess)
                )
            else:
                self.ui.notify_invalid_input()
                should_decrease = False

            if should_decrease:
                self.attempts -= 1
                self.wrong_guesses += 1
                self.ui.display_ascii_art(self.wrong_guesses)

            if self.current_guess_state == self.word:
                win = True

        if win:
            self.handle_win()
        else:
            self.handle_lose()
        return win

    def handle_command(self, user_guess: str) -> bool:
        command = self.commands.get(user_guess.lower())
        if command:
            command()
            return False
        else:
            print("Invalid command. Type /help to see all available commands")
            return False

    def handle_letter(self, user_guess: str) -> bool:
        if user_guess in self.guessed_letters:
            print("You've already guessed that letter.")
            return False

        self.guessed_letters.add(user_guess)

        if user_guess in self.word:
            new_guess_state = ""
            for i, char in enumerate(self.word):
                if char == user_guess or self.current_guess_state[i] != "_":
                    new_guess_state += char
                else:
                    new_guess_state += "_"
            self.current_guess_state = new_guess_state
            return False
        else:
            print("Incorrect letter guess.")
            return True

    def handle_word(self, user_guess: str) -> bool:
        if user_guess == self.word:
            self.current_guess_state = self.word
            return False
        else:
            print("Incorrect word guess.")
            return True

    def handle_win(self):
        print("Congratulations, you guessed the word correctly!")
        print(f"The word was: {self.word}")
        print(f"You had {self.attempts} attempts left.")

    def handle_lose(self):
        print("Sorry, you weren't able to guess the word.")
        print(f"The word was: {self.word}")
        total = len(self.word)
        missing_letters = self.current_guess_state.count('_')
        correct = total - missing_letters
        print(f"You guessed {correct} out of {total} letter{'s' if correct != 1 else ''} correctly.")

    # Commands
    def command_help(self):
        print("Available commands:")
        for cmd, desc in {
            "/help": "Show this help message",
            "/quit": "Quit the current game",
            "/status": "Show current game status",
            "/word": "(DEBUG) Reveal the hidden word",
        }.items():
            print(f"  {cmd:<8} - {desc}")

    def command_quit(self):
        print("Leaving the game...")
        self.attempts = 0

    def command_status(self):
        print("Current statistics:")
        print(f"Your current guess: {self.current_guess_state}")
        print(f"Attempts left: {self.attempts}")
        print(f"Guessed letters: {self.guessed_letters}")
        print(f"Game difficulty: {self.difficulty}")

    def command_word(self):
        print(f"Hidden word: {self.word}")

def start():
    games = 0
    wins = 0
    while True:
        game = Game()
        if game.play():
            wins += 1
        games += 1
        if input("Would you like to play again? (y/n) ").lower() == "n":
            break
    print("Thank you for playing!")
    print(f"Statistics: {games} games: {wins} wins | {games - wins} loses")


if __name__ == "__main__":
    start()
