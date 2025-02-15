import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon Says")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 139)
DARK_YELLOW = (204, 204, 0)

# Button coordinates and sizes
buttons = {
    "red": pygame.Rect(0, 0, WIDTH // 2, HEIGHT // 2),
    "green": pygame.Rect(WIDTH // 2, 0, WIDTH // 2, HEIGHT // 2),
    "blue": pygame.Rect(0, HEIGHT // 2, WIDTH // 2, HEIGHT // 2),
    "yellow": pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2),
}

colors = {
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "yellow": YELLOW,
}

dark_colors = {
    "red": DARK_RED,
    "green": DARK_GREEN,
    "blue": DARK_BLUE,
    "yellow": DARK_YELLOW,
}

# Font
font = pygame.font.Font(None, 60)

# Game variables
sequence = []
user_sequence = []
score = 0
FPS = 60
clock = pygame.time.Clock()


def draw_buttons(active_color=None):
    """Draws the buttons, optionally highlighting one."""
    for color, rect in buttons.items():
        if color == active_color:
            pygame.draw.rect(screen, colors[color], rect)
        else:
            pygame.draw.rect(screen, dark_colors[color], rect)
        pygame.draw.rect(screen, WHITE, rect, 3)  # Border


def show_sequence(seq):
    """Flashes the sequence to the player properly."""
    for color in seq:
        draw_buttons(color)
        pygame.display.update()
        time.sleep(0.5)  # Show color longer

        # Clear screen before moving to next color
        draw_buttons()
        pygame.display.update()
        time.sleep(0.3)  # Small delay before next color



def check_user_sequence():
    """Checks if the user's sequence matches the game sequence."""
    global sequence, user_sequence, score
    if user_sequence == sequence[:len(user_sequence)]:
        if len(user_sequence) == len(sequence):
            score += 1
            user_sequence = []
            sequence.append(random.choice(list(colors.keys())))
            time.sleep(1)
            show_sequence(sequence)
    else:
        game_over()


def game_over():
    """Displays Game Over and exits."""
    screen.fill(WHITE)
    text = font.render(f"Game Over! Score: {score}", True, (0, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Main game loop
sequence.append(random.choice(list(colors.keys())))
show_sequence(sequence)

running = True
while running:
    screen.fill(WHITE)
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for color, rect in buttons.items():
                if rect.collidepoint(pos):
                    user_sequence.append(color)
                    draw_buttons(color)
                    pygame.display.update()
                    time.sleep(0.3)
                    draw_buttons()
                    pygame.display.update()
                    check_user_sequence()

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
