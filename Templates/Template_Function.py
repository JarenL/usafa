"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: _YOUR_DETAILED_DOCUMENTATION_STATEMENT_HERE_.
"""


def main():
    """Main program to get user input, call the function, and display the results."""

    # Get user input.
    the_string = input( "Enter a string: " )
    how_many = int( input( "Enter how many: " ) )

    # Call the function with the given parameters, saving the result.
    result = repeat_string( the_string, how_many )

    # Display the results.
    print( "{} repeated {} times is {}.".format( the_string, how_many, result ) )


def repeat_string( s, n ):
    """Builds and returns a new string that is a copy of the given string repeated n times.

    The operands to the binary multiplication operator can be a string and an integer
    with the result being the string repeated the indicated number of times. However,
    if the integer value is not positive, the result will be an empty string.

    :param str s: The string to be repeated.
    :param int n: The number of times to repeat the string.
    :return: The string s repeated n times.
    :rtype: str
    """
    # Note this function returns the new string; it does not print it.
    return s * n


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
