import random
import pygame
pygame.init()
from words import word_list

WIN_WIDTH = 900
WIN_HEIGHT = 900
FPS = 40
BG_COLOR = (0, 8, 255)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

lists = word_list
yes_list = []
no_list = []
correct_count = 0
incorrect_count = 0

game = True
level = 1

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if level == 1:
        window.fill(BG_COLOR)
        random.shuffle(lists)

        for word in lists:
            text1 = pygame.font.SysFont("Arial", 30, True).render(f"Do you know this word? {word}", True, (225, 0, 0))
            window.blit(text1, (350, 350))
            pygame.display.update()
            clock.tick(FPS)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                yes_list.append(word)
                correct_count += 1
            elif keys[pygame.K_n]:
                no_list.append(word)
                incorrect_count += 1

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()