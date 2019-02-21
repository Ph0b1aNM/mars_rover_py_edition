#!/usr/bin/env python3

from Rover import Rover, directions
from Mars import Mars
import re


def validate_int(x, y):
    """
    Validate that the two parameters are integers.
    Re-used multiple times during the execution.
    """
    try:
        if int(x) >= 0 and int(y) >= 0:
            return True
    except Exception as err:
        print("Only numerical elements. Try again!")
        return False


def validate_rover(x, y, direction):
    """
    Validates a rover to ensure the parameters are
    correct datatypes(int, int, string).
    It also controls ensures that the integers
    are inside the Mars surface and that the
    supplied direction is a correct direction.
    """
    try:

        if validate_int(x, y) and direction in directions:
            return True
    except ValueError as err:
        print("Error: {}\n. Please enter two numbers followed by a char either N, E, S or W\nTry again!".format(err))
        return False
    print("You seem to have entered an incorrect Rover.\nPlease enter two numbers followed by a char either N, E, S or W\nTry again!\n")
    return False

def validate_operations(op):
    """
    Uses regex to validate that
    the supplied string only contains
    'M', 'R' and 'L'.

    Raises a ValueError if incorrect
    operation(s) have been supplied.
    """
    pattern = re.compile("^[MRL]*$")

    if pattern.match(op):
        return True
    else:
        raise ValueError("Only values 'L', 'M' or 'R' accepted!")

def move(op, r):
    """
    Uses the supplied operations
    and moves the rover according to
    the string of operations.

    If a rover goes out of bounds it is
    returned to its initial position
    (where it was initialized at).
    """
    try:
        for operation in op:
            if operation == "L":
                r.turnLeft()
            elif operation == "R":
                r.turnRight()
            else:
                r.forward()
    except Exception as err:
        op = input("Error: {}\nReturning it to inital position ({}, {} facing {}).\
Try again!\n>>> ".format(err, r.initial[0], r.initial[1], r.initial[2]))
        r.return_to_start()
        move(op, r)

def add_rover(mars):
    """
    Taking a reference to Mars
    this function asks for user input.
    The user input is then validate.
    If it passes validation a new Rover
    is created and returned.
    If the input doesn't pass validation
    the user is prompted to enter a
    new Rover.
    """
    while True:
        rover = None
        try:
            choice = check_if_exit(input("Please enter the current rover's initial position.\nRemember to keep inside Mars limits!\n>>> "), mars).split()
            if len(choice) == 3 and validate_rover(choice[0], choice[1], choice[2]): # Check the length of supplied input and check type-integrity
                rover = Rover(int(choice[0]), int(choice[1]), choice[2], mars)       # Initiate a rover with the supplied input. Each rover is assigned to a Mars (many-to-one relation).
        except ValueError as err:
            print(err)
            continue

        if rover is not None:
            return rover

def move_rover(rover, mars):
    """
    Taking the created rover and mars
    the function then asks for user input.
    The input is validated and then
    sent to move() which then performs
    the operations.

    The Rover is then added to the
    occupied spaces on Mars and a
    new Rover will be prompted.
    """
    while True:
        moved = False
        try:
            choice = check_if_exit(input("Enter a sequence of operations.\n>>> "), mars).upper()
            if validate_operations(choice): # Validate that the supplied operations are 'L', 'M' or 'R'
                move(choice, rover)         # Peform the moves on the rover
                mars.occupied.append((rover.x, rover.y, rover.direction))
                #print(mars.occupied)
                moved = True
                print("\n--------------------------------------\n")
        except Exception as err:
            print(err)
            continue

        if moved:
            return

def go_end(mars):
    """
    This function simply gives a pretty output
    of all the Rovers on Mars surface.
    Then exits the application.
    """
    print("--------------- Output ---------------")
    for rover in mars.occupied:
        print("{} {} {}".format(rover[0], rover[1], rover[2]))
    print("--------------------------------------")
    print("Exiting application.")
    exit()

def check_if_exit(iput, mars):
    """
    Every input taken after setting up Mars will
    use this function to check if the input
    contains 'exit'.

    If it contains 'exit' it the go_end
    function will be called.
    """
    if "exit".upper() in iput.upper():
        go_end(mars)
    return iput

def main ():

    """
    The brains of the code.

    Uses a few while loops to validate
    user input and to make the code more user friendly.

    An exit when prompted will print the rover's positions.
    """

    inactivate_loop = False

    while (not inactivate_loop): # will loop until Mars has been initialized.
        choice = input("Please enter the size of mars (2 numbers, separated by a space and higher than 0.)\n>>> ").split()

        if len(choice) == 2 and validate_int(choice[0], choice[1]): # Checks so that the input is length 2 and then checks type-integrity
            mars = Mars(int(choice[0]), int(choice[1]))
            inactivate_loop = True
        else:
            print("Incorrect input. Please ensure you enter a string with two numerical elements")
    print("\n--------------------------------------\n")

    while True:
            rover = add_rover(mars)       # Initiate a rover with the supplied input. Each rover is assigned to a Mars (many-to-one relation).
            move_rover(rover, mars)



if __name__ == "__main__":
    main()