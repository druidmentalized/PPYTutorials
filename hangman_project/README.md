# Hangman Game (Python Project)

A terminal-based implementation of the classic **Hangman** game, written in Python. The game randomly selects a word from a file, and the player must guess the word one letter at a time (or by full-word guesses) within a limited number of attempts.

This project is modular and cleanly separated into logical components using object-oriented programming. It includes enhanced user interaction via ASCII visuals and optional terminal coloring using `colorama`.

---

## Project Structure

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