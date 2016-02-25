"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import math
import random
import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960               # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 // 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = WIDTH // 30      # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = MARGIN // 2   # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False         # Set to True for fast, non-animated turtle movement.

COLORS = [ "red", "green", "blue", "yellow", "cyan", "magenta", "white", "black" ]


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    exercise0()
    exercise1()
    exercise2()


class Point:
    """Point class for representing (x,y) coordinates."""

    # TODO 0a: Read, discuss, and understand the following code.
    def __init__( self, x=0, y=0 ):
        """Create a new Point with the given x and y values.

        :param int x: The x-coordinate; default is zero.
        :param int y: The y-coordinate; default is zero.
        """
        # Assign the x and y values passed as parameters as attributes of self.
        self.x = x
        self.y = y

    # TODO 0c: Read, discuss, and understand the following code.
    def draw( self, art ):
        """Draw this Point object using the given turtle.

        :param turtle.Turtle art: The turtle to use to draw this Point object.
        :return: None
        """
        # Use the self object's x and y values to set the heading.
        art.setheading( art.towards( self.x, self.y ) )
        # Use the self object's x and y values to move the turtle.
        art.setposition( self.x, self.y )
        # Draw a dot at the point.
        art.dot( 4 )


def exercise0():
    """Demonstrate a Point class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Point objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # TODO 0b: Read, discuss, and understand the following code.
    points = []  # An empty list to be filled with Point objects.
    y = HEIGHT // 4  # Start the y-coordinate one-quarter screen height above the x-axis.
    # Loop through evenly spaced x-coordinates.
    for x in range( -WIDTH // 2 + MARGIN, WIDTH // 2 + MARGIN, ( WIDTH - MARGIN * 2 ) // 8 ):
        p = Point( x, y )  # Use the values of x and y to create a Point object.
        points.append( p )  # Appends the point to the list of point objects.
        y *= -1  # Modify y so the points alternate above and below the x-axis.

    # TODO 0d: Read, discuss, and understand the following code.
    # Loop through the list of Point objects and tell each to draw itself.
    for p in points:
        # Tell the Point object to draw itself using the artist turtle.
        print(p, flush=True)
        p.draw( artist )

    # Wait for the user to click before closing the window (leave this as the last line).
    artist.home()
    screen.exitonclick()


# TODO 1a: In the space below this comment, write the class as described in the lab document.
class Spot:
    SIZE = 32
    def __init__(self):
        """

        :return:
        """
        self.x = x
        self.y = y
        self.c = c

    def __str__(self):
        return "({}, {}):{}".format(self.x, self.y, self.c)

    def draw(self,art):
        art.setheading(art.towards(self.x, self.y))
        art.setposition(self.x, self.y)
        art.dot(Spot.SIZE, self.c)
        d = Spot.SIZE // 2
def exercise1():
    """Test a Spot class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Spot objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # TODO 1b: In the space below, use the class as described in the lab document.
    dx = (WIDTH - MARGIN * 2) // len(COLORS)
    dy = (HEIGHT - MARGIN * 2) // len(COLORS)
    x = -WIDTH // 2 + MARGIN + dx // 2
    y = -HEIGHT // 2 + MARGIN + dy // 2
    # Wait for the user to click before closing the window (leave this as the last line).

    spots = []
    for colors in COLORS:
        s = Spot(x, y, color)
        spots.append(s)
        x += dx
        y += dy
    for s in spots:
        print(s, flush=True)
        s.draw(artist)
    artist.home()
    screen.exitonclick()


# TODO 2a: In the space below this comment, write the class as described in the lab document.

class Raindrop:
    SIZE = 32
    def __init__(self):
        """

        :return:
        """
        self.x = x
        self.y = y
        self.c = c

    def __str__(self):
        return "({}, {}):{}".format(self.x, self.y, self.c)

    def draw(self,art):
        art.setheading(art.towards(self.x, self.y))
        art.setposition(self.x, self.y)
        art.dot(Spot.SIZE, self.c)
        d = Spot.SIZE // 2
def exercise2():
    """Test a Raindrop class."""
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()
    writer.write( "Creating and drawing Raindrop objects...",
                  align="center", font=( "Times", FONT_SIZE, "bold" ) )

    # Make the artist turtle a blue circle for this application.
    # artist.color( 'blue' )
    # artist.shape( "circle" )

    # TODO 2b: In the space below, use the class as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code.

    # Wait for the user to click before closing the window (leave this as the last line).
    artist.home()
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
    # Lift the artist's pen and slow it down to see the movements from object to object.
    artist.penup()
    artist.speed( "slowest" )

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