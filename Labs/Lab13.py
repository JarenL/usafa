"""CS 210, Introduction to Programming, Fall 2015, Jaren Lynch.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import Labs.cImage as image
import easygui
import os


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise0()
    # exercise1()
    exercise2()


def exercise0():
    """Test the print_table function."""
    # Print one hard-coded multiplication table.
    print_table( 1, 10 )

    # Un-comment the code below to test different size multiplication tables.
    # start = easygui.integerbox( "Enter start value for the multiplication table:", "Input", "", 0, 2 ** 31 )
    # stop = easygui.integerbox( "Enter stop value for the multiplication table:", "Input", "", 0, 2 ** 31 )
    # while start is not None and stop is not None:  # Continue until the user clicks the Cancel button.
    #     print_table( start, stop )
    #     start = easygui.integerbox( "Enter start value for the multiplication table:", "Input", "", 0, 2 ** 31 )
    #     stop = easygui.integerbox( "Enter stop value for the multiplication table:", "Input", "", 0, 2 ** 31 )


def print_table( start, stop ):
    """Prints a multiplication table with each axis having values in the range [start,stop].

    Sample table output with start=1 and stop=10:

               1     2     3     4     5     6     7     8     9    10
          ------------------------------------------------------------
       1 |     1     2     3     4     5     6     7     8     9    10
       2 |     2     4     6     8    10    12    14    16    18    20
       3 |     3     6     9    12    15    18    21    24    27    30
       4 |     4     8    12    16    20    24    28    32    36    40
       5 |     5    10    15    20    25    30    35    40    45    50
       6 |     6    12    18    24    30    36    42    48    54    60
       7 |     7    14    21    28    35    42    49    56    63    70
       8 |     8    16    24    32    40    48    56    64    72    80
       9 |     9    18    27    36    45    54    63    72    81    90
      10 |    10    20    30    40    50    60    70    80    90   100

    :param start: The starting value for each axis of the multiplication table.
    :param stop: The stopping value for each axis of the multiplication table.
    :return: None
    """
    # TODO 0: Read, discuss, and understand the following code.
    # Print the header row, starting with six spaces in the blank upper-left corner of the table.
    print( "      ", end="" )  # End this print with an empty string rather than the default newline.
    for column in range( start, stop + 1 ):  # Range includes both start and stop.
        print( "{:6d}".format( column ), end="" )  # End with an empty string rather than a newline.
    print()  # Print a newline after the entire header row has been printed.

    # Underline the header row, starting with six spaces in the blank upper-left corner of the table.
    print( "      ", end="" )  # End this print with an empty string rather than the default newline.
    for column in range( start, stop + 1 ):  # Range includes both start and stop.
        print( " -----", end="" )  # End with an empty string rather than a newline.
    print()  # Print a newline after the entire header row has been underlined.

    # Print the table.
    for row in range( start, stop + 1 ):  # Range includes both start and stop.
        # Print the row header (the number right-justified at the beginning of the line).
        print( "{:4d}".format( row ), end=" |" )  # End with the vertical separator; no newline.

        # Print the multiplication values for the column in the row.
        for column in range( start, stop + 1 ):  # Range includes both start and stop.
            print( "{:6d}".format( row * column ), end="" )  # End with empty string; no newline.

        # Print a newline after the entire row has been printed.
        print()

    # Print a blank line after the entire table, ensuring any buffered output is flushed.
    print( flush=True )


def exercise1():
    """Test the print_bar_chart function."""
    # Print one hard-coded bar chart.
    print_bar_chart( [ 42, 25, 75, 13, 37, 67, 88 ] )

    # Un-comment the code below to test multiple bar charts.
    # data = easygui.enterbox( "Enter a series of numbers separated by spaces:", "Input" )
    # while data is not None:  # Continue until the user clicks the Cancel button.
    #     print_bar_chart( data.split() )
    #     data = easygui.enterbox( "Enter a series of numbers separated by spaces:", "Input" )


def print_bar_chart( data ):
    """Prints a bar chart with the given list of values.

    Sample bar chart with data [ 42, 25, 75, 13, 37, 67, 88 ]:

      42 | ******************************************
      25 | *************************
      75 | ***************************************************************************
      13 | *************
      37 | *************************************
      67 | *******************************************************************
      88 | ****************************************************************************************

    Note: Apply the int() function to each value in the list.

    :param list data: The list of values in the bar chart.
    :return: None
    """
    # TODO 1: Implement the nested loops as described in the lab document.
    for num in data:
        print( str(num) + " | " + (int(num) * "*") )


def exercise2():
    """Test the image manipulation functions."""
    # Get a gif image file from the user (extract the base file name for use as window title).
    filename = easygui.fileopenbox( default="./data/*.gif" )
    basename = os.path.basename( filename )

    # Load the image, create a window with the appropriate dimensions, and show the image.
    img = image.Image( filename )
    window = image.ImageWin( basename, img.getWidth(), img.getHeight() )
    img.draw( window )

    # Set the window cursor to the standard busy/wait cursor as image manipulations can take a while.
    window.config( cursor="watch" )

    # Perform an image manipulation (un-comment one of the following three lines).
    new_img = negative_image( img )
    # new_img = grayscale_image( img )
    # new_img = sepia_tone_image( img )

    # Draw the resulting image.
    new_img.draw( window )

    # Set the window cursor back to the default and wait for a click to close.
    window.config( cursor="" )
    window.exitonclick()


def negative_image( old_img ):
    """Creates and returns a negative image based on the given image.

    :param image.Image old_img: The old image from which to make a negated image.
    :return: The new image, which is a negated version of the old image.
    :rtype: image.Image
    """
    # TODO 2a: Read, discuss, and understand the following code.
    # Create an empty image and then set each pixel based on the old image.
    new_img = image.EmptyImage( old_img.getWidth(), old_img.getHeight() )

    # Use nested loops to visit every (x,y) coordinate (as opposed to (col,row) as the author does).
    for x in range( old_img.getWidth() ):
        for y in range( old_img.getHeight() ):
            # Get the old pixel and red, green, blue values.
            old_pixel = old_img.getPixel( x, y )
            old_r = old_pixel.getRed()
            old_g = old_pixel.getGreen()
            old_b = old_pixel.getBlue()
            # Calculate the new red, green, and blue values and create a new pixel.
            new_r = 255 - old_r
            new_g = 255 - old_g
            new_b = 255 - old_b
            new_pixel = image.Pixel( new_r, new_g, new_b )
            # Set the pixel in the new image.
            new_img.setPixel( x, y, new_pixel )

    return new_img


def grayscale_image( old_img ):
    """Creates and returns a grayscale image based on the given image.

    :param image.Image old_img: The old image from which to make a grayscale image.
    :return: The new image, which is a grayscale version of the old image.
    :rtype: image.Image
    """
    # TODO 2b: Implement the grayscale conversion as described in the lab document.
    new_img = image.EmptyImage( old_img.getWidth(), old_img.getHeight())

    for x in range(old_img.getWidth()):
        for y in range(old_img.getHeight()):
            old_pixel = old_img.getPixel(x,y)
            old_r = old_pixel.getRed()
            old_g = old_pixel.getGreen()
            old_b = old_pixel.getBlue()
            intensity = int(0.299 * old_r + 0.587 * old_g + 0.114 * old_b)
            new_pixel = image.Pixel(intensity, intensity, intensity)
            new_img.setPixel(x, y, new_pixel)


def sepia_tone_image( old_img ):
    """Creates and returns a sepia tone image based on the given image.

    :param image.Image old_img: The old image from which to make a sepia tone image.
    :return: The new image, which is a sepia tone version of the old image.
    :rtype: image.Image
    """
    # TODO 2c: Implement the sepia tone conversion as described in the lab document.
    new_img = image.EmptyImage(old_img.getWidth(), old_img.getHeight())
    for x in range(old_img.getWidth()):
        for y in range(old_img.getHeight()):
            old_pixel = old_img.getPixel(x,y)
            old_r = old_pixel.getRed()
            old_g = old_pixel.getGreen()
            old_b = old_pixel.getBlue()
            new_r = int(min(255, old_r * 0.393 + old_g * 0.769 + old_b * 0.189))
            new_g = int(min(255, old_r * 0.349 + old_g * 0.686 + old_b * 0.168))
            new_b = int(min(255, old_r * 0.272 + old_g * 0.534 + old_b * 0.131))
            new_pixel = image.Pixel(new_r, new_g, new_b)
            new_img.setPixel(x, y, new_pixel)
    return new_img

# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()