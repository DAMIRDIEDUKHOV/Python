import pygame
pygame.init()
import os
from random import randint, choice


def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    result = os.path.join(folder, file_name)
    return result

WIN_WIDTH = 900
WIN_HEIGHT = 900
FPS = 40
BG_COLOR = (20, 134, 5)
LOSE_BG_COLOR = (135, 6, 6)
WIN_BG_COLOR = (26, 238, 36)
LOSE_TEXT_COLOR = (233, 113, 9)
WIN_TEXT_COLOR = (36, 150, 236)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class Image():
    def __init__(self, x, y, Width, Height, file_name, num):
        self.rect = pygame.Rect(x, y, Width, Height)
        self.image_back = pygame.image.load(file_path(file_name))
        self.image_front = pygame.image.load(file_path("Front_card.png"))
        self.image_front.convert_alpha()
        self.transperancy = 255
        self.image_front.set_alpha(self.transperancy)
        self.count_transperancy = 0
        self.num = num

    def show_image(self):
        if self.count_transperancy < 0:
            self.transperancy += self.count_transperancy
            if self.transperancy < 0:
               self.transperancy = 0
               self.count_transperancy = 0
            self.image_front.set_alpha(self.transperancy)
            
        elif self.count_transperancy > 0:
            self.transperancy += self.count_transperancy
            if self.transperancy > 255:
                self.transperancy = 255
                self.count_transperancy = 0
            self.image_front.set_alpha(self.transperancy)

        window.blit(self.image_back, (self.rect.x, self.rect.y))
        window.blit(self.image_front, (self.rect.x, self.rect.y))

cards_images = [
    'Apple.png',
    'Banana.png',
    'Grapes.png',
    'Kivi.png',
    'Lemon.png',
    'Oranges.png',
    'Strawberries (1).png',
    'Watermelon.png'
]

card_num = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
open_cards = []
done_cards = []


cards = []
for j in range(4):
    for i in range(4):
        num = choice(card_num)
        card = Image(75 + 200 * i, 125 + 200 * j, 150, 150, cards_images[num], num)
        cards.append(card)
        card_num.remove(num)


timer = 25
text_font1 = pygame.font.SysFont("liberationmono", 40, True)
text_font2 = pygame.font.SysFont("liberationmono", 75, True)
text_timer =  text_font1.render(f"TIME LEFT: {timer}", True, (4, 8, 120))
lose_text = text_font2.render("YOU LOSE", True, LOSE_TEXT_COLOR)
win_text = text_font2.render("YOU WIN", True, WIN_TEXT_COLOR)

start_time = pygame.time.get_ticks()

game = True
level = 1


while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and len(open_cards) < 2:
                    x, y = event.pos
                    for card in cards:
                        if card.rect.collidepoint(x, y):
                            card.count_transperancy = -10
                            open_cards.append(card)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for card in open_cards:
                        card.count_transperancy = 0
                        card.transperancy = 255
                        card.image_front.set_alpha(card.transperancy)
                    for card in done_cards:
                        card.count_transperancy = 0
                        card.transperancy = 255
                        card.image_front.set_alpha(card.transperancy)
                        cards.append(card)
                    done_cards.clear()
                    open_cards.clear()
                    level = 1
                    timer = 25
                    text_timer =  text_font1.render(f"TIME LEFT: {timer}", True, (4, 8, 120))
                
        
    if level == 1:
        window.fill(BG_COLOR)
        for card in cards:
            card.show_image()
        for card in done_cards:
            card.show_image()
            
        if len(open_cards) == 2:
            if open_cards[1].transperancy == 0:
                if open_cards[0].num == open_cards[1].num:
                    done_cards.append(open_cards[0])
                    done_cards.append(open_cards[1])
                    cards.remove(open_cards[0])
                    cards.remove(open_cards[1])
                else: 
                    open_cards[0].count_transperancy = 10
                    open_cards[1].count_transperancy = 10
                open_cards.clear()
        
        if len(cards) == 0:
            level = "win"
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 1000:
            timer -= 1
            start_time = current_time
            text_timer =  text_font1.render(f"TIME LEFT: {timer}", True, (4, 8, 120))
            if timer < 0:
                level = 'lose'
        
        window.blit(text_timer, (0, 0))
    
    elif level == 'lose':
        window.fill(LOSE_BG_COLOR)
        window.blit(lose_text, (300, 400))
    
    elif level == "win":
        window.fill(WIN_BG_COLOR)
        window.blit(win_text, (300, 400))
        
    pygame.display.update()
    clock.tick(FPS)