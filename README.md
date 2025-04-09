# Hangman Game

This is a simple implementation of the classic **Hangman** game using Python. In this game, the player has to guess the letters of a randomly chosen word before running out of lives. Each wrong guess results in the drawing of a hanging man, and the player loses when the figure is fully drawn.

## Features

- **Random Word Selection**: The game picks a random word from a predefined list.
- **Lives**: The player has 6 lives to guess the word. Each incorrect guess reduces a life.
- **Hangman Graphics**: The player sees a visual representation of the hangman figure as they make incorrect guesses.
- **Interactive Gameplay**: The player inputs their guesses one letter at a time.

## Installation

To run this game, ensure that you have Python installed on your machine. Then, clone this repository using the following command:

```bash
git clone https://github.com/ulquiorraexe/hangman.git
```

After going to the project's directory, run the `main.py` file:

```bash
python main.py
```

## How to Play
  1. **Start the Game:** The game will start by picking a random word from the list.
  2. **Make Guesses:** Input one letter at a time to guess the word.
  3. **Lives:** Each incorrect guess reduces your remaining lives. You start with 6 lives.
  4. **Hangman Graphics:** As you make incorrect guesses, the hangman figure is drawn step by step.
  5. **Game Over:** The game ends when you either guess the word correctly or lose all your lives.

## Code Explanation 

  - **Word Selection:** A random word is chosen from the `words` list to be guessed.
  - **Lives and Graphics:** You have 6 lives to start with. Each incorrect guess decreases your lives, and the hangman figure is drawn progressively with each wrong guess.
  - **Game Loop:** The game continues until the word is guessed correctly or the player runs out of lives.
  - **User Input:** The player guesses one letter at a time. If the letter exists in the word, it is revealed in the appropriate positions.

## License 

This project does not have a license.
