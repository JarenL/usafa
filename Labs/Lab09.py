"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import easygui
import math
import random
import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960  # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 // 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = WIDTH // 30  # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = MARGIN // 2  # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = True  # Set to True for fast, non-animated turtle movement.


def main():
    """Main program to test solutions for each problem."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print(__doc__)

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    #exercise5()
    #exercise6()
    #exercise7()


def exercise1():
    """Interact with the user and test the even_odd function."""

    # TODO 1b: Write code to use the even_odd function as described in the lab document.
    int_check = easygui.integerbox("Enter number:", "Input", lowerbound=0)
    easygui.msgbox(even_odd(int_check))


# TODO 1a: In the space below, write the even_odd function as described in the lab document.
def even_odd(value):
    """

    :param value: The inputted number.
    :return "Even": If value is even.
    :return "Odd": If value is odd.
    """
    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"


def exercise2():
    """Interact with the user and test the pass_fail function."""


    # TODO 2b: Write code to use the pass_fail function as described in the lab document.
    pass_check = easygui.integerbox("Enter Grade:", "Input", lowerbound=0, upperbound=100)
    easygui.msgbox(pass_fail(pass_check))


# TODO 2a: In the space below, write the pass_fail function as described in the lab document.
def pass_fail(number):
    """
    :param number: The number user inputs.
    :return "Pass": Returns if number is greater or equal to 70.
    :return "Fail": Returns if number is less than 70.
    """
    if number >= 70:
        return "Pass"
    else:
        return "Fail"


def exercise3():
    """Interact with the user and test the residence_hall function."""
    # TODO 3b: Write code to use the residence_hall function as described in the lab document.
    sq_location = easygui.integerbox("Enter Squadron:", "Input", lowerbound=1, upperbound=40)
    easygui.msgbox(residence_hall(sq_location), "Result")


# TODO 3a: In the space below, write the residence_hall function as described in the lab document.
def residence_hall(number):
    """

    :param number: The number the user inputted in integerbox.
    :return "Sijan": Returns sijan if input is greater than 23.
    :return "Vandy": Returns Vandy if input is less than 23.
    """
    if number > 23:
        return "Sijan"
    else:
        return "Vandy"


def exercise4():
    """Interact with the user and test the days_in_year function."""
    # TODO 4b: Write code to use the days_in_year function as described in the lab document.
    year = easygui.integerbox("Enter year", "Input", lowerbound=0, upperbound=999999)
    easygui.msgbox(days_in_year(year), "Result")


# TODO 4a: In the space below, write the days_in_year function as described in the lab document.
def days_in_year(number):
    """

    :param number: The number value from input.
    :return: IF year is 365 days or 366 days.
    """
    if number % 4 == 0 and (number % 100 != 0 or number % 400 == 0):
        return "The year has 366 days"
    else:
        return "The year has 365 days"


def exercise5():
    """Interact with the user and test the count_multiples function."""
    # TODO 5b: Write code to use the count_multiples function as described in the lab document.
    first = easygui.integerbox("Enter start value", "Start")
    second = easygui.integerbox("Enter stop value", "Stop")
    divisor = easygui.integerbox("Enter the divisro", "Divisor")
    easygui.msgbox(count_multiples(first, second, divisor), "Result")


# TODO 5a: In the space below, write the count_multiples function as described in the lab document.

def count_multiples(start, stop, divisor):
    """

    :param start: Lower bound of user input.
    :param stop: upper bound of user input.
    :param divisor: What each value in this range will be divided by.
    :return: How many multiples in the range are divisible by the divisor.
    """
    count = 0
    for num in range(start, stop + 1):
        if num % divisor == 0:
            count += 1
    return "There are {0} multiples of {1} in the range [{2},{3}]".format(str(count), str(divisor), str(start),
                                                                         str(stop))


# Define a random size box/target in a random location for use in the next exercise.
#      ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
#     |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
#     | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
#     |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
#  _____ _  _ ___ ___ ___    ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___
# |_   _| || | __/ __| __|  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|
#   | | | __ | _|\__ \ _|   | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \
#   |_| |_||_|___|___/___|  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/
#
BOX_W = random.randint(WIDTH // 8, WIDTH // 4)  # The width of the box/target.
BOX_H = random.randint(HEIGHT // 8, HEIGHT // 4)  # The height of the box/target.
# The x-coordinate of the lower-left corner of the box/target.
BOX_X = random.randint(-WIDTH // 2 + MARGIN, WIDTH // 2 - BOX_W - MARGIN)
# The y-coordinate of the lower-left corner of the box/target.
BOX_Y = random.randint(-HEIGHT // 2 + MARGIN, HEIGHT // 2 - BOX_H - MARGIN)


def exercise6():
    """Use the screen and turtle defined below to solve the given exercise."""
    #  ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
    # |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
    # | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
    # |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
    #  _____ _  _ ___ ___    ___ _   _ _  _  ___ _____ ___ ___  _  _
    # |_   _| || |_ _/ __|  | __| | | | \| |/ __|_   _|_ _/ _ \| \| |
    #   | | | __ || |\__ \  | _|| |_| | .` | (__  | |  | | (_) | .` |
    #   |_| |_||_|___|___/  |_|  \___/|_|\_|\___| |_| |___\___/|_|\_|
    #
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # Give the user some instructions.
    writer.write("Try to click in the box...", align="center", font=("Arial", FONT_SIZE, "bold"))

    # Draw a box/target in the middle of the screen.
    artist.color("blue")
    artist.penup()
    artist.setposition(BOX_X, BOX_Y)
    artist.pendown()
    artist.begin_fill()
    for _ in range(2):
        artist.forward(BOX_W)
        artist.left(90)
        artist.forward(BOX_H)
        artist.left(90)
    artist.end_fill()

    # Tell the screen to call the click() function when the user clicks on the screen.
    screen.onclick(box_click)

    # Rather than exitonclick(), enter the main event loop to listen for clicks.
    screen.mainloop()


def box_click(x, y):
    """Display a Hit or Miss message if the (x,y) coordinate is in or out of the box drawn in exercise6().

    Note: The "screen.onclick( box_click )" function call in exercise6() results in
    this function being called automatically when the turtle screen is clicked.

    :param int x: The x-coordinate of the click.
    :param int y: The y-coordinate of the click.
    """
    # TODO 6: Replace True in the line below with a single condition to display the appropriate message.


    # TODO 6: Use the existing definitions of BOX_X, BOX_Y, BOX_W, and BOX_H in your selection statement.
    #determines where box's y and z boundaries are.
    if x > BOX_X and x < BOX_W and y > BOX_Y and y < BOX_H:
        easygui.msgbox("Hit!", "Result")
    else:
        easygui.msgbox("Miss", "Result")


# Define random location/size for the earth and moon for use in the next exercise.
#      ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
#     |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
#     | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
#     |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
#  _____ _  _ ___ ___ ___    ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___
# |_   _| || | __/ __| __|  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|
#   | | | __ | _|\__ \ _|   | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \
#   |_| |_||_|___|___/___|  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/
#
EARTH_R = random.randint(WIDTH // 16, WIDTH // 8)
EARTH_X = random.randint(-WIDTH // 2 + EARTH_R + MARGIN, -EARTH_R)  # Left half of the screen.
EARTH_Y = random.randint(-HEIGHT // 2 + EARTH_R + MARGIN, HEIGHT // 2 - EARTH_R - MARGIN)
MOON_R = int(EARTH_R * 0.2726)  # The moon is just over a quarter of the size of earth.
MOON_X = random.randint(0, WIDTH // 2 - MOON_R - MARGIN)  # Right half of the screen.
MOON_Y = random.randint(-HEIGHT // 2 + MOON_R + MARGIN, HEIGHT // 2 - MOON_R - MARGIN)


def exercise7():
    """Use the screen and turtle defined below to solve the given exercise."""
    #  ___   ___     _  _  ___ _____    __  __  ___  ___ ___ _____   __
    # |   \ / _ \   | \| |/ _ \_   _|  |  \/  |/ _ \|   \_ _| __\ \ / /
    # | |) | (_) |  | .` | (_) || |    | |\/| | (_) | |) | || _| \ V /
    # |___/ \___/   |_|\_|\___/ |_|    |_|  |_|\___/|___/___|_|   |_|
    #  _____ _  _ ___ ___    ___ _   _ _  _  ___ _____ ___ ___  _  _
    # |_   _| || |_ _/ __|  | __| | | | \| |/ __|_   _|_ _/ _ \| \| |
    #   | | | __ || |\__ \  | _|| |_| | .` | (__  | |  | | (_) | .` |
    #   |_| |_||_|___|___/  |_|  \___/|_|\_|\___| |_| |___\___/|_|\_|
    #
    # Create the turtle screen and two turtles (leave this as the first line).
    screen, artist, writer = turtle_setup()

    # Give the user some instructions.
    writer.write("Try to click on the Earth or the Moon...", align="center", font=("Arial", FONT_SIZE, "bold"))

    # Draw a blue dot for the earth and a silver dot for the moon.
    artist.penup()
    artist.color("Blue")
    artist.setposition(EARTH_X, EARTH_Y)
    artist.dot(EARTH_R * 2)
    artist.color("LightGray")
    artist.setposition(MOON_X, MOON_Y)
    artist.dot(MOON_R * 2)

    # Tell the screen to call the click() function when the user clicks on the screen.
    screen.onclick(planet_click)

    # Rather than exitonclick(), enter the main event loop to listen for clicks.
    screen.mainloop()


def planet_click(x, y):
    """Display a Hit or Miss message if the (x,y) coordinate hit the earth or moon drawn in exercise7().

    Note: The "screen.onclick( planet_click )" function call in exercise7() results in
    this function being called automatically when the turtle screen is clicked.

    :param int x: The x-coordinate of the click.
    :param int y: The y-coordinate of the click.
    """
    # TODO 7: Replace True in the line below with a single condition to display the appropriate message.
    # TODO 7: Use the existing definitions of EARTH_X, EARTH_Y, EARTH_R, MOON_X, MOON_Y, and MOON_R.
    #determines areas where moon or earth will be.
    if math.hypot( x - EARTH_X, y - EARTH_Y) < EARTH_R or math.hypot(x - MOON_X, y - MOON_Y) < MOON_R :
        easygui.msgbox("Hit!", "Result")
    else:
        easygui.msgbox("Miss", "Result")


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
