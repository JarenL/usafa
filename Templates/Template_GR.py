"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Note: THIS DOCUMENT IS UNDER ACADEMIC SECURITY ONCE COMPLETED.
"""

import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960              # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 / 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = 32              # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = 16           # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False        # Set to True for fast, non-animated turtle movement.


def main():
    """Main program to test solutions for each problem."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual problem; comment/un-comment these lines as you work.
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()


def problem1():
    """Delete the 'pass' statement and write code to solve the given problem."""
    pass


def problem2():
    """Delete the 'pass' statement and write code to solve the given problem."""
    pass


def problem3():
    """Delete the 'pass' statement and write code to solve the given problem."""
    pass


def problem4():
    """Delete the 'pass' statement and write code to solve the given problem."""
    pass


def problem5():
    """Use the screen and turtle defined below to solve the given problem."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # Delete the 'pass' statement and write code to solve the given problem.
    pass

    # Wait for the user to click before closing the window (leave this as the last line).
    screen.exitonclick()


def problem6():
    """Use the screen and turtle defined below to solve the given problem."""
    # Create the turtle screen and two turtles (leave this as the first line of main).
    screen, artist, writer = turtle_setup()

    # Delete the 'pass' statement and write code to solve the given problem.
    pass

    # Wait for the user to click before closing the window (leave this as the last line of main).
    screen.exitonclick()


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
