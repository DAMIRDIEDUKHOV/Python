import pygame
pygame.init()

L_BLUE = (0, 225, 225)
RED = (150, 0, 0)
GREEN = (72, 225, 0)
BLUE = (17, 0, 225)
PURPLE = (195, 0, 225)
WHITE = (255, 255, 255)

WIN_Width = 600
WIN_Height = 600
FPS = 40

window = pygame.display.set_mode((WIN_Width, WIN_Height))
clock = pygame.time.Clock()

game = True

# Define the rectangle
rect_1 = pygame.Rect(50, 100, 200, 200)
rect_2 = pygame.Rect(350, 100, 200, 200)
rect_3 = pygame.Rect(50, 375, 200, 200)
rect_4 = pygame.Rect(350, 375, 200, 200)

font = pygame.font.Font(None, 50)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill(L_BLUE)
    txt = font.render("My Color", True, WHITE)
    window.blit(txt, (250, 50))

    pygame.draw.rect(window, RED, rect_1)
    pygame.draw.rect(window, BLUE, rect_2)
    pygame.draw.rect(window, GREEN, rect_3)
    pygame.draw.rect(window, PURPLE, rect_4)




    clock.tick(FPS)
    pygame.display.update()

pygame.quit()