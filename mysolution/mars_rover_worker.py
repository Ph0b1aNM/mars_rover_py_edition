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

class Rover_move(object):

    def __init__(self, x, y, direction, plateau_grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau_grid = plateau_grid
        return super().__init__(x, y, direction, plateau_grid)

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.x, self.y, self.direction.name)

    def _get_coordinates(self):
        return (self.x, self.y,)

    coordinates = property(_get_coordinates, doc="get current coordinates")

    def _turn_left(self):
        heading = self.heading.value - 1

        if heading < Heading.N.value:
            heading = Heading.W.value

        self.heading = Heading(heading)

    def _turn_right(self):
        heading = self.heading.value + 1

        if heading > Heading.W.value:
            heading = Heading.N.value

        self.heading = Heading(heading)

    def _move_forward(self):
        if self.heading is Heading.N:
            self.y += 1

        if self.heading is Heading.E:
            self.x += 1

        if self.heading is Heading.S:
            self.y -= 1

        if self.heading is Heading.W:
            self.x -= 1

        if not self.plateau.validate(self.x, self.y):
            logger.warning(
                'Do you can go beyond the borders? '
                'Maybe you need to talk with mission control.')

    def execute(self, command):
        if not isinstance(command, Command):
            raise ValueError(
                'You need talk martian or the command will be ignored.')

        if command is Command.L:
            self._turn_left()

        if command is Command.R:
            self._turn_right()

        if command is Command.M:
            self._move_forward()