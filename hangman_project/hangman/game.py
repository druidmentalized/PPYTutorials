from .ui import *
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

    def play(self) -> bool:
        self.ui.display_welcome(self.attempts)
        win = False
        while self.attempts > 0 and not win:
            self.ui.display_current_guess(self.current_guess_state, self.attempts)
            guess = self.ui.prompt_guess()

            if guess.startswith('/'):
                self.handle_command(guess)
                should_decrease = False
            elif guess.isalpha():
                should_decrease = (self.handle_letter(guess) if len(guess) == 1 else self.handle_word(guess))
            else:
                self.ui.notify_invalid_input()
                should_decrease = False

            if should_decrease:
                self.attempts -= 1
                self.wrong_guesses += 1
                self.ui.display_hangman(self.wrong_guesses)

            if self.current_guess_state == self.word:
                win = True

        if win:
            self.handle_win()
        elif self.attempts == 0:
            self.handle_lose()
        return win

    def handle_command(self, user_guess: str) -> bool:
        command = self.commands.get(user_guess.lower())
        if command:
            command()
            return False
        else:
            self.ui.notify_incorrect_command()
            return False

    def handle_letter(self, user_guess: str) -> bool:
        if user_guess in self.guessed_letters:
            self.ui.notify_already_guessed()
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
            self.ui.notify_incorrect_letter()
            return True

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
