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

timer = 10
txt_timer = Label(15, 15, 100, 50, LIGHT_BLUE)
txt_timer.set_txt(30, 'timer', BLACK)

num_timer = Label(15, 70, 100, 50, LIGHT_BLUE)
num_timer.set_txt(30, str(timer), BLACK)

score = 0
txt_score = Label(600, 15, 100, 50, LIGHT_BLUE)
txt_score.set_txt(30, 'score', BLACK)

num_score = Label(600, 70, 100, 50, LIGHT_BLUE)
num_score.set_txt(30, str(score), BLACK)

count = 0
window.fill(LIGHT_BLUE)
game = True
start_time = pygame.time.get_ticks()


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
                            score += 1
                        else:
                            cards[i].change_color(RED)
                            score -= 1
                        cards[i].show_sprite()
                        num_score.set_txt(30, str(score), BLACK)

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

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 1000:
        timer -= 1
        num_timer.set_txt(30, str(timer), BLACK)
        start_time = current_time

    txt_timer.draw_txt(0, 0)
    num_timer.draw_txt(15, 0)
    txt_score.draw_txt(0, 0)
    num_score.draw_txt(30, 0)

    if score == 5:
        window.fill(GREEN)
        win_card = Label(250, 275, 50, 50, GREEN)
        win_card.set_txt(50, 'You win!!!', BLACK)
        win_card.draw_txt(0, 0)
    elif timer <= 0:
        window.fill(RED)
        lose_card = Label(205, 250, 50, 50, RED)
        lose_card.set_txt(50, 'You lose ): !!!', BLACK)
        lose_card.draw_txt(0, 0)


    clock.tick(FPS)
    pygame.display.update()