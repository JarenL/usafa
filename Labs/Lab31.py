"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise0()
    # exercise1()
    exercise2()
    # exercise3()
    # exercise4()
    # exercise5()


def exercise0():
    """Obtain user input, convert to integer, and display results."""
    # TODO 0: Read, discuss, and understand the following code.

    # Obtain user input as a string.
    s = input( "Enter the answer, which must be an integer: " )
    # Convert the user input to an integer.
    answer = int( s )
    # Display the results. What could go wrong?
    print( "The answer is {}.".format( answer ) )


def exercise1():
    """Demonstrate a basic try/except statement."""
    # TODO 1: Read, discuss, and understand the following code.

    # Obtain user input as a string.
    s = input( "Enter the answer, which must be an integer: " )

    try:
        # Convert the user input to an integer.
        answer = int( s )

    except ValueError:
        # If there is an exception, do this instead.
        answer = 42

    print( "The answer is {}.".format( answer ) )


def exercise2():
    """Demonstrate the full try/except statement."""
    # TODO 2: Read, discuss, and understand the following code.

    try:
        # If any of the next three lines raises an exception,
        # the program will jump directly to the except clause.
        total = int( input( "Enter sum of all scores: " ) )
        count = int( input( "Enter number of scores:  " ) )
        avg = total / count

        # If any of the above lines raise an exception,
        # this line of codes does not execute.
        print( "{} / {} = {}".format( total, count, avg ) )

    except ValueError:
        print( "Integer values only!" )

    except ZeroDivisionError:
        print( "Zero? Really?!" )

    except:
        print( "Something bad happened." )

    else:
        print( "Only happens if NO exceptions are raised." )

    finally:
        print( "Always happens after the code in the try block, no matter what." )


def exercise3():
    """Input validation is a common use of the try/except statement."""
    # TODO 3: Read, discuss, and understand the following code.

    # Initial, unused values to make PyCharm happy. Remove this line to see the warning below.
    a = b = c = 0

    # Loop until the valid_input flag is set to True.
    valid_input = False
    while not valid_input:
        try:
            s = input( "Enter three integers, separated by spaces: " )
            data = s.split()
            a = int( data[ 0 ] )
            b = int( data[ 1 ] )
            c = int( data[ 2 ] )

        except ( ValueError, IndexError ):
            print( "Invalid input; please try again." )

        else:
            # The code reaches this point if no exceptions were raised.
            valid_input = True

    # When the code gets to here, a, b, and c are valid integers.
    if a ** 2 + b ** 2 == c ** 2:
        print( "{}, {}, and {} form a right triangle.".format( a, b, c ) )
    else:
        print( "{}, {}, and {} do not form a right triangle.".format( a, b, c ) )


def exercise4():
    """Demonstrates raising an error or exception."""
    # TODO 4: Read, discuss, and understand the following code.

    try:
        # Calculating the average of an empty list raises an exception.
        # What other exceptions could be raised by the average function?
        print( average( [] ) )

    except RuntimeError as e:
        print( "ERROR: {}".format( e ) )


def average( data ):
    """Calculates and returns the average of a list of numeric values.

    :param list data: The list of numeric values to be averaged.
    :raises RuntimeError: If the list of numeric values is empty.
    :return: The average of the list of numeric values.
    :rtype: float
    """
    if len( data ) == 0:
        raise RuntimeError( "No values to average." )

    # If the above code raises an exception, this code does not execute.
    return sum( data ) / len( data )


def exercise5():
    """Uses the specified function as described in the lab document."""
    # TODO 5: Read, discuss, and understand the following code.

    try:
        p = Person( "Douglas Adams", 42 )
        print( p )

        p = Person( "Yoda", 900 )
        print( p )

    except ValueError as e:
        print( "ERROR: {}".format( e ) )


class Person:
    """A class to represent a person."""

    def __init__( self, name, age ):
        """Create the Person object.

        :param str name: The person's name.
        :param int age: The person's age.
        :raises ValueError: If the age is invalid.
        """
        self.name = name

        if age < 0:
            # Barring time travel, a negative age does not make sense.
            raise ValueError( "Age must be positive." )
        elif age <= 125:
            # Between 0 and 125 seems more or less reasonable.
            self.age = age
        else:
            # https://en.wikipedia.org/wiki/Oldest_people
            raise ValueError( "Age must be reasonable." )

    def __str__( self ):
        """Build and return a string representation of the person."""
        return "{} is {} years old.".format( self.name, self.age )


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()