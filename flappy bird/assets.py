import pygame
import os

sprites = {}



def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('_')[0]] = pygame.image.load(os.path.join(path, file))


def get_sprite(name):
    return sprites[name]