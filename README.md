# Codex_Playground Snake Game

This repository contains a simple yet stylish Snake Game built with
[Pygame](https://www.pygame.org/). The goal is to guide the snake around the
screen collecting food while avoiding collisions with your own body. Each piece
of food you eat will make the snake grow longer and increase your score.

## Installation

1. Ensure you have Python 3 installed.
2. *(Recommended)* Create a virtual environment to keep dependencies isolated:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install pygame
```

## Running the Game

Activate the virtual environment if you created one, then run the game script:

```bash
python snake_game.py
```

When the game starts you can choose to play yourself or watch the built-in AI
play. Use the arrow keys in human mode to control the snake. The game ends if
the snake collides with itself. Your score is displayed in the corner and on the
game over screen.

When you're done playing, exit the virtual environment with:

```bash
deactivate
```

## Files

- `snake_game.py` – Main game logic implemented with Pygame.
- `ENGINEERING.md` – Technical documentation describing how the game is
  organized.

Enjoy playing!

