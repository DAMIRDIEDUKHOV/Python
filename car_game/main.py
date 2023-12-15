import pygame
pygame.init()
import os
from random import randint

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    result = os.path.join(folder, file_name)
    return result

WIN_WIDTH = 900
WIN_HEIGHT = 700
FPS = 40

bg = pygame.image.load(file_path("road.jpg"))
bg = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

class Image():
    def __init__(self, x, y, Width, Height, file_name):
        self.rect = pygame.Rect(x, y, Width, Height)
        self.image = pygame.image.load(file_path(file_name))
        self.image = pygame.transform.scale(self.image, (Width, Height))

    def show_image(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


car = Image(400, 500, 100, 200, r"car_car.png")

def create_wall():
    walls = list()
    x = 0

    rand_num = randint(0, 5)

    for i in range(6):
        if rand_num != i:
            brick = Image(x, -100, 150, 100, r"hard_brick_wall.jpg")
            walls.append(brick)
        x += 150
    return walls

walls = create_wall()

level = "GO"
speed_brick = 2
count = 0
game = True
move_left = False
move_right = False

while game == True:
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
        
    if level == "GO":
        window.blit(bg, (0, 0))
        car.show_image()
        
        if move_left:
            car.rect.x -= 10
        if move_right:
            car.rect.x += 10

        for brick in walls:
            brick.show_image()
            brick.rect.y += speed_brick
            
        if brick.rect.top >= WIN_HEIGHT:
            walls = create_wall()
            count += 1
            if count == 2:
                speed_brick += 1
                count = 0

        

    pygame.display.update()
    clock.tick(FPS)