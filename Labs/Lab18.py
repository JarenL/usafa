"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import easygui
import string
import turtle
# The timeit module provides a simple way to time small bits of Python code.
# https://docs.python.org/3/library/timeit.html
from timeit import timeit
# Import solutions from Lab 15.
# from Labs.Lab15_Strings import pig_latin, rovarspraket, rot13

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960               # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 // 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = WIDTH // 30      # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = MARGIN // 2   # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False         # Set to True for fast, non-animated turtle movement.


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise0()
    # exercise1()
    # exercise2()
    exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
    # exercise8()


def exercise0():
    """Demonstrate writing a text file."""
    # TODO 0: Read, discuss, and understand the following code.

    # A familiar list of strings to test writing to a file.
    values = [ "Integrity First", "Service Before Self", "Excellence In All We Do" ]

    # Opening a file to write requires the second parameter, "w", to specify "write" mode.
    # For other modes, see https://docs.python.org/3.4/library/functions.html#open
    with open( "./data/Values_Write.txt", "w" ) as data_file:
        data_file.write( ", ".join( values ) )

    # Above, the data_file object's write() method was used. However, it can only
    # accept a single string parameter and does not automatically append a newline.
    # The print() function can be used with the file parameter, which then also
    # allows use of the print() function's sep and end parameters.
    with open( "./data/Values_Print.txt", "w" ) as data_file:
        print( ", ".join( values ), file=data_file )

    # The easygui.filesavebox (as opposed to fileopenbox) will give a warning
    # if the file selected for writing already exists.
    with open( easygui.filesavebox( default="./data/*.txt" ), "w" ) as data_file:
        print( "\n".join( values ), file=data_file )


def exercise1():
    """Demonstrate reading a text file with readlines() vs. splitlines()."""
    # TODO 1: Read, discuss, and understand the following code.

    # Recall this method of reading the entire contents
    # of a file into a list of strings, one per line:
    with open( "./data/Test.txt" ) as data_file:
        data = data_file.read().splitlines()  # splitlines() is a method of a string object.
    print( data )

    # The file object also has a readlines() method ... notice any difference in the output?
    with open( "./data/Test.txt" ) as data_file:
        data = data_file.readlines()  # readlines() is a method of a file object.
    print( data )


def exercise2():
    """Demonstrate reading a text file all at once vs. line-by-line."""
    # TODO 2: Read, discuss, and understand the following code.

    # What if reading an entire file was not necessary?
    n = 32
    print( "Starting timeit with n = {}.".format( n ), flush=True )

    t1 = timeit( "find_in_file_v1( 'silence', './data/WarAndPeace.txt' )",
                 "from __main__ import find_in_file_v1", number=n )
    print( "find_in_file_v1 time = {:.2f}.".format( t1 ), flush=True )

    t2 = timeit( "find_in_file_v2( 'silence', './data/WarAndPeace.txt' )",
                 "from __main__ import find_in_file_v2", number=n )
    print( "find_in_file_v2 time = {:.2f}.".format( t2 ), flush=True )

    print( "Percentage faster = {:.2%}.".format( ( t1 - t2 ) / t1 ), flush=True )


def find_in_file_v1( word, filename ):
    """Find the line number of the first occurrence of word in filename.

    :param str word: The word to find.
    :param str filename: The file in which to find the word.
    :return: The line number of the first occurrence of the word; -1 if not found.
    :rtype: int
    """
    # Read the entire contents of the data file into a list of lines.
    with open( filename ) as data_file:
        data = data_file.read().splitlines()

    # Note the following code is un-indented so the data file is closed.
    line_number = 0
    for line in data:
        if word.lower() in line.lower().split():
            return line_number
        else:
            line_number += 1

    return -1


def find_in_file_v2( word, filename ):
    """Find the line number of the first occurrence of word in filename.

    :param str word: The word to find.
    :param str filename: The file in which to find the word.
    :return: The line number of the first occurrence of the word; -1 if not found.
    :rtype: int
    """
    # Open the data file, but do not immediately read its entire contents.
    with open( filename ) as data_file:
        # Note the following code IS indented so the data file is NOT closed.
        line_number = 0
        for line in data_file:
            if word.lower() in line.lower().split():
                return line_number
            else:
                line_number += 1

    return -1


def find_in_file_v3( word, filename, max_lines=1024 ):
    """Find the line number of the first occurrence of word in filename.

    :param str word: The word to find.
    :param str filename: The file in which to find the word.
    :param int max_lines: The maximum number of lines to read before failing.
    :return: The line number of the first occurrence of the word; -1 if not found.
    :rtype: int
    """
    # Open the data file, but do not immediately read its entire contents.
    with open( filename ) as data_file:
        # Note the following code IS indented so the data file is NOT closed.
        line_number = 0
        line = data_file.readline()  # Priming read.
        while line != "" and line_number < max_lines:
            if word.lower() in line.lower().split():
                return line_number
            else:
                line_number += 1
                line = data_file.readline()

    return -1


def exercise3():
    """Uses the specified function as described in the lab document."""
    # Test the last_name_first function before reading/writing the Names.txt file.
    print( last_name_first( "George Washington Carver" ) )

    # TODO 3b: Write code to use the function as described in the lab document.
    with open ("./data/Names.txt") as data_file:
        names = data_file.read().splitlines()
    for index in range(len(names)):
        names[index] = last_name_first(names[index])
    names.sort()

def last_name_first( name ):
    """Converts a full name, First Middle Last, to Last, First M.

     For example, if the actual parameter value is "George Washington Carver",
     the value returned would be "Carver, George W."

    :param name: The First Middle Last name to be converted.
    :return: The Last, First M. name.
    :rtype: str
    """
    # TODO 3a: In the space below, complete the function as described in the lab document.
    b = name.split(" ")
    middle = b[1][0]
    print(str(b[2]) + ", " + str(b[0]) + ", " + str(middle + "."))



def exercise4():
    """Uses the specified function as described in the lab document."""
    # TODO 4: Write code to use the function as described in the lab document.
    filename = easygui.fileopenbox(default="./data/*.txt", title="TOr13 - File Open")
    while len(filename) > 1:
        rot13_filename = filename[:filename.rfind(".") ] + "_rot13.txt"
        with open(filename) as data_file, open(rot13_filename, "w") as rot13_file:
            rot13_file.write(rot13(data_file.read()))
        filename - easygui.fileopenbox(default= "./dara/*.txt", title = "ROT13 - File Open")

def exercise5():
    """Uses the specified function as described in the lab document."""
    # TODO 5: Write code to use the function as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code.


def exercise6():
    """Uses the specified function as described in the lab document."""
    # TODO 6: Write code to use the function as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code.


def exercise7():
    """Uses the specified function as described in the lab document."""
    # TODO 7: Write code to use the function as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code.


def exercise8():
    """Uses the specified function as described in the lab document."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # TODO 8: Write code to use the Mystery.txt file as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code

    # Wait for the user to click before closing the window (leave this as the last line).
    screen.exitonclick()


def turtle_setup():
    """Setup the turtle environment with a screen and two turtles, one for drawing and one for writing.

    Using separate turtles for drawing and writing makes it easy to clear one or the other by
    doing artist.clear() or writer.clear() to clear only the drawing or writing, respectively.

    :return: The screen, a drawing turtle, and a writing turtle.
    :rtype: (turtle.Screen, turtle.Turtle, turtle.Turtle)
    """
    #  ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
    # |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
    # | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
    # |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
    #  _____ _  _ ___ ___    ___ _   _ _  _  ___ _____ ___ ___  _  _
    # |_   _| || |_ _/ __|  | __| | | | \| |/ __|_   _|_ _/ _ \| \| |
    #   | | | __ || |\__ \  | _|| |_| | .` | (__  | |  | | (_) | .` |
    #   |_| |_||_|___|___/  |_|  \___/|_|\_|\___| |_| |___\___/|_|\_|
    #
    # Create the turtle graphics screen and set a few basic properties.
    screen = turtle.Screen()
    screen.setup( WIDTH, HEIGHT, MARGIN, MARGIN )
    screen.bgcolor( "SkyBlue" )

    # Create two turtles, one for drawing and one for writing.
    artist = turtle.Turtle()
    writer = turtle.Turtle()

    # Change the artist turtle's shape so the artist and writer are distinguishable.
    artist.shape( "turtle" )

    # Make the animation as fast as possible and hide the turtles.
    if DRAW_FAST:
        screen.delay( 0 )
        artist.hideturtle()
        artist.speed( "fastest" )
        writer.hideturtle()
        writer.speed( "fastest" )

    # Set a few properties of the writing turtle useful since it will only be writing.
    writer.setheading( 90 )   # Straight up, which makes it look sort of like a cursor.
    writer.penup()            # A turtle's pen does not have to be down to write text.
    writer.setposition( 0, HEIGHT // 2 - FONT_SIZE * 2 )  # Centered at top of the screen.

    return screen, artist, writer


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()