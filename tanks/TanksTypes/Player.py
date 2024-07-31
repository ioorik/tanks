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

    def update(self, keys, walls):
        if keys[pygame.K_UP]:
            self._y += self.acc
            self._facing = 0
        elif keys[pygame.K_LEFT]:
            self._x -= self.acc
            self._facing = 1
        elif keys[pygame.K_DOWN]:
            self._y -= self.acc
            self._facing = 2
        elif keys[pygame.K_RIGHT]:
            self._x += self.acc
            self._facing = 3

        for wall in walls:
            x, y, width, height = wall
            if self._facing == 0:
                if self._y < y + height:
                    if self._y > y - 1 and x - 1 < self._x < x + width:
                        self._y -= self.acc
            if self._facing == 1:
                if self._x < x + width:
                    if self._x > x - 1 and y + 1 > self._y > y - height:
                        self._x += self.acc
            if self._facing == 2:
                if self._y > y - 1:
                    if self._y < y + height and x - 1 < self._x < x + width:
                        self._y += self.acc
            if self._facing == 3:
                if self._x > x - 1:
                    if self._x < x + width and y + 1 > self._y > y - height:
                        self._x -= self.acc
