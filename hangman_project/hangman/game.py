from hangman_project.hangman.ui import UI
from .config_loader import get_attempts_for_difficulty
from .word_provider import get_random_word


class Game:
    def __init__(self):
        self.ui = UI()

        self.difficulty = self.choose_difficulty()
        self.attempts = get_attempts_for_difficulty(self.difficulty)
        self.max_attempts = self.attempts
        self.ui.set_max_attempts(self.max_attempts)

        self.word = get_random_word()
        self.wrong_guesses = 0
        self.is_strict = self.choose_strictness()
        self.guessed_letters = set()
        self.current_guess_state = '_' * len(self.word)
        self.commands = {
            '/help': self.command_help,
            '/quit': self.command_quit,
            '/status': self.command_status,
            '/word': self.command_word,
        }

    def choose_difficulty(self) -> str:
        mapping = {
            "1": "easy",
            "2": "medium",
            "3": "hard"
        }

        self.ui.display_difficulty_menu()
        choice = self.ui.prompt_difficulty_choice()
        difficulty = mapping.get(choice)
        if difficulty is None:
            self.ui.notify_invalid_difficulty()
            return "medium"
        return difficulty

    def choose_strictness(self) -> bool:
        mapping = {
            "1": True,
            "2": False
        }

        self.ui.display_strictness_menu()
        choice = self.ui.prompt_strictness_choice()
        is_strict = mapping.get(choice)
        if is_strict is None:
            self.ui.notify_invalid_strictness()
            return False
        return is_strict

    def play(self) -> bool:
        self.ui.display_welcome(self.attempts, self.is_strict)
        win = False
        while self.attempts > 0 and not win:
            win = self.process_user_guess()
        if win:
            self.handle_win()
        elif self.attempts == 0:
            self.handle_lose()
        return win

    def process_user_guess(self) -> bool:
        self.ui.display_current_guess(self.current_guess_state, self.attempts)
        guess = self.ui.prompt_guess()
        guess_type = self.get_guess_type(guess)

        should_decrease = self.handle_guess_logic(guess, guess_type)

        if should_decrease:
            self.update_after_wrong_guess()

        return self.current_guess_state == self.word

    def get_guess_type(self, guess: str) -> str:
        if guess.startswith('/'):
            return "command"
        elif guess.isalpha():
            return "letter" if len(guess) == 1 else "word"
        else:
            return "invalid"

    def handle_guess_logic(self, guess: str, guess_type: str) -> bool:
        if guess_type == "command":
            self.handle_command(guess)
            return False
        elif guess_type in {"letter", "word"}:
            handler = self.handle_letter if guess_type == "letter" else self.handle_word
            result = handler(guess)
            return True if self.is_strict else result
        else:
            self.ui.notify_invalid_input()
            return not self.is_strict

    def update_after_wrong_guess(self):
        self.attempts -= 1
        self.wrong_guesses += 1
        self.ui.display_hangman(self.wrong_guesses)

    def handle_command(self, user_guess: str):
        command = self.commands.get(user_guess.lower())
        if command:
            command()
        else:
            self.ui.notify_incorrect_command()

    def handle_letter(self, guess: str) -> bool:
        if guess in self.guessed_letters:
            self.ui.notify_already_guessed()
            return False

        self.guessed_letters.add(guess)

        if guess in self.word:
            self.reveal_letter(guess)
            return False
        else:
            self.ui.notify_incorrect_letter()
            return True

    def reveal_letter(self, guess: str):
        self.current_guess_state = "".join(
            c if c == guess or g != "_" else "_"
            for c, g in zip(self.word, self.current_guess_state)
        )

    def handle_word(self, user_guess: str) -> bool:
        if user_guess == self.word:
            self.current_guess_state = self.word
            return False
        else:
            self.ui.notify_incorrect_word()
            return True

    def handle_win(self):
        self.ui.display_win(self.word, self.attempts)

    def handle_lose(self):
        total = len(self.word)
        missing_letters = self.current_guess_state.count('_')
        correct = total - missing_letters
        self.ui.display_lose(self.word, correct, total)

    # Commands
    def command_help(self):
        self.ui.display_help()

    def command_quit(self):
        self.ui.display_quit()
        self.attempts = -1

    def command_status(self):
        self.ui.display_status(self.current_guess_state, self.attempts, self.guessed_letters, self.difficulty)

    def command_word(self):
        self.ui.display_hidden_word(self.word)


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
