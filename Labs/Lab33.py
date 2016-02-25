"""CS 210, Introduction to Programming, Fall 2015, Dr. Bower.

This module contains a simple Fraction class to be used to
demonstrate the property() function and @property decorator.
See https://docs.python.org/3/library/functions.html#property

Documentation: None.
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    f = Fraction( 1, 8 )
    for _ in range( 8 ):
        print( "{} = {:.3f}".format( f, float( f ) ) )
        f.n += 1

    print()

    f = Fraction( 1, 2 )
    for _ in range( 8 ):
        print( "{} = {:.3f}".format( f, float( f ) ) )
        f.d += 1


class Fraction:
    """Class for representing a fraction with integer values for numerator and denominator."""

    def __init__( self, n=0, d=1 ):
        """Create a new Fraction with the given values.

        :param int n: The numerator.
        :param int d: The denominator.
        """
        self.n = n
        self.d = d

    def __str__( self ):
        """Build and return a string representation of the object.

        :return: A string representation of this Raindrop in the format "(x,y):r".
        :rtype: str
        """
        return "{}/{}".format( self.n, self.d )

    def __int__( self ):
        """Calculates and returns the integer value of this Fraction object.

        :return: The integer value of this Fraction object.
        :rtype: int
        """
        return self.n // self.d

    def __float__( self ):
        """Calculates and returns the float value of this Fraction object.

        :return: The float value of this Fraction object.
        :rtype: float
        """
        return self.n / self.d

    def __add__( self, other ):
        """Adds two Fraction objects, building and returning a new Fraction object.

        Note: This method does NOT modify the self or other Fraction objects.

        Note: This method ensures the result Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object to be added to this Fraction object.
        :return: A new Fraction object equal to the sum of the self and other Fraction objects.
        :rtype: Fraction
        """
        n1 = self.n * other.d
        n2 = self.d * other.n
        d = self.d * other.d
        result = Fraction( n1 + n2, d )
        result.simplify()
        return result

    def __iadd__( self, other ):
        """Adds two Fraction objects, modifying the self Fraction object.

        Note: This method does NOT modify the other Fraction object.

        Note: This method ensures the Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object to be added to this Fraction object.
        :return: A new Fraction object equal to the sum of the self and other Fraction objects.
        :rtype: Fraction
        """
        self.n *= other.d
        self.n += self.d * other.n
        self.d *= other.d
        self.simplify()
        return self

    def __sub__( self, other ):
        """Subtracts two Fraction objects, building and returning a new Fraction object.

        Note: This method does NOT modify the self or other Fraction objects.

        Note: This method ensures the result Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object to be subtracted from this Fraction object.
        :return: A new Fraction object equal to the difference between the self and other Fraction objects.
        :rtype: Fraction
        """
        n1 = self.n * other.d
        n2 = self.d * other.n
        d = self.d * other.d
        result = Fraction( n1 - n2, d )
        result.simplify()
        return result

    def __isub__( self, other ):
        """Subtracts two Fraction objects, modifying the self Fraction object.

        Note: This method does NOT modify the other Fraction object.

        Note: This method ensures the Fraction object is in lowest terms after the addition.

        :param Fraction other: The other Fraction object to be subtracted from this Fraction object.
        :return: A new Fraction object equal to the difference between the self and other Fraction objects.
        :rtype: Fraction
        """
        self.n *= other.d
        self.n -= self.d * other.n
        self.d *= other.d
        self.simplify()
        return self

    def __mul__( self, other ):
        """Multiplies two Fraction objects, building and returning a new Fraction object.

        Note: This method does NOT modify the self or other Fraction objects.

        Note: This method ensures the result Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to multiply this Fraction object.
        :return: A new Fraction object equal to the product of the self and other Fraction objects.
        :rtype: Fraction
        """
        result = Fraction( self.n * other.n, self.d * other.d )
        result.simplify()
        return result

    def __imul__( self, other ):
        """Multiplies two Fraction objects, modifying the self Fraction object.

        Note: This method does NOT modify the other Fraction object.

        Note: This method ensures the Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to multiply this Fraction object.
        :return: A new Fraction object equal to the product of the self and other Fraction objects.
        :rtype: Fraction
        """
        self.n *= other.n
        self.d *= other.d
        self.simplify()
        return self

    def __truediv__( self, other ):
        """Divides two Fraction objects, building and returning a new Fraction object.

        Note: This method does NOT modify the self or other Fraction objects.

        Note: This method ensures the result Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to divide this Fraction object.
        :return: A new Fraction object equal to the division of the self by the other Fraction objects.
        :rtype: Fraction
        """
        result = Fraction( self.n * other.d, self.d * other.n )
        result.simplify()
        return result

    def __itruediv__( self, other ):
        """Divides two Fraction objects, modifying the self Fraction object.

        Note: This method does NOT modify the other Fraction object.

        Note: This method ensures the Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to divide this Fraction object.
        :return: A new Fraction object equal to the division of the self by the other Fraction objects.
        :rtype: Fraction
        """
        self.n *= other.d
        self.d *= other.n
        self.simplify()
        return self

    def __floordiv__( self, other ):
        """Divides two Fraction objects, building and returning a new Fraction object.

        Note: This method does NOT modify the self or other Fraction objects.

        Note: This method ensures the result Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to divide this Fraction object.
        :return: A new Fraction object equal to the division of the self by the other Fraction objects.
        :rtype: Fraction
        """
        result = Fraction( self.n * other.d // self.d * other.n, 1 )
        return result

    def __ifloordiv__( self, other ):
        """Divides two Fraction objects, modifying the self Fraction object.

        Note: This method does NOT modify the other Fraction object.

        Note: This method ensures the Fraction object is in lowest terms.

        :param Fraction other: The other Fraction object by which to divide this Fraction object.
        :return: A new Fraction object equal to the division of the self by the other Fraction objects.
        :rtype: Fraction
        """
        self.n = self.n * other.d // self.d * other.n
        self.d = 1
        return self

    def __eq__( self, other ):
        """Implements the == operator; the fractions 2/3 and 4/6 are mathematically equal.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is equal to the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d == self.d * other.n

    def __ne__( self, other ):
        """Implements the != operator.

        Note: The fractions 2/3 and 4/6 are mathematically equal.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is not equal to the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d != self.d * other.n

    def __lt__( self, other ):
        """Implements the < operator.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is less than the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d < self.d * other.n

    def __le__( self, other ):
        """Implements the <= operator.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is less than or equal to the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d <= self.d * other.n

    def __gt__( self, other ):
        """Implements the > operator.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is greater than the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d > self.d * other.n

    def __ge__( self, other ):
        """Implements the >= operator.

        :param Fraction other: The other Fraction object to be compared to this Fraction object.
        :return: True if this Fraction is greater than or equal to the other Fraction; False otherwise.
        :rtype: bool
        """
        return self.n * other.d >= self.d * other.n

    def simplify( self ):
        """Simplifies this Fraction object such that it is in lowest terms."""
        # Find the greatest common divisor of this Fraction object's numerator and denominator.
        divisor = gcd( self.n, self.d )
        # Simplify this Fraction object's numerator and denominator.
        self.n //= divisor
        self.d //= divisor

    def get denominator(self):
    @property
    def d(self):
        """ Returns the current value of the denominator.
        :return: The denominator.
        :rtype: int
        """
        return self._d
    def set_denominator(self, d):
    @d.setter
    def d(self, d):
        d = int(d)

        if d == 0:
            raise ZeroDivisionError( "Denominator cannot be zero.")
        if d > 0:
            self._d = d
        else:
            self._n *= -1
            self._d = -d

def gcd( a, b ):
    """Uses division-based version of Euclid's algorithm to calculate the greatest common divisor of two integers.

    https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations

    :param int a: An integer.
    :param int b: An integer.
    :return: The greatest common divisor of a and b.
    :rtype: int
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()