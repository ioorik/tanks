"""
A tank interface

Each tank should implement update and ... methods. And have the x,y propreties.
"""

import abc


class ITank(metaclass=abc.ABCMeta):

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
