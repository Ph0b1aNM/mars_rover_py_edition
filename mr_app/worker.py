import operator

# Create Mars Plateau as object:

class Mars(object):
    
    def __init__(self, x, y):
        """
        Initializes a Mars-object.
        """
        self.x = x
        self.y = y
        self.occupied = []

# Create Mars Rover as object:

directions = ("N", "E", "S", "W") # Use tuple since we don't need to manipulate
                                  # the direciton after initializing it (immutable)
class Rover(object):

    def __init__(self, x, y, direction, mars):
        self.Mars = mars
        self.direction = direction
        self.x = x
        self.y = y
        self.initial = (self._x, self._y, self._direction)

    direction = property(operator.attrgetter('_direction'))
    @direction.setter

    def direction(self, d):
        if d.upper() not in directions:
            raise ValueError("Direction not correct, use 'N, E, S or W'")
        self._direction = d.upper()

    x = property(operator.attrgetter('_x'))

    @x.setter

    def x(self, x):
        if (x < 0 or x > self.Mars.x):
            raise ValueError("""This rover's x-value is out of bounds.
It should be value should be < 0 and > {}""".format(str(self.Mars.x)))
        self._x = x

    y = property(operator.attrgetter('_y'))

    @y.setter

    def y(self, y):
        if (y < 0 or y > self.Mars.y):
            raise ValueError("This rover's y-valueis out of bounds.\
It should be value should be < 0 and > " + str(self.Mars.y))
        self._y = y

    initial = property(operator.attrgetter('_initial'))
    @initial.setter

    def initial(self, tup):
        for spaces in self.Mars.occupied:
            if (tup[0], tup[1]) == (spaces[0], spaces[1]): raise RuntimeError("This position is \
already occupied by another rover")
        #if (tup[0], tup[1]) in self.Mars.occupied: raise IndexError("This position is already occupied by another rover")
        self._initial = tup


    def get_formatted_position(self):
        return "{} {} {}".format(self._x, self._y, self._direction)

    def get_current_position(self):
        return (self._x, self._y)

    def return_to_start(self):
        self.x = self._initial[0]
        self.y = self._initial[1]
        self.direction = self._initial[2]

    def turnRight(self):
        self.direction = directions[0] \
        if directions.index(self._direction) == 3 \
        else directions[directions.index(self._direction) + 1]

    def turnLeft(self):
        self.direction = directions[3] \
        if directions.index(self._direction) == 0 \
        else directions[directions.index(self._direction) - 1]

    def forward(self):
        if self._direction == "N":
            self.y = self._y + 1
        elif self._direction == "S":
            self.y = self._y - 1
        elif self._direction == "E":
            self.x = self._x + 1
        else:
            self.x = self._x - 1
        #Test the current space
        for spaces in self.Mars.occupied:
            if self.get_current_position() == (spaces[0], spaces[1]):
                raise RuntimeErrorjk("I've hit a position that is already taken.\n\
Returning to my initial position. Please try again!\n")
                self.return_to_start()