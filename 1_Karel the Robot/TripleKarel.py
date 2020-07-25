from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    # for loop with three because it is a TripleKarel which means there are 3 buildings
    for i in range(3):
        paint_a_bulding()
        turn_around()
    turn_left()


# This function will turn Karel around
def turn_around():
    turn_left()
    turn_left()


# precondition : Karel facing west at the upper right
# postcondition : Karel paints the three walls of building
# This function will paint all the three walls of the building
def paint_a_bulding():

    # for loop three because we want to paint three walls
    for i in range (3):

        if left_is_clear():
            move()

        # while we are walking through th wall we should paint it
        while left_is_blocked():
            put_beeper()
            move()

        # turn left to move to the other wall
        turn_left()



# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
