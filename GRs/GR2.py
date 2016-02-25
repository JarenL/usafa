"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: No help received; this GR is entirely individual effort.
=======================================================================
"""
from textwrap import fill

import easygui
import random

""" The following code segments are provided for your reference.
    You are free to copy/paste them into your answers below.

    # An easygui message box to display a formatted string.
    easygui.msgbox( "pi = {:.2f}".format( 22 / 7 ), "Result" )

    # An easygui enter box for entering a string.
    s = easygui.enterbox( "Enter a string:", "Input" )

    # An easygui integer box for entering a positive integer.
    n = easygui.integerbox( "Enter a positive integer:", "Input", "", 1, 2 ** 31 )

    # Get a file name from the user with an easygui File Open Dialog.
    filename = easygui.fileopenbox( default="./data/*.txt" )

    # Read the entire contents of filename into a single string.
    with open( filename ) as data_file:
        data_string = data_file.read()

    # Read the entire contents of filename into a list of strings, one per word.
    with open( filename ) as data_file:
        data_words = data_file.read().split()

    # Read the entire contents of filename into a list of strings, one per line.
    with open( filename ) as data_file:
        data_lines = data_file.read().splitlines()
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print(__doc__)

    # Call each individual exercise; comment/un-comment these lines as you work.
    # problem1()
    problem2()
    # problem3()
    # problem4()


def problem1():
    """Uses the specified function as described in the exam document."""
    # TODO 1b: Write code to use the function as described in the exam document.
    winner = generate_lotto(33)
    ticket = generate_lotto(33)
    counter = 0
    count = 0
    for num in range(len(winner)):
        if num == ticket[counter]:
            count += 1
        counter += 1
    print("Winner =", winner)
    print("Ticket =", ticket)
    print("Count =", count)


# TODO 1a: In the space below, write the function as described in the exam document.

def generate_lotto(upper_bound):
    return random.sample(range(1, upper_bound), 6)


def problem2():
    """Uses the specified function as described in the exam document."""
    # TODO 2b: Write code to use the function as described in the exam document.
    build_matrix(9, 8)
    print("Hello")


# TODO 2a: In the space below, write the function as described in the exam document.

def build_matrix(rows, columns):
    matrix = []
    start = 0
    for row in range(rows):
        row = []
        for col in range(columns):
            row.append(str(start + 1) * (start + 1))
        start += 1
        matrix.append(row)

    # for num in range(rows):
    #     for nums in range(columns):

    for row in matrix:
        print("     ".join(row))





def problem3():
    """Uses the specified function as described in the exam document."""
    # TODO 3b: Write code to use the function as described in the exam document.
    filename = easygui.fileopenbox(default="./data/data/*.txt")
    print_in_box(filename)


# TODO 3a: In the space below, write the function as described in the exam document.

def print_in_box(file):
    # Splits text into values in a list.
    with open(file) as data_file:
        data_lines = data_file.read().splitlines()
    longest_line = 0
    for line in data_lines:
        if len(line) > longest_line:
            longest_line = len(line)
    # Adjusts length of +-----+ on top and bottom.
    border = "+" + ("-" * (longest_line + 4)) + "+"
    print(border)
    # I could not remember the command to justify. Added blank space on the left to push text to the right. Appears to
    # have same effect.
    for line in data_lines:
        # Adds " | " on either side of text
        print("|" + " " * ((len(border) - len(line)) - 4) + str(line) + "  |")
    print(border)


def problem4():
    """Uses the specified function as described in the exam document."""
    # TODO 4b: Write code to use the class as described in the exam document.
    first.Barrel = (50, 25)
    print(str(Barrel))


    # TODO 4a: In the space below, write the class as described in the exam document.

    class Barrel():
        def __init__(self, capacity, fill):
            self.capacity = capacity
            self.fill = fill

        def __str__(self):
            print("{} of {} full".format(fill, capacity))

        def fill_from(self, Barrel):
            self.Barrel = Barrel + Barrel.capacity
            self.fill = fill2


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
