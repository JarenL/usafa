"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import math
import random
import turtle
import time
import sys


# ###################################################################### #
# NOTE: The main() function, remaining constant definitions, and various #
# other utility functions have been moved to the bottom of this file     #
# because YOU DO NOT NEED TO EDIT ANY OF THIS CODE. Your work will be    #
# done in the recursive functions immediately following this comment.    #
# ###################################################################### #


# ################### #
# Sierpinski Triangle #
# ################### #
def draw_sierpinski_triangle( artist ):
    """Draw the initial triangle and start the recursion for the Sierpinski Triangle.

    http://en.wikipedia.org/wiki/Sierpinski_triangle

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # Build the first, largest triangle to get started, creating points as tuples
    # with two integer values (x,y) and a triangle as a tuple of three points.
    top = ( 0, HEIGHT // 2 - MARGIN )
    left = ( -WIDTH // 2 + MARGIN, -HEIGHT // 2 + MARGIN )
    right = (  WIDTH // 2 - MARGIN, -HEIGHT // 2 + MARGIN )
    triangle = ( top, left, right )

    # Draw a single large triangle filling the entire window.
    artist.color( "Blue" )
    fill_triangle( artist, triangle )

    # The Sierpinski Triangle pattern is now achieved by recursively erasing inner triangles.
    # NOTE: The version in the book avoids this by drawing smaller triangles in a different color.
    artist.color( "White" )

    # Start the recursion with the initial triangle and depth=3.
    sierpinski_triangle( artist, triangle, 3 )


def sierpinski_triangle( artist, triangle, depth ):
    """Draws the Sierpinski Triangle pattern within the given triangle.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param ((int, int), (int, int), (int, int)) triangle: A tuple of three (x,y) coordinates.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Nothing to do in the base case, so test the condition to keep going.
    # Specifically, if the points of the triangle are sufficiently far apart.
    if depth > 0 and distance_between( triangle[ 0 ], triangle[ 1 ] ) > 4:
        # "Unpack" the points from the triangle tuple.
        top, left, right = triangle

        # Find the midpoint of each side of the triangle.
        left_mid = midpoint( left, top )
        right_mid = midpoint( right, top )
        bottom_mid = midpoint( left, right )

        # Fill (i.e., erase since tom is drawing in white) the inner triangle.
        fill_triangle( artist, ( bottom_mid, left_mid, right_mid ) )

        # Recursively draw the same pattern in each of the smaller triangles.
        # Note the last parameter decreases depth by one in each recursive call.

        # TODO 1a: Un-comment the line below to draw the pattern inside the top triangle.
        sierpinski_triangle( artist, ( top, left_mid, right_mid ), depth - 1 )

        # TODO 1b: Un-comment the line below to draw the pattern inside the left triangle.
        sierpinski_triangle( artist, ( left_mid, left, bottom_mid ), depth - 1 )

        # TODO 1c: Un-comment the line below to draw the pattern inside the left triangle.
        sierpinski_triangle( artist, ( right_mid, bottom_mid, right ), depth - 1 )

        # TODO 1d: Rearrange the order of the above three lines of code and re-run the program.

        # TODO 1e: The last line of the draw_sierpinski_triangle() function calls the recursive
        # TODO 1e: sierpinski_triangle() function with the actual depth parameter value of 3.
        # TODO 1e: Change this value to 4 and re-run the program. Change it to 5 run again.
        # TODO 1e: Do you have the patience to try 6 or 7? If you do and want to stop,
        # TODO 1e: press Escape to exit the drawing and see the menu immediately.


def distance_between( p1, p2 ):
    """Calculate and return the distance between two points.

    :param (int, int) p1: The first point, stored as an (x,y) tuple.
    :param (int, int) p2: The second point, stored as an (x,y) tuple.
    """
    # Unpack the point tuples into x,y coordinates.
    x1, y1 = p1
    x2, y2 = p2
    # Calculate and return the distance between the two points.
    return math.hypot( x1 - x2, y1 - y2 )


def midpoint( p1, p2 ):
    """Create and return the midpoint between two points, stored as (x,y) tuples.

    :param (int, int) p1: The first point, stored as an (x,y) tuple.
    :param (int, int) p2: The second point, stored as an (x,y) tuple.
    :return: The midpoint between p1 and p2.
    :rtype: (int, int)
    """
    # Unpack the point tuples into x,y coordinates.
    x1, y1 = p1
    x2, y2 = p2
    # Calculate and return the midpoint as a new (x,y) tuple.
    return ( x1 + x2 ) / 2, ( y1 + y2 ) / 2


def fill_triangle( artist, triangle ):
    """Fills a triangle with the given points.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param ((int, int), (int, int), (int, int)) triangle: A tuple of three (x,y) coordinates.
    """
    # Lift the pen and move to the first point in the triangle.
    artist.penup()
    artist.setposition( triangle[ 0 ] )
    artist.pendown()
    # Begin filling and move to the second and third points,
    # and then back to the first point to close the triangle.
    artist.begin_fill()
    artist.setposition( triangle[ 1 ] )
    artist.setposition( triangle[ 2 ] )
    artist.setposition( triangle[ 0 ] )
    artist.end_fill()


# ################# #
# Sierpinski Carpet #
# ################# #
def draw_sierpinski_carpet( artist ):
    """Start the recursion for the Sierpinski Carpet.

    http://en.wikipedia.org/wiki/Sierpinski_carpet

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # No need to draw anything before getting started, so just call the recursive
    # function with the center and size of the entire carpet and recursive depth=3.
    sierpinski_carpet( artist, 0, 0, WIDTH, HEIGHT, 3 )


def sierpinski_carpet( artist, center_x, center_y, width, height, depth ):
    """Uses the given turtle to draw the Sierpinski Carpet.

    http://en.wikipedia.org/wiki/Sierpinski_carpet

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int center_x: The x-coordinate of the center of the current carpet segment.
    :param int center_y: The y-coordinate of the center of the current carpet segment.
    :param int width: The width of the current carpet segment.
    :param int height: The height of the current carpet segment.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Nothing to do in the base case, so test the condition to keep going.
    # Specifically, if the piece of carpet is large enough to split.
    if depth > 0 and min( width, height ) > 3:
        # Temporary variables to hold the width and height of each of the
        # nine smaller sub-carpets that need to be drawn.
        w = width // 3
        h = height // 3

        # Fill the center sub-carpet.
        fill_rect( artist, center_x, center_y, w, h )

        # Recursively draw the pattern in each of the other eight sub-carpets.
        sierpinski_carpet( artist, center_x + w, center_y + h, w, h, depth - 1 )

        # TODO 2a: Make a copy of the above line and change the additions
        # TODO 2a: to subtractions. Run the program and observe the result.
        sierpinski_carpet(artist, center_x - w, center_y - h, w, h, depth - 1)

        # TODO 2b: Make six more copies of the above line, ONE AT A TIME, for each
        # TODO 2b: of the remaining directions in the pattern. That is, there will
        # TODO 2b: be one that does -w and +h, one that does +w and -h, one that
        # TODO 2b: only does +h, one that only does -h, one that only does +w,
        # TODO 2b: and one that only does -w. Run the program after adding each
        # TODO 2b: individual line and observe the result.
        sierpinski_carpet(artist, center_x - w, center_y + h, w, h, depth - 1)
        sierpinski_carpet(artist, center_x + w, center_y - h, w, h, depth - 1)
        sierpinski_carpet(artist, center_x, center_y + h, w, h, depth - 1)
        sierpinski_carpet(artist, center_x, center_y - h, w, h, depth - 1)
        sierpinski_carpet(artist, center_x - w, center_y, w, h, depth - 1)
        sierpinski_carpet(artist, center_x + w, center_y, w, h, depth - 1)

        # TODO 2c: Rearrange the above recursive calls so the pattern fills starting with
        # TODO 2c: the upper-right and moving clockwise. That is, if the pattern were the
        # TODO 2c: numbers on a telephone and the center square were the 5, it would fill
        # TODO 2c: the following squares in the order 3, 6, 9, 8, 7, 4, 1, 2.

        # TODO 2d: Change the initial depth of the recursion (last line of
        # TODO 2d: draw_sierpinski_carpet function) and re-run the program.


def fill_rect( artist, x, y, w, h ):
    """Fills a rectangle centered at (x,y).

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int x: The x-coordinate of the center of the rectangle.
    :param int y: The y-coordinate of the center of the rectangle.
    :param int w: The width of the rectangle.
    :param int h: The height of the rectangle.
    """
    # Lift the pen and move to a corner of the rectangle.
    artist.penup()
    artist.setposition( x - w // 2, y + h // 2 )
    artist.pendown()
    # Draw a filled rectangle.
    artist.begin_fill()
    for side in range( 2 ):
        artist.forward( w )
        artist.right( 90 )
        artist.forward( h )
        artist.right( 90 )
    artist.end_fill()


# ###################### #
# Sierpinski-ish Circles #
# ###################### #
def draw_sierpinski_circles( artist ):
    """Start the recursion for the Sierpinski-ish Circles.

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # No need to draw anything before getting started, so just call the recursive
    # function with the center and size of the initial circle and recursive depth=3.
    sierpinski_circles( artist, 0, 0, ( WIDTH + HEIGHT ) // 8, 3 )


def sierpinski_circles( artist, center_x, center_y, radius, depth ):
    """Uses the given turtle to draw filled circles in a Sierpinski-ish pattern.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int center_x: The x-coordinate of the center of the current circle.
    :param int center_y: The y-coordinate of the center of the current circle.
    :param int radius: The radius of the current circle.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # If the circle size is large enough, keep going.
    if depth > 0 and radius > 1:
        # Move the turtle to the center of the circle and draw a dot.
        artist.setposition( center_x, center_y )
        artist.dot( radius * 2 )

        # Recursively draw smaller circles in each diagonal direction.
        sierpinski_circles( artist, center_x - radius, center_y + radius, radius // 2, depth - 1 )

        # TODO 3a: Make three copies of the above line for each of the other diagonal directions.
        # TODO 3a: This is very similar to the carpet pattern, but it only moves diagonally.
        sierpinski_circles(artist, center_x - radius, center_y - radius, radius // 2, depth - 1)
        sierpinski_circles(artist, center_x + radius, center_y - radius, radius // 2, depth - 1)
        sierpinski_circles(artist, center_x + radius, center_y + radius, radius // 2, depth - 1)

        # TODO 3b: Arrange your recursive calls so the pattern draws counter-clockwise.

        # TODO 3c: Move the three lines of code from above that position the turtle and draw the dot
        # TODO 3c: (ok, two lines of code and one comment) so they are BELOW the recursive calls.
        artist.setpos( center_x, center_y)
        artist.dot(radius * 2)
        # TODO 3d: Change the initial depth of the recursion and re-run the program.


# ###### #
# H-Tree #
# ###### #
def draw_h_tree( artist ):
    """Start the recursion for the H-Tree.

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # No need to draw anything before getting started, so just call the recursive
    # function with the center and size of the initial H and recursive depth=3.
    h_tree( artist, 0, 0, ( WIDTH + HEIGHT ) // 4, 3 )


def h_tree( artist, center_x, center_y, size, depth ):
    """ Recursively draws an H-tree.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int center_x: The x-coordinate of the center of the current H.
    :param int center_y: The y-coordinate of the center of the current H.
    :param int size: The size of the current H.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # If the H size is large enough, keep going.
    if depth > 0 and size > 4:
        # Draw the center horizontal line.
        draw_line( artist, center_x - size//2, center_y, center_x + size//2, center_y )
        # Draw the left vertical line.
        draw_line( artist, center_x - size//2, center_y - size//2, center_x - size//2, center_y + size//2 )
        # Draw the right vertical line.
        draw_line( artist, center_x + size//2, center_y - size//2, center_x + size//2, center_y + size//2 )

        # TODO 4a: Recursively draw a smaller H in each direction.
        # TODO 4a: This time none of the recursive calls are provided, so you must
        # TODO 4a: write all four. Don't panic ... they are very similar to the circles
        # TODO 4a: in the previous problem. The size of each H is decreased by half
        # TODO 4a: and the center point of each H is either increased or decreased
        # TODO 4a: by half of the size. Run the program after adding each individual
        # TODO 4a: recursive call and observe the result.
        h_tree(artist, center_x - size // 2, center_y + size // 2, size // 2, depth - 1)
        h_tree(artist, center_x + size // 2, center_y + size // 2, size // 2, depth - 1)
        h_tree(artist, center_x - size // 2, center_y - size // 2, size // 2, depth - 1)
        h_tree(artist, center_x - size // 2, center_y - size // 2, size // 2, depth - 1)

        # TODO 4b: Move the six lines of code from above that draw the lines (ok, three lines
        # TODO 4b: of code and three comments) so they are BELOW the recursive calls.

        # TODO 4c: Move the two lines of code that draw the center horizontal line
        # TODO 4c: back above the recursive calls. Run the program.

        # TODO 4d: Change the initial depth of the recursion and re-run the program.


def draw_line( artist, x1, y1, x2, y2 ):
    """Draws a line between the two given points.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int x1: The x-coordinate of the first endpoint of the line.
    :param int y1: The y-coordinate of the first endpoint of the line.
    :param int x2: The x-coordinate of the second endpoint of the line.
    :param int y2: The y-coordinate of the second endpoint of the line.
    """
    artist.penup()
    artist.setposition( x1, y1 )
    artist.pendown()
    artist.setposition( x2, y2 )


# ########## #
# Leafy Tree #
# ########## #
FALL_COLORS = [ "Red", "Orange", "OrangeRed", "Purple", "Orchid", "ForestGreen", "SandyBrown" ]


def draw_leafy_tree( artist ):
    """Start the recursion for the leafy tree.

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # Center the turtle horizontally, toward the bottom of the screen.
    artist.penup()
    artist.setposition( 0, -HEIGHT // 3 )
    artist.pendown()
    artist.setheading( 90 )  # Straight up.
    artist.color( "Brown" )  # The tree trunk and branches are brown.
    # Start the recursion with the initial branch length and depth=3.
    leafy_tree( artist, HEIGHT // 5, 3 )


def leafy_tree( artist, branch_length, depth ):
    """Recursively draws a leafy tree.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int branch_length: The current branch length.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # Finally, there is something to do in the base case ... draw a leaf!
    if depth <= 0 or branch_length < 4:
        # TODO 5c: Note ... do this last, after completing 5a and 5b below ...
        # TODO 5c: Draw a leaf using tom.dot() with a random pixel size between
        # TODO 5c: 4 and 8 pixels. Also, use random.choice() to get a random
        # TODO 5c: color from the list of FALL_COLORS defined above.
        # TODO 5c: Remember to set the color back to Brown after drawing the leaf!
        pass  # Write your code here (and remove this comment).

    else:
        # Use the recursion depth as the circumference of the branch
        # (i.e., turtle pensize), so the branches are thinner near the end.
        artist.pensize( depth )
        artist.forward( branch_length )

        # Turn slightly to the right and recursively draw a smaller tree.
        artist.right( 30 )
        leafy_tree( artist, branch_length * 3 // 4, depth - 1 )

        # TODO 5a: Copy the two lines above and change the right( 30 ) to left( 60 )
        # TODO 5a: so the left smaller tree will be 30 degrees to the left.
        # TODO 5a:
        # TODO 5a: Next, add two more lines of code that turn the turtle right( 30 )
        # TODO 5a: so it is pointing straight up again and then move the turtle backward
        # TODO 5a: the branch length so it is back in its original position.
        # TODO 5a:
        # TODO 5a: Run the program and observe the results.
        # TODO 5a: How did adding a recursive call with a left turn end
        # TODO 5a: up drawing so many more right branches as well? Fun!
        artist.left(60)
        leafy_tree(artist, branch_length * 3 // 4, depth - 1)
        artist.right(30)
        artist.backward(branch_length)

        # TODO 5b: The above modifications draw a very balanced tree. The images in the
        # TODO 5b: lab document show a more natural looking tree drawn by turning left 80
        # TODO 5b: degrees and drawing the smaller tree with two-thirds the branch size.
        # TODO 5b: Make these modifications to your code.
        # TODO 5b: NOTE: However far left the turtle turns, it must turn right to point straight up.
        artist.left(80)
        leafy_tree(artist, branch_length * 2 // 3, depth - 1)
        artist.right(50)
        artist.backward(branch_length)

        # TODO 5d: Change the initial depth of the recursion and re-run the program.


# ############## #
# Koch Snowflake #
# ############## #
def draw_koch_snowflake( artist ):
    """Start the recursion for the Koch Snowflake.

    :param turtle.Turtle artist: The turtle to do the drawing.
    """
    # The size of the snowflake to fill about two-thirds of the screen.
    size = min( WIDTH, HEIGHT ) * 2 // 3
    # Center the turtle horizontally, at the top tip of the snowflake,
    # which is above the center by about 60% of the size of the snowflake.
    artist.penup()
    artist.setposition( 0, size * 3 // 5 )
    artist.pendown()
    # Facing down the side of the first equilateral triangle.
    artist.setheading( 300 )
    # Start the recursion with the length of the side of the
    # triangle and the recursion depth=3.
    koch_snowflake( artist, size, 3 )


def koch_snowflake( artist, size, depth ):
    """Uses a loop to draw the three sides of the snowflake. (Yes, a loop.)

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int size: The size of the current side of the snowflake.
    :param int depth: The current depth of the recursion.
    """
    for side in range( 3 ):
        snowflake_side( artist, size, depth )
        artist.right( 120 )


def snowflake_side( artist, length, depth ):
    """Recursively draws one side of the snowflake.

    :param turtle.Turtle artist: The turtle to do the drawing.
    :param int length: The length of one side of the snowflake.
    :param int depth: The current depth of the recursion.
    """
    # Stop the recursion if the user presses the Escape key.
    if key_press.escape:
        return

    # TODO 6: Complete the code below to draw the Koch Snowflake.
    # TODO 6: Drawing a single straight line is the correct action in the base case.
    # TODO 6: Replace the True in the if-statement with an appropriate condition that
    # TODO 6: tests both the depth and length variables.
    # TODO 6: Then, replace the pass statement in the else clause with appropriate
    # TODO 6: recursive calls and turns to draw the rest of the snowflake.
    # TODO 6: There will be four recursive calls since each straight edge of a
    # TODO 6: larger triangle is divided into four pieces. The length of each
    # TODO 6: of these smaller edges will be one-third of the current length.
    # TODO 6: Also, don't forget to subtract one from the depth variable in
    # TODO 6: each recursive call. Finally, recall the inner angles of an
    # TODO 6: equilateral triangle are sixty degrees.
    if True:
        artist.forward( length )
    else:
        snowflake_side(artist, length // 3, depth - 1)
        artist.left(60)
        snowflake_side(artist, length // 3, depth - 1)
        artist.right(120)
        snowflake_side(artist, length // 3, depth - 1)
        artist.left(60)
        snowflake_side(artist, length // 3, depth - 1)


# NOTE: See note at top of file about why these constants are down here.
#      ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
#     |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
#     | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
#     |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
#  _____ _  _ ___ ___ ___    ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___
# |_   _| || | __/ __| __|  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|
#   | | | __ | _|\__ \ _|   | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \
#   |_| |_||_|___|___/___|  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/
#
WIDTH = 640             # Usually 640, 800, 1024, or 1200
HEIGHT = WIDTH          # A square window for this application.
MARGIN = WIDTH // 40    # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = False       # Set to True for faster drawing.

# The following constants are used by show_menu() and menu_click().
OPTIONS = [ "Sierpinski Triangle", "Sierpinski Carpet", "Sierpinski-ish Circles",
            "H Tree", "Leafy Tree", "Koch Snowflake", "Exit" ]
FONT_SIZE = HEIGHT // 4 // len( OPTIONS )
BUTTON_SIZE = FONT_SIZE * 4


# NOTE: See note at top of file about why this function is down here.
def main():
    """Main program to show menu of recursive drawing functions."""
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
    screen.bgcolor( "White" )
    screen.title( "Visualizing Recursion" )

    # Make the animation as fast as possible.
    if DRAW_FAST:
        screen.delay( 0 )

    # Create a turtle to do the drawing, making it stealthy and fast.
    artist = turtle.Turtle()
    artist.hideturtle()
    artist.speed( "fastest" )
    artist.color( "Blue" )

    # Show initial menu; it is re-drawn at the end of menu_click, after drawing something.
    show_menu( artist )

    # Tell the system to call menu_click when the turtle screen is clicked.
    screen.onclick( menu_click )

    # Tell the system to call key_press when the Escape key is pressed
    # and then start listening for key presses.
    screen.onkey( key_press, key="Escape" )
    screen.listen()

    # Start the main loop that listens for mouse clicks and key presses.
    screen.mainloop()


def show_menu( artist ):
    """Show a menu of options, spaced nicely on the screen.

    :param turtle.Turtle artist: The turtle to do the drawing.
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
    # Clear everything tom has drawn and move to the top, center of the window.
    artist.clear()
    artist.penup()
    artist.color( "Blue" )
    artist.setposition( 0, HEIGHT // 2 - BUTTON_SIZE * 3 // 4 )
    artist.setheading( 270 )  # Straight down.
    for option in OPTIONS:
        artist.write( option, align="center", move=False, font=( "Courier", FONT_SIZE, "bold" ) )
        artist.forward( BUTTON_SIZE )  # Move down to the next button location.

    # See the note about function attributes in the key_press() function.
    key_press.escape = False


def menu_click( x, y ):
    """Figures out which 'button' was pressed and draws the appropriate image.

    :param int x: The x-coordinate of the mouse click (required, but not used in this application).
    :param int y: The y-coordinate of the mouse click.
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
    # The turtle screen is a "Singleton Object", which means there is only one.
    # When this line of code is called in main(), it creates the new screen.
    # When this line of code is called here, it gets the already created screen.
    screen = turtle.Screen()

    # Don't listen for more clicks while drawing the current shape.
    screen.onclick( None )

    # Shift and invert the y-coordinate so it is a positive number with 0 at the top of the screen.
    # This way, when divided by BUTTON_SIZE, it can be used as an index into the OPTIONS list.
    y = HEIGHT - ( y + HEIGHT // 2 )
    option = OPTIONS[ int( y // BUTTON_SIZE ) ]

    # Since this function can only receive two parameters from the system, we have
    # to get our faithful artist turtle from the screen's list of all turtles.
    artist = screen.turtles()[ 0 ]  # First in the list since there is only one.
    artist.clear()
    artist.penup()
    artist.home()
    artist.pensize( 1 )

    # Figure out which shape is being requested and draw it.
    if option == "Sierpinski Triangle":
        draw_sierpinski_triangle( artist )
    elif option == "Sierpinski Carpet":
        draw_sierpinski_carpet( artist )
    elif option == "Sierpinski-ish Circles":
        draw_sierpinski_circles( artist )
    elif option == "H Tree":
        draw_h_tree( artist )
    elif option == "Leafy Tree":
        draw_leafy_tree( artist )
    elif option == "Koch Snowflake":
        draw_koch_snowflake( artist )
    else:
        screen.bye()  # Closes the turtle screen.
        sys.exit()    # Actually stops the program.

    # Pause for a few seconds to admire the pretty picture, then show the menu again.
    # (Skip the pause of the user impatiently presses the Escape key.)
    if not key_press.escape:
        time.sleep( 3 )
    show_menu( artist )

    # Start listening for clicks again.
    screen.onclick( menu_click )


def key_press():
    """Called by the system when the user presses the Escape key."""
    #  ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
    # |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
    # | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
    # |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
    #  _____ _  _ ___ ___    ___ _   _ _  _  ___ _____ ___ ___  _  _
    # |_   _| || |_ _/ __|  | __| | | | \| |/ __|_   _|_ _/ _ \| \| |
    #   | | | __ || |\__ \  | _|| |_| | .` | (__  | |  | | (_) | .` |
    #   |_| |_||_|___|___/  |_|  \___/|_|\_|\___| |_| |___\___/|_|\_|
    #
    # Use a function attribute to indicate a key has been pressed. For more
    # on function attributes: http://legacy.python.org/dev/peps/pep-0232/
    key_press.escape = True
    """:type: bool"""


# Before starting main(), set the initial value of the key press function attribute.
key_press.escape = False


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()