from .config_loader import get_attempts_for_difficulty
from .word_provider import get_random_word

def choose_difficulty():
    print("Please choose difficulty:")
    print("1) easy -- 10 attempts")
    print("2) medium -- 6 attempts")
    print("3) hard -- 4 attempts")

    choice = input("Your choice (1/2/3): ").strip()
    difficulty_map = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }
    if choice not in difficulty_map:
        print("Invalid choice. Defaulting to medium difficulty.")
    return difficulty_map.get(choice, "medium")


class Game:
    def __init__(self):
        self.word = get_random_word()
        self.difficulty = choose_difficulty()
        self.attempts = get_attempts_for_difficulty(self.difficulty)
        self.guessed_letters = set()
        self.current_guess_state = "_" * len(self.word)
        self.commands = {
            "/help": self.command_help,
            "/quit": self.command_quit,
            "/status": self.command_status,
            "/word": self.command_word,
        }

    def play(self) -> bool:
        print("Welcome to the Hangman game!")

        print(f"In your game you'll have {self.attempts} attempts!")
        print("Type /help to show all available commands")

        win = False
        while self.attempts > 0 and not win:
            print(f"Current guess: {self.current_guess_state}")
            print(f"Attempts left: {self.attempts}")
            user_guess = input("Guess a letter: ").strip().lower()

            if user_guess.startswith("/"):
                should_decrease = self.handle_command(user_guess)

            elif user_guess.isalpha():
                should_decrease = (
                    self.handle_letter(user_guess)
                    if len(user_guess) == 1
                    else self.handle_word(user_guess)
                )

            else:
                print("Please enter a single letter, word or command starting with '/'.")
                should_decrease = False

            if should_decrease:
                self.attempts -= 1

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
                if char == user_guess or char == self.current_guess_state[i]:
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
        missing_letters = self.current_guess_state.count('_')
        print(f"You guessed {len(self.word) - missing_letters} out of {len(self.word)} letters correctly.")

    # Commands
    def command_help(self):
        print("📘 Available commands:")
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
