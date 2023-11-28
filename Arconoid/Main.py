import pygame
import time
import sys

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 40
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Arconoid')
clock = pygame.time.Clock()

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

platform = GameSprites(350, 500, 125, 100, "platform 2.png")
ball = GameSprites(300, 300, 50, 50, "Ball.png")
big_health_bar = GameSprites(180, 20, 175, 30, "full_health.png")
x = 0
enemies = []
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
    health_bar = GameSprites(x, 130, 70, 10, "full_health.png")
    health_bars.append(health_bar)
    x += 90

x = 37
for i in range(8):
    health_bar = GameSprites(x, 220, 70, 10, "full_health.png")
    health_bars.append(health_bar)
    x += 90

x = 75
for i in range(7):
    health_bar = GameSprites(x, 310, 70, 10, "full_health.png")
    health_bars.append(health_bar)
    x += 90

move_left = False
move_right = False
speed_x = 3
speed_y = 3

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

        window.blit(text, text_rect)

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

        if ball.rect.top > WIN_HEIGHT:
            level = 3

        if len(enemies) == 0:
            level = 2

    elif level == 2:
        window.blit(bg_win, (0, 0))
    elif level == 3:
        window.blit(bg_lose, (0, 0))

    clock.tick(FPS)
    pygame.display.update()