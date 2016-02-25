"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import easygui
import random
import string

#from Labs.Lab16_Lists import rand_list


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    exercise1()
    exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()


def exercise1():
    """Uses the specified function as described in the lab document."""
    # Test both the rand_matrix and print_matrix functions.
    # print_matrix( [ [ 37, 84, 42, 51 ], [ 99, 13, 67, 75 ], [ 29, 32, 16, 64 ] ] )
    # print()
    # Once print_matrix works with the above list, un-comment the lines below to test rand_matrix.
    print_matrix( rand_matrix( 4, 5, 10, 99 ) )
    print()
    print_matrix( rand_matrix( 6, 8, 0, 999 ) )
    print()
    print(rand_matrix(3, 4, 10, 99))

def rand_matrix( rows, columns, lower_bound, upper_bound ):
    """Build and return a matrix of random values.

    For example, given the parameters ( 3, 4, 10, 99 ), the function might
    build and return the following nested list structure:
      [ [ 37, 84, 42, 51 ], [ 99, 13, 67, 75 ], [ 29, 32, 16, 64 ] ]

    :param int rows: How many rows to include in the matrix.
    :param int columns: How many columns to include in the matrix.
    :param int lower_bound: The lower bound of the random values, inclusive.
    :param int upper_bound: The upper bound of the random values, inclusive.
    :return: A matrix with the indicated number of rows and columns.
    :rtype: list[list[int]]
    """
    # TODO 1a: Remove the line below and complete the function as described in the lab document.
    matrix = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(random.randint(lower_bound, upper_bound))
        matrix.append(row)
    return matrix


def print_matrix( matrix ):
    """Prints a matrix with values right-justified in 8-character columns.

    For example, the following nested list structure:
      [ [ 37, 84, 42, 51 ], [ 99, 13, 67, 75 ], [ 29, 32, 16, 64 ] ]
    would be printed as:
      37      84      42      51
      99      13      67      75
      29      32      16      64

    :param list[list[int]] matrix: The matrix to be printed.
    :return: None
    """
    # TODO 1b: Remove the line below and complete the function as described in the lab document.
    for x in matrix:
        print(*x, sep="       ")

def exercise2():
    """Uses the specified function as described in the lab document."""
    # TODO 2b: Write code to use the function as described in the lab document.
    m1 = rand_matrix(3,4,10,99)
    m2 = rand_matrix(3,4,10,99)
    print_matrix(m1)
    print("  +")
    print_matrix(m2)
    print(" =====================")
    print_matrix(add_matrices(m1,m2))
    print()


def add_matrices( a, b ):
    """Adds two matrices together.

    http://www.mathsisfun.com/algebra/matrix-introduction.html

    Note: This function does NOT change either of the original matrices!

    :param list[list[int]] a: Matrix to be added.
    :param list[list[int]] b: Matrix to be added.
    :return: The sum of the two matrices.
    :rtype: list[list[int]]
    """
    # TODO 2a: Remove the line below and complete the function as described in the lab document.
    result = []
    for r in range(len(a)):
        row = []
        for c in range( len(a[r])):
            row.append(a[r][c] + b[r][c])
        result.append(row)
    return result




def exercise3():
    """Uses the specified function as described in the lab document."""
    # TODO 3b: Write code to use the function as described in the lab document.
    squares = [ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ]

    for square in squares:
        print_matrix(square)
        print("The above matrix {} a magic square.".format("IS" if is_magic(square) else "is NOT"))
        print("The above matrix {} a magic square.".format("IS" if is_magic_v2(square) else "is NOT"))
        print()
    attempts = 0
    square = squares[-1]
    while attempts < 1000 and not is_magic(square):
        square = rand_matrix(3,3,1,9)
        attempts += 1

    print_matrix( square )
    print("The above matrix {} a magic square.".format("IS" if is_magic(square) else "is NOT"))
    print()
def is_magic( square ):
    """Determines if a matrix of integer values is a magic square.

    A matrix is a magic square if its row and column dimensions are equal and odd
    and the sum of all rows, columns, and diagonals through the center are equal.
    For example, the following matrix is a magic square:
        [ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ].

    Note: This function does NOT change the original matrix!

    :param list[list[int]] square: The matrix to be tested for magic.
    :return: True if the matrix is a magic square; False otherwise.
    """
    # TODO 3a: Remove the line below and complete the function as described in the lab document.
    return True


def exercise4():
    """Uses the specified function as described in the lab document."""
    # One simple hard-coded test; write more tests using rand_list.
    print( list_str( [ 37, 84, 42, 51, 99, 13, 67, 75, 29 ] ) )

    # TODO 4b: Write code to use the function as described in the lab document.


def list_str( data ):
    """Applies the str() function to every item in a list and return a string of all items separated by spaces.

    Note: This function is to be accomplished in one line with a list comprehension!

    :param list[int] data: The list of data.
    :return: A space delimited string of all items in the list.
    :rtype: str
    """
    # TODO 4a: Remove the line below and complete the function as described in the lab document.
    return ""


def exercise5():
    """Uses the specified function as described in the lab document."""
    # One simple hard-coded test; write more tests using rand_list.
    print( sum_multiples( [ 37, 84, 42, 51, 99, 13, 67, 75, 29 ], 21 ) )

    # TODO 5b: Write code to use the function as described in the lab document.
    for _ in range(3):
        r_list = rand_list(8,0,999)
        print(list_str(r_list), "...", sum_multiples(r_list, 10))
    print()

def sum_multiples( data, divisor ):
    """Calculates and returns the sum of all values in a list of integers that are evenly divisible by divisor.

    Note: This function is to be accomplished in one line with a list comprehension!

    :param list[int] data: The list of data.
    :param int divisor: The divisor.
    :return: The sum of all values in the list evenly divisible by divisor.
    :rtype: int
    """
    # TODO 5a: Remove the line below and complete the function as described in the lab document.
    return sum([value for value in data if value % divisor == 0])


def exercise6():
    """Uses the specified function as described in the lab document."""
    # TODO 6b: Write code to use the function as described in the lab document.
    s = easygui.enterbox( "Enter a string (Cancel to quit):", "Acronym - Input", "Three Letter Acronym" )  # TLA
    while s is not None:
        easygui.msgbox( acronym( s ), "Acronym - Result" )
        s = easygui.enterbox( "Enter a string (Cancel to quit):", "Acronym - Input",
                              "Integrity first, Service before self, Excellence in all we do." )  # IFSBSEA


def acronym( s ):
    """Creates and returns an acronym from the first letter of every word in s longer than two characters.

    Note: This function is to be accomplished in one line with a list comprehension!

    :param str s: The string to be acronym-ed.
    :return: The acronym built from the string.
    :rtype: str
    """
    # TODO 6a: Remove the line below and complete the function as described in the lab document.
    return "".join([word[0] for word in s.upper().split() if len(word.strip(string.punctuation)) > 2 ]


# Multiply matrix
def exercise7():
    """Uses the specified function as described in the lab document."""
    # TODO 7b: Write code to use the function as described in the lab document.
    pass  # Remove the pass statement (and this comment) when writing your own code.


def multiply_matrices( left, right ):
    """Adds two matrices together.

    http://www.mathsisfun.com/algebra/matrix-multiplying.html

    :param list[list[int]] left: Matrix to be added.
    :param list[list[int]] right: Matrix to be added.
    :return: The sum of the two matrices.
    :rtype: list[list[int]]
    """
    # TODO 7a: Remove the line below and complete the function as described in the lab document.
    return []


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()