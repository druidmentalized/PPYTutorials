# Hangman Game

A console-based implementation of the classic **Hangman** game, written in Python. The game randomly selects a word from a file, and the player must guess the word one letter at a time (or by full-word guesses) within a limited number of attempts.

This project is modular and cleanly separated into logical components using object-oriented programming. It includes enhanced user interaction via ASCII visuals and optional terminal coloring using `colorama`.

---

## Project Structure

- `hangman_project/`
	- `hangman/` (main package)
	  - **__init__.py**
      - **game.py** — core game logic
      -	**ui.py** — handles output, ASCII art, and terminal styling
	  - **config_loader.py** — reads settings from config.ini
	  - **word_provider.py** — loads a random word from the word list
	- **config.ini** — stores difficulty settings
	- **words.txt** — list of playable words (one per line)
	- `main.py` — program entry point
	- **README.md** — project description and usage instructions

---

## How to Run the Game

1. **Install Python** (Python 3.8 or later recommended)

2. **Install dependencies** (only `colorama` is required):
```bash
    pip install colorama
```

3. **Run the game** from the project root:
```bash
    python main.py
```

## Gameplay Features
- Choose difficulty level (**Easy**, **Medium**, **Hard**)
- Guess one letter at a time — or guess the full word
- Tracks guessed letters and attempts left
- ASCII art to visualize the Hangman status
- Terminal coloring with colorama for better readability
- Command system (e.g. /help, /quit, ...)
- Statistics tracking (games played, wins/losses)
- Clean, testable architecture (OOP + modular functions)

## Example gameplay

```text
Please choose difficulty:
1) easy -- 10 attempts
2) medium -- 6 attempts
3) hard -- 4 attempts
Your choice (1/2/3): 3
Please choose strictness:
1) Strict -- attempts decreased for every guess
2) Moderate -- attempts decreased only for incorrect guesses
Your choice (1/2): 2
Welcome to the Hangman game!
You have 4 attempts.
Your game mode is 'Moderate'.
Type /help to show all available commands
--------------------------------------------------
Current guess: ______
Attempts left: 4
Guess a letter or word: a
Incorrect letter guess.
   _______
  |/      |
  |      (_)
  |       |
  |
  |
__|__
--------------------------------------------------
Current guess: ______
Attempts left: 3
Guess a letter or word: e
--------------------------------------------------
Current guess: ___e__
Attempts left: 3
Guess a letter or word: object
--------------------------------------------------
Congratulations, you guessed the word correctly!
The word was: object
You had 3 attempts left.
Would you like to play again? (y/n) n
Thank you for playing!
Statistics: 1 games: 1 wins | 0 loses
```

## Commands Available During the Game
- `/help` - Show all available commands
- `/quit` - Quit the current game
- `/status` - Show current progress and stats
- `/word` - Reveal the word(debug only)

## Configuration
You can adjust the difficulty in the `config.ini` file:
```ini
[Attempts]
easy = 10
medium = 6
hard = 4
```

## License
This project is for educational purposes and may be reused or extended freely.