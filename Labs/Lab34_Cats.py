"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

A hierarchy of Cat classes to demonstrate inheritance.

Documentation: http://www.youtube.com/watch?v=KJFp272w9u8
=========================================================
"""


def main():
    """"Main program to run demonstration."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    cats = [ Cat( "Felix" ), Lion( "Mufasa" ), Cub( "Simba" ), Cheetah( "Chester" ), Cartoon( "Sylvester" ),
             Tiger( "Tony") ]

    for cat in cats:
        print( cat )

    for cat in cats:
        try:
            print( "{} sings {}!".format( cat.name, cat.sing() ) )
        except AttributeError:
            print( "{} can't sing.".format( cat.name ) )


class Cat( object ):
    """Class to represent a cat with a name that can move and make noise."""

    def __init__( self, name ):
        """Create a new cat with the given name.

        :param str name: The cat's name.
        """
        self.name = name

    def __str__( self ):
        """Build and return a string with this cat's information.

        :return: A string representation of this Cat object.
        :rtype: str
        """
        # Accessing the class name with self.__class__.__name__
        # is usually a bad idea, but is handy for this demo.
        return "I am {} the {}, watch me {}, hear me {}!".format(
            self.name, self.__class__.__name__, self.move(), self.make_noise() )

    # All cats purr, right?
    def make_noise( self ):
        """Return a string indicating the noise this cat makes."""
        return "purr"

    # And all cats definitely saunter.
    def move( self ):
        """Return a string indicating how this cat moves."""
        # define: saunter - Walk in a slow, relaxed manner, without hurry or effort.
        return "saunter"


class Lion( Cat ):
    """Class to represent a Lion and demonstrate inheritance."""

    # Lions roar more often than the purr, so re-define make_noise.
    def make_noise( self ):
        """Return a string indicating the noise this cat makes."""
        return "roar"

    # Lions can run, but they usually saunter so inherit move from Cat.


class Cub( Lion ):
    """Class to represent a baby lion Cub and demonstrate inheritance."""

    # Cubs roar as well, so inherit make_noise from Lion.
    # Don't believe me?  https://www.youtube.com/watch?v=ee7WKxzpY7E

    # Cubs are playful, so they romp rather than saunter.
    def move( self ):
        """Return a string indicating how this cat moves."""
        return "romp"

    # In addition to making noise and moving, a Cub sings.
    def sing( self ):
        """Sing!"""
        return "hakuna matata"


class Cheetah( Cat ):
    """Class to represent a Cheetah and demonstrate inheritance."""

    # Cheetahs don't roar, but they do purr, so inherit make_noise from Cat.

    # https://en.wikipedia.org/wiki/Cheetah#Speed_and_acceleration
    def move( self ):
        """Return a string indicating how this cat moves."""
        return "sprint"


class Cartoon( Cat ):
    """Class to represent a Cartoon cat and demonstrate inheritance."""

    # https://www.youtube.com/watch?v=PkhPuH8G5Hg
    def make_noise( self ):
        """Return a string indicating the noise this cat makes."""
        return "sufferin' succotash!"

    # Cartoon cats also mostly saunter, so inherit move from Cat.

class Eat( Cat ):
    def meat(self):
        return "Eats meat"

class Tiger( Cat ):
    def walks(self):
        return "It walks"
    def noise( self ):
        return "They're great!"

class Siberian( Tiger):
    def lives(self):
        return "In the snow"
    def build(self):
        return "Builds snow man"
# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()