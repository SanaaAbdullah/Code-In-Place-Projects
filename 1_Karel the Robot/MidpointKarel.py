from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    """
    The proposed algorithm:
    1. count the number of columns
    2. find the center and move to it
    3. put beeper on the center
    """

    num_col = count_col()
    move_center(num_col)
    put_beeper()


# precondition: Karel in the first row and first column facing East
# Postcondition: Karel in the first row and last column facing West
# Return: return the number of column
def count_col():

    col = 1

    while front_is_clear():
        move()
        col += 1

    turn_around()

    return col

# Karel should turn around which means turn left two times
def turn_around():
    for i in range(2):
        turn_left()


# precondition: Karel in the first row and last column facing West
# Postcondition: Karel in the first row and the center facing West
# Parameter: this function will take the number of column to calculate the center
def move_center(col):

    center = int(col/2)

    for i in range(center):
        move()


ma
# There is no need to edit code beyond this point
#if __name__ == "__main__":
#    run_karel_program()
