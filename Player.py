import pygame as pg

MOVE_SPEED = 7
SIZE = WIDTH, HEIGHT = 22, 32
COLOR = (150,20,240)
JUMP_POWER = 10
GRAVITY = 0.3

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.onGround = False
        self.xvel = 0
        self.yvel = 0
        self.startx = x
        self.starty = y
        self.image = pg.Surface(SIZE)
        self.image.fill(COLOR)
        self.rect = pg.Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if not(left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pg.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0