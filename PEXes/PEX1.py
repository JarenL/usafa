"""CS 210, Introduction to Programming, Fall 2015, C3C Jaren D. Lynch.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: Lt. Col Christman explained to me how return in fucntions works, as I was having trouble returning my
player_score values out of the roll_dice function.. Explained to me how to return my values. Seen on line 157 in  the
roll_die function. I read on stackoverflow.com how to draw dots with turtle, used in draw_die function starting on line
210. How to erase what a turtle has drawn with turtle.clear(), starting on line 125. How easygui.boolbox can be used to
represent either a 1 or 0, starting on line 49. The coursebook illustrated how to utilize "screenexitonclick()" which
I used to close the window at the end of the program. I looked on wikipedia.org to find out more information on how pig
is played. This helped me understand what I was doing for the project. The lab guidance pdf had in it ways to draw
the pips based on the number of the roll. I implemented this in my draw_die function and was how I determined the
position of the pips. Starting on line 210.
"""

import easygui
import random
import turtle

# Define several useful constants to be used by the Turtle graphics.
WIDTH = 960  # Usually 720, 960, 1024, 1280, 1600, or 1920.
HEIGHT = WIDTH * 9 / 16  # Produces the eye-pleasing 16:9 HD aspect ratio.
MARGIN = 32  # Somewhat arbitrary value, but it looks nice.
FONT_SIZE = 16  # Somewhat arbitrary value, but it looks nice.
DRAW_FAST = True  # Set to True for fast, stealthy turtles.
DICE_SIZE = (WIDTH - MARGIN * 9) / 8
START_X = WIDTH / 2 - MARGIN
START_Y = HEIGHT / 2 - MARGIN
SPACE2 = DICE_SIZE + MARGIN
ROLL = random.randint(1, 7)
HOW_MANY_COLUMN = int(WIDTH / (DICE_SIZE + MARGIN))


def main():
    """
    :return: No return
    """
    """Main program to _INSERT_BRIEF_DESCRIPTION_HERE_."""
    # Create the turtle screen and two turtles (leave this as the first line of main).
    screen, artist, writer = turtle_setup()

    # TODO: Implement your main program here.
    begin = easygui.boolbox("Do you want to play pig?", "Choose:", ["YES", "NO WAY"])
    player_score1 = 0
    player_score2 = 0
    if begin:
        player1 = easygui.enterbox("Player 1's name?")
        player2 = easygui.enterbox("Player 2's name?")
        begin_player = easygui.boolbox("Who's starting?", "Choose:", [player1, player2])
        ready_check = easygui.choicebox("Ready " + begin_player + "?", "Choose:", ["YES", "WHOOPS"])
        if ready_check == "Yes":
            roll_die(writer, player1, player2, player_score1, player_score2)
            if player_score1 >= 100:
                easygui.msgbox(player1 + " won!")
            elif player_score2 >= 100:
                easygui.msgbox(player2 + " won!")
        else:
            easygui.msgbox("Click Green to exit! Goodbye!")
            screen.exitonclick()
    else:
        easygui.msgbox("Click Green to exit! Goodbye!")
        screen.exitonclick()
    # Wait for the user to click before closing the window (leave this as the last line of main).


# TODO: Implement your roll_die function here.


def roll_die(turtle1, player1, player2, player_score1, player_score2):
    """

    :param turtle1: Drawer for this function. In this case writer is inputted.
    :param player1: First player.
    :param player2: Second Player.
    :param player_score1: Score of player 1.
    :param player_score2: Score of player 2.
    :return: Returns player_score1 and player_score2 and pos_count to be used for score keeping and die position.
    """
    screen, artist, writer = turtle_setup()
    # Used "shoot" as a way to move back and forth between the players.
    shoot = 1
    artist.hideturtle()
    writer.hideturtle()
    pos_count = 0
    turtle1.setposition(0, HEIGHT // 2 - FONT_SIZE * 2)
    # Loops until a player reaches the max of 100
    while player_score1 < 100 and player_score2 < 100:
        while shoot == 1 and player_score1 < 100:
            roll = random.randint(1, 6)
            choice = easygui.boolbox("Roll or Hold?", "Choose:", ["ROLL", "HOLD"])
            writer.reset()
            turtle1.setpos(-DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
            if choice:
                if roll == 1:
                    easygui.msgbox(str(player1) + " busted. Next Player.")
                    shoot = 0
                    artist.reset()
                    player_score1 = 0
                    pos_count = 0
                    turtle1.clear()
                    turtle1.write(str(player1) + ": " + str(player_score1), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                    turtle1.setpos(DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
                    turtle1.write(str(player2) + ": " + str(player_score2), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                else:
                    draw_die(artist, roll, START_X, START_Y, pos_count)
                    player_score1 += roll
                    pos_count += 1
                    turtle1.clear()
                    turtle1.write(str(player1) + ": " + str(player_score1), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                    turtle1.setpos(DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
                    turtle1.write(str(player2) + ": " + str(player_score2), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
            else:
                shoot = 0
                artist.reset()
                turtle1.setposition(0, HEIGHT // 2 - FONT_SIZE * 2)
                pos_count = 0
        while shoot == 0 and player_score2 < 100:
            roll2 = random.randint(1, 6)
            choice = easygui.boolbox("Roll or Hold?", "Choose:", ["ROLL", "HOLD"])
            writer.reset()
            turtle1.setpos(-DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
            if choice:
                if roll2 == 1:
                    easygui.msgbox(str(player2) + " busted. Next Player.")
                    shoot = 1
                    artist.reset()
                    player_score2 = 0
                    pos_count = 0
                    turtle1.clear()
                    turtle1.write(str(player1) + ": " + str(player_score1), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                    turtle1.setpos(DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
                    turtle1.write(str(player2) + ": " + str(player_score2), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                else:
                    draw_die(artist, roll2, START_X, START_Y, pos_count)
                    player_score2 += roll2
                    pos_count += 1
                    turtle1.clear()
                    turtle1.write(str(player1) + ": " + str(player_score1), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
                    turtle1.setpos(DICE_SIZE, HEIGHT // 2 - FONT_SIZE * 2)
                    turtle1.write(str(player2) + ": " + str(player_score2), align="Center", font=("Arial", FONT_SIZE,
                                                                                                  "bold"))
            else:
                shoot = 1
                artist.reset()
                turtle1.setposition(0, HEIGHT // 2 - FONT_SIZE * 2)
                pos_count = 0
    if player_score1 >= 100:
        easygui.msgbox(player1 + " won! Click Green to Exit")
        screen.exitonclick()
    elif player_score2 >= 100:
        easygui.msgbox(player2 + " won! Click Green to Exit")
        screen.exitonclick()
    return player_score1, player_score2, pos_count

# TODO: Implement your draw_die function here.


def draw_die(turtle2, number_of_pips, x, y, pos_mod):
    """

    :param turtle2: Whether drawer will be artist or writer. For this function it will be artist.
    :param number_of_pips: Takes result of "roll" to determine number of pips on dice to be drawn.
    :param x: Starting x position
    :param y: Starting y position
    :param pos_mod: Keeps a count of a players dice rolls so next dice drawn will be beside it and not on top.
    :return: No return.
    """
    turtle2.penup()
    x_pos = x
    y_pos = y
    # moves the next dice drawn to be beside first one. I'm not sure if this will work if the width or height
    #  is changed or how to solve for that change.
    if pos_mod < HOW_MANY_COLUMN:
        x_pos -= SPACE2 * pos_mod
        y_pos = y
        turtle2.setpos(x_pos, y_pos)
    # Starts second row of die.
    elif pos_mod >= HOW_MANY_COLUMN:
        y_pos = START_Y - SPACE2
        x_pos -= SPACE2 * (pos_mod - HOW_MANY_COLUMN)
        turtle2.setpos(x_pos, y_pos)
        # Starts Third row of die.
        if pos_mod >= HOW_MANY_COLUMN * 2:
            y_pos = START_Y - (SPACE2 * 2)
            x_pos -= SPACE2 * (pos_mod - HOW_MANY_COLUMN * 2)
            turtle2.setpos(x_pos, y_pos)
            # Starts Fourth row of die.
            if pos_mod >= HOW_MANY_COLUMN * 3:
                y_pos = START_Y - (SPACE2 * 3)
                x_pos -= SPACE2 * (pos_mod - HOW_MANY_COLUMN * 3)
                turtle2.setpos(x_pos, y_pos)
                # Starts Fifth row of die.
                if pos_mod >= HOW_MANY_COLUMN * 4:
                    y_pos = START_Y - (SPACE2 * 4)
                    x_pos -= SPACE2 * (pos_mod - HOW_MANY_COLUMN * 4)
                    turtle2.setpos(x_pos, y_pos)
    # Makes die red filled.
    turtle2.fillcolor("Red")
    turtle2.begin_fill()
    turtle2.pendown()
    for side in range(0, 4):
        turtle2.right(90)
        turtle2.forward(DICE_SIZE)
    turtle2.end_fill()
    turtle2.penup()
    # Odd pips have pip in center.
    if number_of_pips % 2 != 0:
        turtle2.setpos(x_pos - DICE_SIZE / 2, y_pos - DICE_SIZE / 2)
        turtle2.dot(DICE_SIZE / 5)
    # Pips greater than one, have pip in top left and bottom right.
    if number_of_pips > 1:
        turtle2.setpos(x_pos - DICE_SIZE * (7 / 8), y_pos - DICE_SIZE * (1 / 8))
        turtle2.dot(DICE_SIZE / 5)
        turtle2.setpos(x_pos - DICE_SIZE * (1 / 8), y_pos - DICE_SIZE * (7 / 8))
        turtle2.dot(DICE_SIZE / 5)
    # Pips greater than 3 have pips in bottom left and top right.
    if number_of_pips > 3:
        turtle2.setpos(x_pos - DICE_SIZE * (1 / 8), y_pos - DICE_SIZE * (1 / 8))
        turtle2.dot(DICE_SIZE / 5)
        turtle2.setpos(x_pos - DICE_SIZE * (7 / 8), y_pos - DICE_SIZE * (7 / 8))
        turtle2.dot(DICE_SIZE / 5)
    # Six pips have pips in the center horizontal.
    if number_of_pips == 6:
        turtle2.setpos(x_pos - DICE_SIZE * (1 / 8), y_pos - DICE_SIZE / 2)
        turtle2.dot(DICE_SIZE / 5)
        turtle2.setpos(x_pos - DICE_SIZE * (7 / 8), y_pos - DICE_SIZE / 2)
        turtle2.dot(DICE_SIZE / 5)


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
    screen.bgcolor("Green")

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
