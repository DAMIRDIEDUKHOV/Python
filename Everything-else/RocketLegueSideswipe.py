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
player_x = WINDOW_WIDTH // 1.15 - player_width // 1.15
player_y = WINDOW_HEIGHT - player_height
player_speed_x = 5

ball_radius = 30  # Adjust the size of the ball
ball_color = (255, 255, 255)
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_velocity_x = 0
ball_velocity_y = 0
gravity = 0.5  # Adjust the gravity value for desired effect
bounce_factor = 0.8  # Adjust the bounce factor for desired effect

boundary_width = 30  # Width of the boundaries
boundary_radius = 50  # Radius of the curved corners
boundary_color = (0, 255, 0)  # Color of the boundaries
boundary_thickness = 3  # Thickness of the boundary lines

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
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)  # Create a rectangle for the ball

    ball_velocity_y += gravity  # Apply gravity to the ball's vertical velocity
    ball_x += ball_velocity_x  # Update the ball's horizontal position based on velocity
    ball_y += ball_velocity_y  # Update the ball's vertical position based on velocity

    if ball_y + ball_radius >= WINDOW_HEIGHT - boundary_width:  # Check collision with the bottom boundary
        ball_y = WINDOW_HEIGHT - boundary_width - ball_radius  # Set the ball's position just above the bottom boundary
        ball_velocity_y = -ball_velocity_y * bounce_factor  # Reverse the vertical velocity and apply bounce factor

    if ball_x - ball_radius <= boundary_width or ball_x + ball_radius >= WINDOW_WIDTH - boundary_width:
        ball_velocity_x = -ball_velocity_x * bounce_factor  # Reverse the horizontal velocity and apply bounce factor

    if ball_y - ball_radius <= WINDOW_HEIGHT - boundary_width:  # Check if the ball is above the boundary intercept line
        if player_x - player_width // 2 < ball_x < player_x + player_width // 2:
            ball_y = WINDOW_HEIGHT - boundary_width - ball_radius - player_height  # Set the ball's position just above the boundary intercept line
            ball_velocity_y = -ball_velocity_y * bounce_factor  # Reverse the vertical velocity and apply bounce factor

    window.fill((0, 0, 0))

    # Draw the boundaries
    pygame.draw.rect(window, boundary_color, (0, 0, WINDOW_WIDTH, boundary_width))  # Top boundary
    pygame.draw.rect(window, boundary_color, (0, 0, boundary_width, WINDOW_HEIGHT - boundary_width))  # Left boundary
    pygame.draw.rect(window, boundary_color, (0, WINDOW_HEIGHT - boundary_width, WINDOW_WIDTH, boundary_width))  # Bottom boundary
    pygame.draw.rect(window, boundary_color, (WINDOW_WIDTH - boundary_width, 0, boundary_width, WINDOW_HEIGHT - boundary_width))  # Right boundary

    # Draw the curved corners
    pygame.draw.circle(window, boundary_color, (boundary_width, boundary_width), boundary_radius, boundary_thickness)  # Top left corner
    pygame.draw.circle(window, boundary_color, (WINDOW_WIDTH - boundary_width, boundary_width), boundary_radius, boundary_thickness)  # Top right corner
    pygame.draw.circle(window, boundary_color, (boundary_width, WINDOW_HEIGHT - boundary_width), boundary_radius, boundary_thickness)  # Bottom left corner
    pygame.draw.circle(window, boundary_color, (WINDOW_WIDTH - boundary_width, WINDOW_HEIGHT - boundary_width), boundary_radius, boundary_thickness)  # Bottom right corner

    pygame.draw.rect(window, player_color, player_rect)
    pygame.draw.circle(window, ball_color, (ball_x, int(ball_y)), ball_radius)  # Draw the ball with integer position

    pygame.display.update()
    clock.tick(FPS)