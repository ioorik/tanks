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

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def facing(self) -> int:
        return self._facing

    def update(self, keys, walls):
        if keys[pygame.K_UP]:
            self._y += 0.1
            self._facing = 0
        elif keys[pygame.K_DOWN]:
            self._y -= 0.1
            self._facing = 2
        elif keys[pygame.K_RIGHT]:
            self._x += 0.1
            self._facing = 3
        elif keys[pygame.K_LEFT]:
            self._x -= 0.1
            self._facing = 1
