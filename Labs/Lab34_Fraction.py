"""CS 210, Introduction to Programming, Fall 2015, Dr. Bower.

This module contains a ProperFraction class that inherits from the previous lesson's Fraction.

Documentation: None.
"""

# TODO: Modify this import statement as necessary for your own project structure.
from Labs.Lab33 import Fraction

def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # A Fraction object with numerator larger than denominator is unnatural to read when printed.
    f = Fraction( 7, 2 )
    print( "f = {}".format( f ) )

    # A ProperFraction object prints in a much nicer format.
    f = ProperFraction( 7, 2 )
    print( "f = {}".format( f ) )

    # The above example is not surprising since both Fraction and ProperFraction implement __str__.
    # However, the beauty of inheritance is that ProperFraction can do anything a Fraction can do!
    f += ProperFraction( 5, 4 )
    print( "f = {}".format( f ) )


class ProperFraction( Fraction ):
    """Class for representing a proper fraction in the form '3 1/2'."""

    def __str__( self ):
        """Build and return a string representation of the object.

        :return: A string representation of this Fraction in the format "w n/d".
        :rtype: str
        """
        if self.n < self.d:
            return "{}/{}".format( self.n, self.d )
        else:
            return "{} {}/{}".format( self.n // self.d, self.n % self.d, self.d )


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()