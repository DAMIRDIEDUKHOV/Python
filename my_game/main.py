import pygame

WIN_WIDTH = 600
WIN_HEIGHT = 600
FPS = 40
BG_COLOR = (4, 0, 225)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.diplay.set_caption("GAME1")
pygame.time.Clock()

game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT

