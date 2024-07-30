"""
The player's tank
Implements the ITank interface

Usage Example:

    >>> pygame.init()
    (5, 0)
    >>> p = Player(0, 1)
    >>> p.x()
    0
    >>> p.y()
    1
    >>> p.update(pygame.key.get_pressed(), [1, 0,  1, 1])
    >>> p.y()
    1

"""

import pygame

from tanks.TanksTypes.ITank import ITank


class Player(ITank):

    def __init__(self, x, y):
        self._x: float = x
        self._y: float = y
        self._facing = 0
        self.acc = 0.002

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def facing(self) -> int:
        return self._facing

    def update(self, keys, walls, gs):
        if keys[pygame.K_UP]:
            self._y += self.acc
            self._facing = 0
        elif keys[pygame.K_DOWN]:
            self._y -= self.acc
            self._facing = 2
        elif keys[pygame.K_RIGHT]:
            self._x += self.acc
            self._facing = 3
        elif keys[pygame.K_LEFT]:
            self._x -= self.acc
            self._facing = 1

        for wall in walls:
            x, y, width, height = wall
            if x + width > self._x + 1 > x and y - 1 < self._y < y + height:
                self._x -= self.acc
            if x < self._x < x + width and y - 1 < self._y < y + width:
                self._x += self.acc

            if y + height > self._y > y - 1.1 and x + width > self._x > x:
                self._y -= self.acc
            if y < self._y < y + height + 0.1 and x + width > self._x > x - 1:
                self._y += self.acc
