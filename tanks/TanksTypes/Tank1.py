from tanks.TanksTypes.ITank import ITank
from random import randint


class Tank1(ITank):

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.time = 0
        self._facing = 2
        self.acc = 0.001

    def x(self) -> float:
        return self._x

    def y(self) -> float:
        return self._y

    def facing(self) -> int:
        return self._facing

    def update(self, keys, walls):
        self.time += 1
        if self.time > randint(25, 50):
            shouldSwitch = randint(0, 50)
            if shouldSwitch == 0:
                self._facing = randint(0, 3)
            self.time = 0
        else:
            if self.facing() == 0:
                self._y += self.acc
            elif self.facing() == 1:
                self._x -= self.acc
            elif self.facing() == 2:
                self._y -= self.acc
            elif self.facing() == 3:
                self._x += self.acc

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

        if randint(0, 1000) == 0:
            return True
        else:
            return False
