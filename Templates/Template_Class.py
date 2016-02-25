"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: _YOUR_DETAILED_DOCUMENTATION_STATEMENT_HERE_.
"""

from datetime import date


def main():
    """Main program to create several Person objects and display them."""

    # Create three Person objects.
    a = Person( "Lance", "Peter", "Sijan", 1942 )
    b = Person( "Hoyt", "Sanford", "Vandenberg", 1899 )
    c = Person( "Muir", "Stephen", "Fairchild", 1894 )

    # Display the objects as strings (Python automatically calls the __str__ method).
    print( a, b, c, sep='\n' )


class Person( object ):
    """This class represents a Person with First, Middle, and Last names and an age."""

    def __init__( self, first, middle, last, birth_year ):
        """Initialize a new Person object with the given attribute values.

        :param str first: The person's first name.
        :param str middle: The person's middle name.
        :param str last:  The person's last name.
        :param int birth_year: The year the person was born.
        """
        self.first = first
        """:type: str"""
        self.middle = middle
        """:type: str"""
        self.last = last
        """:type: str"""
        self.age = date.today().year - birth_year  # Not completely accurate.
        """:type: int"""

    def __str__( self ):
        """Returns a string representation of the object."""
        return "{}, {} {}., Age: {}".format( self.last, self.first, self.middle[ 0 ], self.age )


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
