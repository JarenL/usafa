"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: No help received; this GR is entirely individual effort.
=======================================================================
"""

import easygui
import random
import math
import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960  # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 // 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = WIDTH // 30  # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = MARGIN // 2  # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False  # Set to True for fast, non-animated turtle movement.

""" The following code segments are provided for your reference.
    You are free to copy/paste them into your answers below.

    # An easygui message box to display a formatted string.
    easygui.msgbox( "pi = {:.2f}".format( 22 / 7 ), "Result" )

    # An easygui integer box for entering a string.
    s = easygui.enterbox( "Enter a string:", "Input" )

    # An easygui integer box for entering a positive integer.
    n = easygui.integerbox( "Enter a positive integer:", "Input", "", 1, 2 ** 31 )

    # Read the entire contents of a file into a single string.
    with open( easygui.fileopenbox( default="./data/*.txt" ) ) as data_file:
        data_string = data_file.read()

    # Read the entire contents of a file into a list of strings, one per word.
    with open( easygui.fileopenbox( default="./data/*.txt" ) ) as data_file:
        data_words = data_file.read().split()

    # Read the entire contents of a file into a list of strings, one per line.
    with open( easygui.fileopenbox( default="./data/*.txt" ) ) as data_file:
        data_lines = data_file.read().splitlines()
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print(__doc__)

    # Call each individual exercise; comment/un-comment these lines as you work.
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()
    # problem6()


def problem1():
    """Uses the specified function as described in the exam document."""
    # TODO 1b: Write code to use the function as described in the exam document.
    kilo = [100, 150, 200, 250, 300, 350, 400, 450, 500]
    print("Kilograms    Pounds")
    print("=========   ========")
    kilograms_to_pounds(kilo)


# TODO 1a: In the space below, write the function as described in the exam document.

def kilograms_to_pounds(kilograms):
    for num in kilograms:
        pounds = num * 2.204622
        print("   " + str(num) + "   " + "    " + str(pounds) + " ")


def problem2():
    """Uses the specified function as described in the exam document."""
    # TODO 2b: Write code to use the function as described in the exam document.
    count = easygui.integerbox("How many numbers?")
    bottom = easygui.integerbox("Lower Bound?")
    top = easygui.integerbox("Upper Bound?")
    even_odd(count, bottom, top)

# TODO 2a: In the space below, write the function as described in the exam document.

def even_odd(how_many, lower_bound, upper_bound):
    sum_even = 0
    sum_odd = 0
    while how_many > 0:
        roll = random.randint(lower_bound, upper_bound)
        if roll % 2 == 0:
            sum_even += roll
        else:
            sum_odd += roll
        how_many -= 1
    what_i_need = sum_even - sum_odd
    return easygui.msgbox("Result:" + str(what_i_need))


def problem3():
    """Uses the specified function as described in the exam document."""
    # TODO 3b: Write code to use the function as described in the exam document.
    first_num = easygui.integerbox("First Number?")
    second_num = easygui.integerbox("Second Number?")
    third_number = easygui.integerbox("Third Number?")
    fourth_number = easygui.integerbox("Fourth Number?")
    first = gcd(first_num, second_num)
    second = gcd(second_num, third_number)
    third = gcd(third_number, fourth_number)
    greatest_common_denominator = first
    if second <= greatest_common_denominator:
        greatest_common_denominator = second
    elif third <= greatest_common_denominator:
        greatest_common_denominator = third
    easygui.msgbox("GCD: " + str(greatest_common_denominator))

# TODO 3a: In the space below, write the function as described in the exam document.

def gcd(int1, int2):
    """
    Takes two inputs and if they are of different values will output their difference.
    :param int1: The first value entered into the function.
    :param int2: The second value entered into the function.
    :return: Returns the difference between int1 and int2.
    """
    what_i_need = 0
    if int1 != int2:
        if int1 > int2:
            what_i_need = int1 - int2
        elif int2 > int1:
            what_i_need = int2 - int1
    return what_i_need



def problem4():
    """Uses the specified function as described in the exam document."""
    # TODO 4b: Write code to use the function as described in the exam document.
    pass  # Remove the pass statement (and this comment) when writing your own code.
    what_i_need = ["I", "me", "he", "she", "him", "her", "we", "us", "they", "them"]
    what_i_need_first = ["we", "us", "I", "me"]
    what_i_need_third = ["he", "she", "him", "her","they", "them"]
    # I couldn't remember how to open document.
    textfile = easygui.fileopenbox()
    count_string = count_word(what_i_need, textfile)
    count_first = count_word(what_i_need_first, textfile)
    count_third = count_word(what_i_need_third, textfile)



# TODO 4a: In the space below, write the function as described in the exam document.

def count_word(single_string, list_string):
    count = 0
    for word in list_string:
        if word == single_string:
            count += 1
    return count



def problem5():
    """Use the screen and turtle defined below to solve the problem specified in the exam document."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # TODO 5b: Write code to use the function as described in the exam document.
    r = (WIDTH - 2 * MARGIN) / 12
    distancex = r * 2 + MARGIN
    bottom_rowx = (r + (MARGIN / 3))
    bottom_rowy = (r + MARGIN) / 2
    black_posx = 0
    black_posy = 0
    blue_posx = black_posx - distancex
    blue_posy = black_posy
    red_posx = black_posx + distancex
    red_posy = black_posy
    yellow_posx = black_posx - bottom_rowx
    yellow_posy = black_posy - bottom_rowy
    green_posx = black_posx + bottom_rowx
    green_posy = black_posy - bottom_rowy
    # ###Could not figure out how to use the given for loop. Improvised. Color isn't changing can't figure out why.
    artist.pencolor("Black")
    draw_circle( artist, black_posx, black_posy, r)
    artist.color("Blue")
    draw_circle( artist, blue_posx, blue_posy, r)
    artist.color( "Red" )
    draw_circle( artist, red_posx, red_posy, r)
    artist.color( "Yellow" )
    draw_circle( artist, yellow_posx, yellow_posy, r)
    artist.color( "Green" )
    draw_circle( artist, green_posx, green_posy, r)
    # Wait for the user to click before closing the window (leave this as the last line).
    screen.exitonclick()


# TODO 5a: In the space below, write the function as described in the exam document.

def draw_circle(turtle, x, y, radius):
    screen, artist, writer = turtle_setup()
    artist.penup()
    artist.setpos(x, y)
    artist.pendown()
    artist.circle(radius)


def problem6():
    """Use the screen and turtle defined below to solve the problem specified in the exam document."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # TODO 6: Write code to solve the problem as described in the GR document.

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
    screen.setup(WIDTH, HEIGHT, MARGIN, MARGIN)
    screen.bgcolor("SkyBlue")

    # Create two turtles, one for drawing and one for writing.
    artist = turtle.Turtle()
    writer = turtle.Turtle()

    # Change the artist turtle's shape so the artist and writer are distinguishable.
    artist.shape("turtle")

    # Make the animation as fast as possible and hide the turtles.
    if DRAW_FAST:
        screen.delay(0)
        artist.hideturtle()
        artist.speed("fastest")
        writer.hideturtle()
        writer.speed("fastest")

    # Set a few properties of the writing turtle useful since it will only be writing.
    writer.setheading(90)  # Straight up, which makes it look sort of like a cursor.
    writer.penup()  # A turtle's pen does not have to be down to write text.
    writer.setposition(0, HEIGHT // 2 - FONT_SIZE * 2)  # Centered at top of the screen.

    return screen, artist, writer


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
