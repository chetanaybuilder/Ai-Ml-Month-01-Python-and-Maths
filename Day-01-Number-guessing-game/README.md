<p align="center">
  <img src="assets/banner.svg" alt="AI and ML Month 1: Python and Maths - Day 1" width="100%">
</p>

<p align="center">
  <strong>A command-line Python project focused on program structure, state, and control flow.</strong>
</p>

## Number Guessing Game

A command-line game that generates a secret integer and gives the player five attempts to guess it. Each guess receives higher-or-lower feedback, and the secret number is shown when the round ends.

## System Architecture

The project is intentionally implemented as a single Python module:

- `greet_user()` prints the game banner, collects the player's name, and introduces the attempt limit.
- `play_game()` creates the round state, reads guesses, compares each guess with the secret number, and prints feedback.
- The `__main__` guard starts the greeting and game when the file is run directly.

The secret number and attempt counter are local to the game function. `MAX_ATTEMPTS` is a module-level configuration value shared by the functions that need it.

## Core Mechanics

1. Generate a random integer from 1 through 100.
2. Read each player guess, require a whole number from 1 through 100, and reject invalid input without consuming an attempt.
3. Compare the guess with the secret number and report whether it is lower, higher, or equal.
4. Decrease the remaining-attempt count and display it.
5. After the configured attempts, reveal the secret number.

Guesses are appended to a local history list during the round. The list is not currently displayed or used in the game output.

## Topics Mastered

- **Environment setup:** Create and activate a `venv`, work in VS Code, and use Git to track project changes.
- **Data types:** Use strings for player input and messages, integers for guesses and counters, and a list for guess history.
- **Control flow:** Use a `while` loop and `if`/`elif`/`else` branches to manage attempts and provide feedback.
- **Modular functions:** Separate the greeting from the round logic with `greet_user()` and `play_game()`.
- **Variable scope (LEGB):** Resolve `MAX_ATTEMPTS` from module/global scope while keeping round values such as `secret_no` and `attempts_left` local to `play_game()`.
- **In-place mutability:** `history.append(guess)` updates the existing list rather than creating a replacement list.

## Local Setup

Python 3 is required. The game uses only the Python standard library.

Create a virtual environment from the project directory:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Open the project folder in VS Code and select the `.venv` interpreter for the workspace. No additional packages are required.

## Execution

From the project directory, run:

```powershell
python Number.py
```

If the virtual environment is not activated, use the Python interpreter available on your `PATH`.

## Terminal Screenshots

<p align="center">
  <img src="assets/terminal-start-preview.png" alt="Terminal showing the game prompt" width="48%">
  &nbsp;&nbsp;
  <img src="assets/terminal-gameplay-preview.png" alt="Terminal showing a completed game" width="48%">
</p>

---

**Author:** chetanaybuilder · Future Founder
