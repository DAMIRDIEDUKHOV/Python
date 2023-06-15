import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle and ball dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_RADIUS = 20

# Paddle positions and velocities
paddle_a_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_b_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_a_velocity = 0
paddle_b_velocity = 0
PADDLE_VELOCITY = 5

# Ball position and velocities
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_velocity_x = -3
ball_velocity_y = -3

# Score
score_a = 0
score_b = 0
SCORE_FONT = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_a_velocity = -PADDLE_VELOCITY
            elif event.key == pygame.K_s:
                paddle_a_velocity = PADDLE_VELOCITY
            elif event.key == pygame.K_UP:
                paddle_b_velocity = -PADDLE_VELOCITY
            elif event.key == pygame.K_DOWN:
                paddle_b_velocity = PADDLE_VELOCITY
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_a_velocity = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_b_velocity = 0

    # Update paddle positions
    paddle_a_y += paddle_a_velocity
    paddle_b_y += paddle_b_velocity

    # Restrict paddle positions within the window
    paddle_a_y = max(0, min(WINDOW_HEIGHT - PADDLE_HEIGHT, paddle_a_y))
    paddle_b_y = max(0, min(WINDOW_HEIGHT - PADDLE_HEIGHT, paddle_b_y))

    # Move the ball
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Ball collisions with walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= WINDOW_HEIGHT:
        ball_velocity_y *= -1

    # Ball collisions with paddles
    if ball_x - BALL_RADIUS <= PADDLE_WIDTH and paddle_a_y <= ball_y <= paddle_a_y + PADDLE_HEIGHT:
        ball_velocity_x *= -1
    elif ball_x + BALL_RADIUS >= WINDOW_WIDTH - PADDLE_WIDTH and paddle_b_y <= ball_y <= paddle_b_y + PADDLE_HEIGHT:
        ball_velocity_x *= -1

    # Ball out of bounds
    if ball_x - BALL_RADIUS <= 0:
        score_b += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_velocity_x *= -1
    elif ball_x + BALL_RADIUS >= WINDOW_WIDTH:
        score_a += 1
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_velocity_x *= -1

    # Clear the window
    window.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(window, WHITE, pygame.Rect(0, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, pygame.Rect(WINDOW_WIDTH - PADDLE_WIDTH, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Draw scores
    score_text = SCORE_FONT.render("Player A: {}  Player B: {}".format(score_a, score_b), True, WHITE)
    window.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
