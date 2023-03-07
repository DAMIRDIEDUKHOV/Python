import pygame as pg
from Player import *
from Platf import *
pg.init()

DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 800
BG_COLOR = (50, 20, 200)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pg.Rect(0,0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return pg.Rect(l, t, w, h)

def main():
    pg.init()
    mw = pg.display.set_mode(DISPLAY)
    pg.display.set_caption('Super MARIVO')
    bg = pg.Surface(DISPLAY)
    bg.fill(BG_COLOR)
    clock = pg.time.Clock()

    entities = pg.sprite.Group()
    platforms = []

    level = [
        '-------------------------------------------------',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-         -----                                 -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                 ---             ---------     -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-            ---------                          -',
        '-                                               -',
        '-                                               -',
        '-                        --                     -',
        '-                                               -',
        '-                                               -',
        '-                               ------          -',
        '-        ------------                           -',
        '-                                               -',
        '-                                               -',
        '-                        -----                  -',
        '-                                               -',
        '-                                    ----       -',
        '-                                               -',
        '-------------------------------------------------']

    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == '-':
                pf = Platform.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += Platform.PF_WIDTH
        x = 0
        y += Platform.PF_HEIGHT

    total_width = len(level[0])*Platform.PF_WIDTH
    total_height = len(level)*Platform.PF_HEIGHT
    camera = Camera(camera_configure, total_width, total_height)

    hero = Player.Player(50, total_height - 100)
    entities.add(hero)
    left = right = up = False
    Game = True
    while Game:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                Game = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_w:
                    up = True
                if e.key == pg.K_a:
                    left = True
                if e.key == pg.K_d:
                    right = True
            if e.type == pg.KEYUP:
                if e.key == pg.K_w:
                    up = False
                if e.key == pg.K_a:
                    left = False
                if e.key == pg.K_d:
                    right = False
        
        mw.blit(bg, (0,0))
        hero.update(left, right, up, platforms)
        camera.update(hero)
        for e in entities:
            mw.blit(e.image, camera.apply(e))
        
if True:
    pg.display.update()
    pg.clock.tick(60)

        