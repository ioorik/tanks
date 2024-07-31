"""
A tank interface

Each tank should implement update and ... methods. And have the x,y propreties.

    >>> ITank()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class ITank with abstract methods update, x, y
"""

import abc


class ITank(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def facing(self) -> int:
        """Returns the facing direction of the tank"""

    @property
    @abc.abstractmethod
    def x(self) -> float:
        """Returns the x position of the tank"""

    @property
    @abc.abstractmethod
    def y(self) -> float:
        """Returns the y position of the tank"""

    @abc.abstractmethod
    def update(self, keys, walls):
        """Update the position, direction, wall collision of the tank"""
