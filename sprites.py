# file constructed by Charlie Fezell

''' Sources:
Mr. Cozort's wonderful teaching and code
Kids Can Code'''

# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,40))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        print("adding vecs " + str(self.vel + self.acc))

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        print("acc " + str(self.acc))
        print("vel " + str(self.vel))

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x =  -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # set player friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # jump to other side of screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
    
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# class Enemy(Sprite):

#     def __init__(self):
#         Sprite.__init__(self)
#         self.image = pg.Surface((30,40))
#         self.image.fill(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT /2)
#         self.vx = 0
#         self.vy = 0
#     def update(self):
#         self.vx = 0
#         keys = pg.key.get_pressed()
#         if keys[pg.K_a]:
#             self.vx = -5
#         if keys[pg.K_d]:
#             self.vx = 5

#         self.rect.x += self.vx
#         self.rect.y += self.vy
