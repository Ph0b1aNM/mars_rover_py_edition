class Mars(object):
    """
    As mentions above, creates a Mars-object.
    """
    def __init__(self, x, y):
        """
        Initializes a Mars-object.
        """
        self.x = x
        self.y = y
        self.occupied = []