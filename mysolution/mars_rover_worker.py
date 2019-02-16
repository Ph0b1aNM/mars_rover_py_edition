# mars_rover_worker will handle all variable calculations that are passed through

from enum import Enum

class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

class Command(Enum):
    L = 1
    R = 2
    M = 3

class Plateau_Grid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return super().__init__(x , y)
