# Engineering Documentation

This document explains the design and major components of the Snake Game
implemented using Pygame.

## File Overview

- **snake_game.py** – Entry point of the game and contains all game logic.

## Components

### Global Configuration
- **WIDTH, HEIGHT, GRID_SIZE, GRID_WIDTH, GRID_HEIGHT** – Control the size of
the game window and the grid on which the snake moves.
- **Colors and Fonts** – Color tuples and font objects used throughout the game.
- **screen, clock** – Initialized Pygame display surface and clock for frame
  rate control.

### `draw_grid()`
Draws grid lines on the screen to provide a clear playing field. Called every
frame to redraw the grid.

### `Snake` Class
Represents the player's snake. Key methods:
- **`__init__`** – Initializes the snake at the center of the grid with a random
  starting direction.
- **`move()`** – Moves the snake one grid cell in the current direction. Handles
  collision with itself by raising an exception. Supports growth via
  `grow_pending` flag.
- **`grow()`** – Sets the flag so the next call to `move()` extends the snake.
- **`draw()`** – Renders each segment of the snake onto the screen.

### `Food` Class
Manages the food item that the snake must collect.
- **`__init__`** – Generates an initial food position that does not collide with
  the snake.
- **`random_position()`** – Finds a random valid grid position.
- **`draw()`** – Draws the food square on the screen.

### `get_ai_direction(snake, food)`
Simple helper that chooses a valid move bringing the snake closer to the food.
Used when the game runs in AI mode.

### `game_over_screen(score)`
Displays a simple end screen showing the player's final score. Waits a few
seconds before returning control.

### `start_menu()`
Initial menu that lets the user pick whether to play manually or let the AI
control the snake. Returns `True` for AI mode and `False` for human mode.

### `main()`
Main entry point:
1. Initializes `Snake` and `Food` objects and keeps track of the score.
2. Processes user input for arrow keys to change direction.
3. Moves the snake each frame and checks for collisions.
4. Updates score when food is eaten, generates new food, and handles game over
   state by calling `game_over_screen`.
5. Draws all elements each frame and regulates the frame rate with `clock.tick(10)`.

The game loop exits when the user quits the game window. All resources are
cleaned up when `pygame.quit()` is called.

