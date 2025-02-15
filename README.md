# Simson
# Simon Says Game

## Description
This is a simple command-line **Simon Says** memory game written in Python. The game challenges the player to remember and repeat an increasing sequence of colors.

## How to Play
1. The game starts by displaying a sequence of colors.
2. The player must memorize and **repeat the sequence** correctly.
3. If the player enters the correct sequence, the game continues by **adding one more color** to the sequence.
4. If the player enters the wrong sequence, the game **ends**, displaying the correct sequence and the final score.
5. The player can type **"exit"** anytime to quit the game.

## Installation
To play the game, ensure you have **Python 3.x** installed on your system.

### Steps:
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/simon-says-game.git
   cd simon-says-game
   ```
2. Run the game:
   ```sh
   python simon_says.py
   ```

## Dependencies
No additional libraries are required. The game runs using built-in Python modules:
- `random` (for generating random colors)
- `time` (for displaying colors with a delay)

## Features
- Randomized color sequences for an engaging experience.
- Increasing difficulty with each round.
- Ability to exit the game anytime with "exit".
- Displays the correct sequence when the player makes a mistake.

## Example Gameplay
```
Welcome to Simon Says!
Repeat the sequence of colors in order. Type 'exit' to quit.

Simon says:
red
------

Your turn! Enter the sequence (space-separated):
red
Good job! Current score: 1

Simon says:
red blue
------

Your turn! Enter the sequence (space-separated):
red blue
Good job! Current score: 2
```

## Contributing
Feel free to fork the repository and submit pull requests with improvements or new features!

---
Enjoy playing Simon Says! 🎮

