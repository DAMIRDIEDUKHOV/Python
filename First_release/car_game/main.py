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

end_count = 0

level = "GO"
arial30 = pygame.font.SysFont("Arial", 30, True)
text2 = arial30.render("YOU LOSE", True, (255, 0, 0))
text = arial30.render(f"YOU'RE SCORE: {end_count}", True, (40, 9, 194))
text3 = arial30.render("YOU WIN", True, (0, 255, 0))
text4 = arial30.render("Press R to restart.", True, (0, 0, 0))
speed_brick = 2
count = 0
game = True
move_left = False
move_right = False

while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if level == "GO":
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
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    level = "GO"
                    walls = create_wall()
                    end_count = 0
                    count = 0
                    speed_brick = 2
                    car.rect.x = 400
                    text = arial30.render(f"YOU'RE SCORE: {end_count}", True, (40, 9, 194))
                    
    if level == "GO":
        window.blit(bg, (0, 0))
        car.show_image()
        
        if move_left and car.rect.left > 0:
            car.rect.x -= 10
        if move_right and car.rect.right < WIN_WIDTH:
            car.rect.x += 10

        for brick in walls:
            brick.show_image()
            brick.rect.y += speed_brick
            if car.rect.colliderect(brick.rect):
                level = "STOP"
        
        window.blit(text, (0, 0))
            
        if brick.rect.top >= WIN_HEIGHT:
            walls = create_wall()
            count += 1
            end_count += 1
            text = pygame.font.SysFont("Arial", 30, True).render(f"YOU'RE SCORE: {end_count}", True, (40, 9, 194))
            if count == 2:
                speed_brick += 1
                count = 0
            if end_count == 14:
                level = "WIN"

    elif level == "STOP":
        window.blit(text2, (350, 350))
        window.blit(text4, (350, 400))
    elif level == "WIN":
        window.blit(text3, (350, 350))
        window.blit(text4, (350, 400))

    pygame.display.update()
    clock.tick(FPS)