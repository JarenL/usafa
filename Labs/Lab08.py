"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: Used the solutions posted on piazza to figure out exercise 2. Used the code to supplement my own
I had written.
=======================================================================
"""

# Import specific functions from the math library, just to demonstrate how to do it.
from math import atan2, sqrt, degrees
import easygui
import turtle


# Define several useful constants to be used by the Turtle graphics.
WIDTH = 640              # A smaller window for this problem.
HEIGHT = WIDTH           # A square window for this problem.
MARGIN = 32              # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = 16           # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False        # Set to True for fast, non-animated turtle movement.


def main():
    """Main program to test solutions for each problem."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise1()
    # exercise2()
    exercise3()


def exercise1():
    """Odd and Even Sums exercise."""
    # TODO 1c: Write code to use the sum_odds and sum_evens functions, as described in the lab document.
    number1 = int(easygui.integerbox(msg="Number: ", title="Lab08", default="", lowerbound=int(0)))
    odd = sum_odds(number1)
    even = sum_evens(number1)
    easygui.msgbox(msg="Number:" + str(number1) + " " + "sum of evens:" + str(even) + " " + "sum of odds:" + str(odd),
    title="results", ok_button="Cool")

# TODO 1a: In the space below, write the sum_odds function as described in the lab document.
def sum_odds(number1):
    count = 0
    for num in range(1, number1 + 1, 2):
        count += num
    return count

# TODO 1b: In the space below, write the sum_evens function as described in the lab document.
def sum_evens(number1):
    count = 0
    for num in range(2, number1 + 1, 2):
        count += num
    return count


def exercise2():
    """Summations exercise."""
    # TODO 2b: Write code to use the summation function, as described in the lab document.
    number = int(easygui.integerbox(msg="n: ", title="Lab08", default="", lowerbound=(0), upperbound=(32)))
    some = summation(number, 1)
    formula = number * (number + 1) / 2
    easygui.msgbox("n = {}, summation(n,1) = {}, formula result = {}". format(number, some, formula))

    some = summation(number, 2)
    formula = number * (number + 1) * (2 * number + 1) / 6
    easygui.msgbox("n = {}, summation(n,1) = {}, formula result = {}". format(number, some, formula))

    some = summation(number, 3)
    formula = (number * (number + 1) / 2)**2
    easygui.msgbox("n = {}, summation(n,1) = {}, formula result = {}". format(number, some, formula))

# TODO 2a: In the space below, write the summation function as described in the lab document.
def summation(n, value):
    """

    :param n:
    :param value:
    :return:
    """
    count = 0
    for num in range(1, n+1):
        count += num ** value
    return count


def exercise3():
    """Use the screen and turtle defined below to solve the given exercise."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # TODO 3b: In the space below, write code to use the draw_inner_square function, as described in the lab document.
    draw_square(artist, 200)
    draw_inner_square(artist, 200, 0.25)
    easygui.msgbox("Click ok")
    artist.clear()

    # TODO 3d: In the space below, write code to use the draw_inner_squares function, as described in the lab document.
    draw_square(artist, 200)
    draw_inner_square(artist, 200, 9)
    artist.penup()
    artist.setpos( -120, 0)
    artist.pendown()
    draw_square(artist, 100)
    draw_inner_square(artist, 100, 4)
    artist.penup()
    artist.setpos(-120, -300)
    artist.pendown()
    draw_square(artist, 280)
    draw_inner_square(artist, 280, 2)
    easygui.msgbox("Click Ok")
    artist.clear()

    # TODO 3f: In the space below, write code to use the draw_art function, as described in the lab document.
    draw_art(artist, WIDTH - MARGIN * 2)

    # Wait for the user to click before closing the window (leave this as the last line).
    screen.exitonclick()


# TODO 3a: In the space below, write the draw_inner_square function as described in the lab document.
def draw_inner_square(turt, outer, percent):
    """

    :param turt: what to draw with
    :param outer: Length of outer side.
    :param percent: The percentage of one side to find corner.
    :return:
    """
    first = outer * percent
    second = outer - first
    alpha = degrees( atan2(first, second))
    inner_size = int(sqrt(first ** 2 + second ** 2))
    turt.penup()
    turt.forward(second)
    turt.pendown()
    turt.left(90 - alpha)
    draw_square(turt, inner_size)
    turt.penup()
    turt.right(90 - alpha)
    turt.back(second)
    turt.pendown()

# TODO 3c: In the space below, write the draw_inner_squares function as described in the lab document.
def draw_inner_squares(art, out_size, how_many):
    """

    :param art:
    :param out_size:
    :param how_many:
    :return:
    """
    for square in range(1, how_many + 1):
        draw_inner_square(art, out_size, square / (how_many + 1))

# TODO 3e: In the space below, write the draw_art function as described in the lab document.
def draw_art(art, outer_size):
    """

    :param art:
    :param outer_size:
    :return:
    """
    positions = [(0, 0), (0, -outer_size / 2), (-outer_size / 2, 0), (-outer_size / 2, -outer_size / 2)]
    for position in positions:
        art.penup()
        art.setposition(position)
        art.pendown()
        draw_square(art, outer_size / 2)
        draw_inner_square(art, outer_size / 2, 14)
    # Leave this function below those written in steps 3a, 3c, and 3e.
def draw_square( art, size ):
    """Use the given turtle to draw a square with one corner at the turtle's current location.

    :param turtle.Turtle art: The turtle to do the drawing.
    :param int size: The length of one side of the square.
    """
    for _ in range( 4 ):
        art.forward( size )
        art.left( 90 )


def turtle_setup():
    """Setup the turtle environment with a screen and two turtles, one for drawing and one for writing.

    Using separate turtles for drawing and writing makes it easy to clear one or the other by
    doing artist.clear() or writer.clear() to clear only the drawing or writing, respectively.

    :return: The screen, a drawing turtle, and a writing turtle.
    :rtype: (turtle.Screen, turtle.Turtle, turtle.Turtle)
    """
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