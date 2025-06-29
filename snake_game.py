# Snake Game using Pygame
# An aesthetically pleasing single-player game

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
# Darker background for "dark mode"
WHITE = (220, 220, 220)
BLACK = (0, 0, 0)
BG_COLOR = (30, 30, 30)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.SysFont('arial', 24)
LARGE_FONT = pygame.font.SysFont('arial', 72)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()


def draw_grid():
    """Placeholder to keep compatibility; grid disabled for dark mode."""
    pass


class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.grow_pending = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_x = head_x + dir_x
        new_y = head_y + dir_y
        if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
            raise Exception('Wall Collision')
        new_pos = (new_x, new_y)
        if new_pos in self.positions:
            raise Exception('Collision')
        self.positions.insert(0, new_pos)
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def draw(self):
        for pos in self.positions:
            rect = pygame.Rect(pos[0]*GRID_SIZE, pos[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)


class Food:
    def __init__(self, snake_positions):
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_positions:
                return pos

    def draw(self):
        rect = pygame.Rect(self.position[0]*GRID_SIZE, self.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)



def game_over_screen(score):
    """Display game over screen and return player's choice."""
    while True:
        screen.fill(BG_COLOR)
        game_over_text = LARGE_FONT.render('Game Over', True, RED)
        score_text = FONT.render(f'Score: {score}', True, WHITE)
        prompt_text = FONT.render('Press R to Restart or Q to Quit', True, WHITE)
        screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH//2, HEIGHT//3)))
        screen.blit(score_text, score_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH//2, HEIGHT*2//3)))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'restart'
                if event.key == pygame.K_q:
                    return 'quit'


def get_ai_direction(snake, food):
    """Return a direction tuple for the AI to move toward the food."""
    head_x, head_y = snake.positions[0]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    valid_moves = []
    for dir_x, dir_y in directions:
        new_x = head_x + dir_x
        new_y = head_y + dir_y
        if (0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT and
                (new_x, new_y) not in snake.positions):
            valid_moves.append((dir_x, dir_y))
    if not valid_moves:
        return snake.direction
    def distance(move):
        new_x = head_x + move[0]
        new_y = head_y + move[1]
        return abs(food.position[0] - new_x) + abs(food.position[1] - new_y)
    return min(valid_moves, key=distance)


def game_loop(ai_mode=False):
    snake = Snake()
    food = Food(snake.positions)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif not ai_mode and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        if ai_mode:
            snake.direction = get_ai_direction(snake, food)

        try:
            snake.move()
        except Exception:
            return game_over_screen(score)

        if snake.positions[0] == food.position:
            snake.grow()
            score += 1
            food = Food(snake.positions)

        screen.fill(BG_COLOR)
        draw_grid()
        snake.draw()
        food.draw()

        score_text = FONT.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (5, 5))

        pygame.display.flip()
        clock.tick(10)


def start_menu():
    """Display a menu allowing the player to choose Human or AI mode."""
    while True:
        screen.fill(BG_COLOR)
        title_text = LARGE_FONT.render('Snake Game', True, GREEN)
        prompt_text = FONT.render('Press H for Human or A for AI', True, WHITE)
        screen.blit(title_text, title_text.get_rect(center=(WIDTH//2, HEIGHT//3)))
        screen.blit(prompt_text, prompt_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    return False
                if event.key == pygame.K_a:
                    return True


def main():
    ai_mode = start_menu()
    if ai_mode is None:
        pygame.quit()
        return
    while True:
        result = game_loop(ai_mode)
        if result != 'restart':
            break
    pygame.quit()


if __name__ == '__main__':
    main()
