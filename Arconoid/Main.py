import pygame
pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Arconoid')
clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill(BLACK)

    clock.tick(FPS)
    pygame.display.update()