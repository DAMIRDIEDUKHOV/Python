import pygame
pygame.init()
from random import randint


WIN_WIDTH = 700
WIN_HEIGHT = 600

LIGHT_BLUE = (0, 191, 255)
YELLOW = (255, 230, 0)
BLACK = (0, 0, 0)
GREEN = (34, 255, 0)
RED = (255, 0, 0)

FPS = 40

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def change_color(self, new_color):
        self.color = new_color

    def show_sprite(self):
        pygame.draw.rect(window, self.color, self.rect)

class Label(Area):
    def set_txt(self, size, text, color):
        self.font = pygame.font.SysFont('Arial', size)
        self.text = self.font.render(text, True, color)
    
    def draw_txt(self, shift_x, shift_y):
        self.show_sprite()
        window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))



X = 75

cards = []
for i in range(4):
    card = Label(X, 200, 100, 200, YELLOW)
    card.set_txt(30, 'click', BLACK)
    cards.append(card)
    X += 150

count = 0
window.fill(LIGHT_BLUE)
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                for i in range(4):
                    if cards[i].rect.collidepoint(pos):
                        if i == num:
                            cards[i].change_color(GREEN)
                        else:
                            cards[i].change_color(RED)
                        cards[i].show_sprite()

    if count == 0:
        num = randint(0, 3)
        for i in range(4):
            cards[i].change_color(YELLOW)
            if i == num:
                cards[i].draw_txt(20, 70)
            else:
                cards[i].show_sprite()
        count = 20
    else:
        count -= 1

    clock.tick(FPS)
    pygame.display.update()