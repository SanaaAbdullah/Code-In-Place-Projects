from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    while front_is_clear():
        repair_arches()
        next_arches()

    repair_arches()


# This function will turn Karel around
def turn_around():
    turn_left()
    turn_left()


# move to the next arches which will be after three steps
def next_arches():
    for i in range (4):
        move()


# precondition : Karel should face the lowest east
# postcondition : one column should have beeper and Karel must be at lowest east
# This function will repair the arches for the entire column
def repair_arches():

    turn_left()

    while front_is_clear():

        if beepers_present():
            move()

        else:
            put_beeper()

    if no_beepers_present():
        put_beeper()

    turn_around()
    return_to_start()


# precondition : Karel should face the upper north
# postcondition : Karel must be at lowest east
# This function will return Karel to lowest of the column
def return_to_start():

    while front_is_clear():
        move()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
