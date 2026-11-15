![AI/ML Month 1: Python and Core Mathematics](../assets/readme-banner.png)

# Number Guessing Game

A small command-line game that demonstrates validated input, bounded attempts, and conditional feedback in Python.

## Overview

The program chooses a secret integer from 1 through 100 and gives the player five valid guesses. After each accepted guess, it reports whether the value is too low, too high, or correct.

## Purpose

This project is an exercise in translating a simple game loop into Python: collect input, reject invalid values, update state, and provide feedback.

## Features

- Generates an inclusive random integer from 1 to 100.
- Allows five in-range integer guesses.
- Rejects non-integer and out-of-range input without consuming an attempt.
- Reports the remaining attempt count after each valid guess.

## Core Concepts

- `random.randint()` for random integer selection.
- Functions for separating the greeting from a game round.
- `try`/`except` input conversion and loop control.
- Conditional branches and a counter to track game state.
- The `if __name__ == "__main__"` entry-point guard.

## Technology Stack

- Python 3.6 or later
- Python standard library only; no third-party packages

## Project Structure

```text
Day-01-Number-guessing-game/
├── Number.py
├── README.md
└── assets/
    ├── terminal-gameplay-preview.png
    ├── terminal-gameplay.png
    ├── terminal-start-preview.png
    └── terminal-start.png
```

## Installation and Setup

Install Python 3.6 or later. No package installation or virtual environment is required.

## How to Run

From this project directory:

```console
python Number.py
```

On Windows, `py Number.py` also works when the Python launcher is installed.

## Usage

Enter a name at the greeting prompt, then enter whole-number guesses between 1 and 100. Invalid entries are rejected and the program asks for another guess.

## Implementation Notes

`greet_user()` prints the welcome message. `play_game()` creates the secret number, tracks the remaining attempts, and evaluates each valid guess. The game uses a new secret number each time it starts.

## Error Handling and Limitations

The input loop handles non-integer values and integers outside the accepted range. A correct guess is acknowledged, but does not end the round early: the player can continue guessing until all five valid attempts have been used. The program then prints the game-over message and reveals the secret number.

## Testing

No automated test files are included in this project.

## Learning Outcomes

- Validate interactive input before using it.
- Keep state for one game round inside the function that owns that round.
- Use a loop and conditional branches to express repeated game behavior.

## Future Improvements

- End the round immediately after a correct guess.
- Add automated tests by injecting the secret number and input/output dependencies.
- Offer a replay option without restarting the script.

## Project Information

Part of the AI/ML Month 1 Python and Core Mathematics learning series.

Author: [chetanaybuilder](https://github.com/chetanaybuilder)
