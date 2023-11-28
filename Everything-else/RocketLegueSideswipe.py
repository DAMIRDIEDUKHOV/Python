import pygame
from pygame.locals import *
import sys
import math

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Rocket League Sideswipe')

clock = pygame.time.Clock()
FPS = 60

player_width = 50
player_height = 25
player_color = (255, 0, 0)
player_x = WINDOW_WIDTH - 100  # Move the car further to the right
player_y = WINDOW_HEIGHT - player_height
player_speed_x = 5

ball_radius = 30
ball_color = (255, 255, 255)
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_velocity_x = 0
ball_velocity_y = 0
gravity = 0.5
bounce_factor = 0.8

boundary_color = (0, 0, 255)  # Change boundary color

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed_x
    elif keys[K_RIGHT]:
        player_x += player_speed_x

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    ball_velocity_y += gravity
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    if ball_y + ball_radius >= WINDOW_HEIGHT:
        ball_y = WINDOW_HEIGHT - ball_radius
        ball_velocity_y = -ball_velocity_y * bounce_factor

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WINDOW_WIDTH:
        ball_velocity_x = -ball_velocity_x * bounce_factor

    if ball_y - ball_radius <= WINDOW_HEIGHT - player_height:
        if player_rect.colliderect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2):
            collision_direction = (ball_x - player_x - player_width / 2) / (player_width / 2)
            ball_velocity_x = collision_direction * 5
            ball_velocity_y = -ball_velocity_y

    window.fill((0, 0, 0))

    # Draw the side boundaries with a different color
    pygame.draw.rect(window, boundary_color, (0, 0, WINDOW_WIDTH, 30))  # Top boundary
    pygame.draw.rect(window, boundary_color, (0, 0, 30, WINDOW_HEIGHT))  # Left boundary
    pygame.draw.rect(window, boundary_color, (0, WINDOW_HEIGHT - 30, WINDOW_WIDTH, 30))  # Bottom boundary
    pygame.draw.rect(window, boundary_color, (WINDOW_WIDTH - 30, 0, 30, WINDOW_HEIGHT))  # Right boundary

    pygame.draw.rect(window, player_color, player_rect)
    pygame.draw.circle(window, ball_color, (ball_x, int(ball_y)), ball_radius)

    pygame.display.update()
    clock.tick(FPS)