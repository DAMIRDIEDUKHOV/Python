import pygame
import time
from time import sleep

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Arconoid')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

bg = pygame.image.load("Purple_backround.jpg")
bg = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))

bg_win = pygame.image.load("you_win.jpg")
bg_win = pygame.transform.scale(bg_win, (WIN_WIDTH, WIN_HEIGHT))

bg_lose = pygame.image.load("you_lose.jpg")
bg_lose = pygame.transform.scale(bg_lose, (WIN_WIDTH, WIN_HEIGHT))

class GameSprites():
    def __init__(self, x, y, width, height, file_name):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_name)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.creation_time = time.time()  # Store the creation time of the health bar

    def show_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

platform = GameSprites(350, 500, 125, 100, "platform_2.png")
ball = GameSprites(300, 300, 50, 50, "Ball.png")
big_health_bar = GameSprites(180, 20, 175, 30, "full_health2.png")
half_health_bar = GameSprites(180, 20, 175, 30, "half_health.png")
no_health_bar = GameSprites(180, 20, 175, 30, "no_health_bar.png")
x = 0
enemies = []
count = len(enemies)
health_bars = []

for i in range(9):
    monster = GameSprites(x, 50, 75, 75, "monster.png")
    enemies.append(monster)
    x += 90

x = 37
for i in range(8):
    monster = GameSprites(x, 140, 75, 75, "monster.png")
    enemies.append(monster)
    x += 90

x = 75
for i in range(7):
    monster = GameSprites(x, 225, 75, 75, "monster.png")
    enemies.append(monster)
    x += 90
x = 0
for i in range(9):
    health_bar = GameSprites(x, 130, 70, 10, "full_health2.png")
    health_bars.append(health_bar)
    x += 90

x = 37
for i in range(8):
    health_bar = GameSprites(x, 220, 70, 10, "full_health2.png")
    health_bars.append(health_bar)
    x += 90

x = 75
for i in range(7):
    health_bar = GameSprites(x, 310, 70, 10, "full_health2.png")
    health_bars.append(health_bar)
    x += 90

move_left = False
move_right = False
speed_x = 6
speed_y = 6

game = True
level = 1
while game:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    if level == 1:
        window.blit(bg, (0, 0))
        platform.show_sprite()
        ball.show_sprite()
        big_health_bar.show_sprite()

        for health_bar in health_bars.copy():
            health_bar.show()
            if current_time - health_bar.creation_time >= 2:
                health_bars.remove(health_bar)

        text = font.render('All Enemy Health:', True, (225, 225, 225))     
        text_rect = text.get_rect(center=(70, 30))
        
        text2 = font.render('Enemy Count: {}'.format(len(enemies)), True, (225, 225, 225))     
        text_rect2 = text2.get_rect(center=(475, 30))

        window.blit(text, text_rect)
        window.blit(text2, text_rect2)

        for enemy in enemies:
            enemy.show_sprite()
            if ball.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                speed_y = -speed_y

        if move_left == True and platform.rect.left > 0:
            platform.rect.x -= 10

        if move_right == True and platform.rect.right < WIN_WIDTH:
            platform.rect.x += 10
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if platform.rect.colliderect(ball.rect):
            speed_y = -speed_y
        if ball.rect.right >= WIN_WIDTH:
            speed_x = -speed_x
        if ball.rect.top <= 0:
            speed_y = -speed_y
        if ball.rect.left <= 0:
            speed_x = -speed_x

        #for i in range(22):
        if len(enemies) == 23:
            name = GameSprites(180, 20, 175, 30, "23_enemies_left.png")
            name.show_sprite()
        
        elif len(enemies) == 22:
            name = GameSprites(180, 20, 175, 30, "22_enemies_left.png")
            name.show_sprite()
        
        elif len(enemies) == 21:
            name = GameSprites(180, 20, 175, 30, "21_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 20:
            name = GameSprites(180, 20, 175, 30, "20_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 19:
            name = GameSprites(180, 20, 175, 30, "19_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 18:
            name = GameSprites(180, 20, 175, 30, "18_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 17:
            name = GameSprites(180, 20, 175, 30, "17_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 16:
            name = GameSprites(180, 20, 175, 30, "16_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 15:
            name = GameSprites(180, 20, 175, 30, "15_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 14:
            name = GameSprites(180, 20, 175, 30, "14_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 13:
            name = GameSprites(180, 20, 175, 30, "13_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 12:
            half_health_bar.show_sprite()

        elif len(enemies) == 11:
            name = GameSprites(180, 20, 175, 30, "11_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 10:
            name = GameSprites(180, 20, 175, 30, "10_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 9:
            name = GameSprites(180, 20, 175, 30, "9_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 8:
            name = GameSprites(180, 20, 175, 30, "8_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 7:
            name = GameSprites(180, 20, 175, 30, "7_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 6:
            name = GameSprites(180, 20, 175, 30, "6_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 5:
            name = GameSprites(180, 20, 175, 30, "5_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 4:
            name = GameSprites(180, 20, 175, 30, "4_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 3:
            name = GameSprites(180, 20, 175, 30, "3_enemies_left.png")
            name.show_sprite()

        elif len(enemies) == 2:
            name = GameSprites(180, 20, 175, 30, "2_enemies_left.png")
            name.show_sprite()
            

        if ball.rect.top > WIN_HEIGHT:
            level = 3

        if len(enemies) == 0:
            no_health_bar.show_sprite()
            level = 2

    elif level == 2:
        sleep(2)
        window.blit(bg_win, (0, 0))
    elif level == 3:
        window.blit(bg_lose, (0, 0))

    clock.tick(FPS)
    pygame.display.update()
