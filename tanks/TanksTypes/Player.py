import pygame

from tanks.TanksTypes.ITank import ITank


class Player(ITank):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def update(self, keys, walls):
        if keys[pygame.K_UP]:
            self._y += 0.1
        if keys[pygame.K_DOWN]:
            self._y -= 0.1

        if keys[pygame.K_RIGHT]:
            self._x += 0.1
        if keys[pygame.K_LEFT]:
            self._x -= 0.1
