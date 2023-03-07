import pygame as pg

PF_SIZE = PF_WIDTH, PF_HEIGHT = 32, 32

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('platform.png')
        self.rect = pg.Rect(x, y, PF_WIDTH, PF_HEIGHT)
        
       