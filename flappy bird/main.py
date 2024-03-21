import pygame
import configs

pygame.init()

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512    
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('pink')

    pygame.display.flip()
    clock.tick(FPS)

pygame.QUIT