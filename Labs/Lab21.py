"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import easygui
import os
import random


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    exercise0()
    exercise1()
    exercise2()
    exercise3()
    exercise4()


def exercise0():
    """Demonstrate list objects, references, and aliases."""
    # TODO 0: Follow the instructions in the lab document using the Python shell.
    print( "This exercise is to be completed using the Python shell." )


def exercise1():
    """Demonstrate lists and tuples."""
    # TODO 1: Follow the instructions in the lab document using the Python shell.
    print( "This exercise is to be completed using the Python shell." )


def exercise2():
    """Uses the specified function as described in the lab document."""
    # TODO 2: Read, discuss, and understand the following code.
    origin = ( 0, 0 )   # A tuple can be created with explicit parentheses,
    corner = 8.4, 12.6  # but can also be created with implicit parentheses.
    middle = midpoint( origin, corner )
    print( "The midpoint between {} and {} is {}.".format( origin, corner, middle ) )


def midpoint( p1, p2 ):
    """Create and return the midpoint between two points, stored as (x,y) tuples.

    :param (float, float) p1: The first point, stored as an (x,y) tuple.
    :param (float, float) p2: The second point, stored as an (x,y) tuple.
    :return: The midpoint between p1 and p2.
    :rtype: (float, float)
    """
    # Unpack the point tuples into x,y coordinates.
    x1, y1 = p1
    x2, y2 = p2
    # Calculate and return the midpoint as a new (x,y) tuple.
    return ( x1 + x2 ) / 2, ( y1 + y2 ) / 2


def exercise3():
    """Display file information until the user clicks Cancel."""
    # TODO 3b: Re-write the code below to use the file_info function as described in the lab document.
    # Get the first file name before testing the loop condition.
    filename = easygui.fileopenbox( default="./data/*.txt" )

    # A valid filename (i.e., user did not click Cancel) is longer than one character.
    while len( filename ) > 1:
        # Get the base file name to use as the dialog title, then show the results.
        basename = os.path.basename( filename )

        # Show the entire string returned from the file_info function in the message box.
        easygui.msgbox( file_info( filename ), basename )

        # Get another file name before testing the loop condition.
        filename = easygui.fileopenbox( default="./data/*.txt" )


# TODO 3a: Re-write the file_info function as described in the lab document.
def file_info( filename ):
    """Builds and returns a string with file information (lines, words, and characters).

    The string returned is in the following format:
    Lines: 4, Words: 21, Characters: 104

    :param filename: The file for which the info is to be obtained.
    :return: A string with the specified file information.
    :rtype: str
    """
    # Open the file and read its contents as a single string.
    with open( filename ) as data_file:
        data_string = data_file.read()

    # Split the string into words and lines.
    data_words = data_string.split()
    data_lines = data_string.splitlines()

    # Build and return a string with the file information.
    return "Lines: {}, Words: {}, Characters: {}".format( len( data_lines ), len( data_words ), len( data_string ) )


def exercise4():
    """Uses the specified function as described in the lab document."""
    # Test the move_smallest function several times.
    for _ in range( 4 ):
        # Use a list comprehension to build a list of random two-digit values.
        a_list = [ random.randint( 10, 99 ) for _ in range( 8 ) ]
        # Print the data, move the smallest, then print it again.
        print( a_list )
        move_smallest( a_list )
        print( a_list )
        print()


def move_smallest( data ):
    """This function moves the smallest item in a list of data to location 0.

    The item in location 0 is moved to the location where the smallest item is found.

    :param list data: A list of data items.
    :return: None
    """
    # TODO 4: In the space below, complete the function as described in the lab document.
    for _ in range(4):
        a_list = [random.randint(10, 99) for _ in range(8)]
        print(a_list)
        print()
# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()