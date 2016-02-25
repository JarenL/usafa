"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""


def main():
    """Main program to demonstrate/test various recursive functions."""

    # Testing the factorial() function.
    print( "Factorial of 5 =", factorial( 5 ) )
    print( "Factorial of 5 =", factorial_verbose( 5 ) )
    print()

    # Testing the fibonacci() function.
    print( "The {}st Fibonacci number is {}.".format( 1, fibonacci( 1 ) ) )
    print( "The {}th Fibonacci number is {}.".format( 8, fibonacci( 8 ) ) )
    print( "The {}th Fibonacci number is {}.".format( 13, fibonacci( 13 ) ) )
    print()

    # Testing the gcd() function.
    print( "gcd:", gcd( 42, 28 ), gcd( 63, 84 ), gcd( 14, 21 ) )
    print( "gcd:", gcd( 19, 51 ), gcd( 51, 19 ) )
    print()

    # Testing the list_sum() function and first/rest helper functions.
    a_list = [ 37, 83, 42, 51, 99, 13, 29, 67 ]
    print( "a_list = {}".format( a_list ) )
    print( "first = {}, rest = {}".format( first( a_list ), rest( a_list ) ) )
    print( "Sum of a_list = {}".format( list_sum( a_list ) ) )
    print( "Sum of a_list = {}".format( list_sum_verbose( a_list ) ) )
    print()

    # Testing the list_contains() function.
    for value in [ 42, 13, 37, 67, 50, 19 ]:
        print( "{} contains {}: {}".format( a_list, value, list_contains( value, a_list ) ) )
    print()

    # Testing the list_count() function using a list of characters.
    s = "This is a test. This is only a test."
    char_list = list( s.lower() )
    for char in [ 'e', 't', 'z' ]:
        print( "'{}' contains {} {} times.".format( s, char, list_count( char, char_list ) ) )
    print()

    # Testing the list_merge() function. These tests also start with strings,
    # use the list() function to create a list of individual characters,
    # and then the string join() function to show the result as a string.
    print( "".join( list_merge( list( "aeiou" ), list( "cfmsw" ) ) ) )
    print( "".join( list_merge( list( "abcghimnostuyz" ), list( "defjklpqrvwx" ) ) ) )
    print( "".join( list_merge( list( "abcd" ), list( "wxyz" ) ) ) )
    print( "".join( list_merge( list( "wxyz" ), list( "abcd" ) ) ) )
    print()

    # A list of strings, some palindromes, some not.
    palindromes = [ "Go hang a salami; I'm a lasagna hog.", "Able was I ere I saw Elba.",
                    "Madam, I'm Adam.", "Madam in Eden, I'm Adam", "Never odd or even",
                    "Lee has a race car as a heel.", "No sir! Away! A papaya war is on!",
                    "Stressed? No tips? Spit on desserts.", "Mr. Owl ate my metal worm.",
                    "Flee to me, remote Elf!", "So many Dynamos!", "1001001", "Huh?",
                    "This is not a palindrome.", "Neither is this." ]

    # Testing the is_palindrome() function.
    for p in palindromes:
        print( "The string '{}' {} a palindrome.".format( p, "IS" if is_palindrome( p ) else "is NOT" ) )
    print()

    # My favorite binary tree:
    #         42
    #     25      75
    #   13  37  67  88
    # My favorite tree stored as nested lists.
    a_tree = [ 42, [ 25, [ 13, [], [] ],
                         [ 37, [], [] ] ],
                   [ 75, [ 67, [], [] ],
                         [ 88, [], [] ] ] ]

    # Print an in-order traversal of a binary tree.
    in_order( a_tree )
    print()


def factorial( n ):
    """Recursively calculates the factorial of a given number.

    :param int n: A non-negative integer value.
    :return: The factorial of n.
    :rtype: int
    """
    # TODO 0: Read, discuss, and understand the following code.
    if n <= 1:
        return 1
    else:
        return n * factorial( n - 1 )


def factorial_verbose( n ):
    """Recursively calculates the factorial of a given number while also printing trace information.

    :param int n: A non-negative integer value.
    :return: The factorial of n.
    :rtype: int
    """
    # TODO 0: Read, discuss, and understand the following code.
    print( "n = {}:".format( n ), end=" " )
    if n <= 1:
        print( "returning 1." )
        return 1
    else:
        print( "calculating result = {} * factorial( {} )".format( n, n-1 ) )
        result = n * factorial_verbose( n - 1 )
        print( "n = {}: returning {}".format( n, result ) )
        return result


def fibonacci( n ):
    """Recursively determines the nth Fibonacci number.

    :param int n: A non-negative integer value.
    :return: The nth Fibonacci number.
    :rtype: int
    """
    # TODO 1: Remove the line below and complete the function as described in the lab document.
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd( m, n ):
    """Recursively calculates the greatest common divisor of the given values.
    :param int m: A non-negative integer value.
    :param int n: A positive integer value.
    :return: The greatest common divisor of m and n.
    :rtype: int
    """
    # TODO 2: Remove the line below and complete the function as described in the lab document.
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def first( a_list ):
    """Returns the first item in a list.

    :param list[int] a_list: The non-empty list of which the first item is desired.
    :return: The first item in the list.
    :rtype: int
    """
    return a_list[ 0 ]


def rest( a_list ):
    """Returns a list containing all items in a list except the first.
    :param list[int] a_list: The non-empty list of which the rest is desired.
    :return: A list containing all items from a_list except the first.
    :rtype: list[int]
    """
    return a_list[ 1: ]


def list_sum( a_list ):
    """Recursively calculate and return the sum of a list of integers.

    :param list[int] a_list: The list of integers whose sum is to be calculated.
    :return: The sum of the numbers in the list.
    :rtype: int
    """
    # TODO 3: Read, discuss, and understand the following code.
    if not a_list:
        return 0
    else:
        return first( a_list ) + list_sum( rest( a_list ) )


def list_sum_verbose( num_list ):
    """Recursively calculate and return the sum of a list of integers while also printing trace information.

    :param list[int] a_list: the list of integers whose sum is to be calculated.
    :return: The sum of the numbers in the list.
    :rtype: int
    """
    # TODO 3: Read, discuss, and understand the following code.
    print( "num_list = {}:".format( num_list ), end=" " )
    if not num_list:
        print( "returning 0." )
        return 0
    else:
        print( "calculating result = {} + list_sum( {} )".format( first( num_list ), rest( num_list ) ) )
        result = first( num_list ) + list_sum_verbose( rest( num_list ) )
        print( "num_list = {}: returning {}".format( num_list, result ) )
        return result


def list_contains( item, a_list ):
    """Recursively determines if the given item is in the given list.

    :param item: An item to be searched for in the given list.
    :param a_list: The list of items to be searched.
    :return: True if the item is in the list; False otherwise.
    :rtype: bool
    """
    # The recursive algorithm to determine list membership is:
    # If the list is empty,
    # then the item is not in the list.
    # If the list is not empty and the item equals the first item in the list,
    # then the item is in the list.
    # If the list is not empty and the item does not equal the first item in the list,
    # the the item is in the list if it is in the rest of the list.

    # TODO 4a: Remove the line below and complete the function as described in the lab document.
    if not a_list:
        return False
    elif item == first(a_list):
        return True
    else:
        return list_contains(item, rest(a_list))


def list_count( item, a_list ):
    """Recursively determines how many times the given item occurs in the given list.

    :param item: An item to be searched for in the given list.
    :param a_list: The list of items to be searched.
    :return: The number of times the item occurs in the list.
    :rtype: int
    """
    # The recursive algorithm to count item occurrences in a list is:
    # If the list is empty,
    # then the item occurs in the list zero times.
    # If the list is not empty and the item equals the first item in the list,
    # then the item occurs one plus the number of times in occurs in the rest of the list.
    # If the list is not empty and the item does not equal the first item in the list,
    # then the item occurs the number of times it occurs in the rest of the list.

    # TODO 4b: Remove the line below and complete the function as described in the lab document.
    if not a_list:
        return 0
    elif item == first(a_list):
        return list_count(item, rest(a_list)) + 1
    else:
        return list_count(item, rest(a_list))


def list_merge( a_list, b_list ):
    """Recursively merges the two sorted lists into one list.

    Both parameters must be lists sorted in ascending order.

    :param a_list: A sorted list to be merged.
    :param b_list: A sorted list to be merged.
    :return: A new list with the sorted contents of both a_list and b_list.
    """
    # The recursive algorithm to merge two sorted lists is:
    # If the first list is empty,
    # then the result is the second list.
    # If the second list is empty,
    # then the result is the first list.
    # If the first item in the first list is less than the first item in the second list,
    # then the result is a list containing the first item from the first list concatenated
    # with a the result of merging the rest of the first list with the second list.
    # If the first item in the second list is less than the first item in the first list,
    # then the result is a list containing the first item from the second list concatenated
    # with a the result of merging the rest of the second list with the first list.

    # TODO 4c: Remove the line below and complete the function as described in the lab document.
    if not a_list:
        return b_list
    elif not b_list:
        return a_list
    elif first(a_list) < first(b_list):
        return [ first(a_list)] + list_merge(rest(a_list), b_list)
    else:
        return [ first(b_list)] + list_merge(a_list, rest(b_list))


def is_palindrome( s ):
    """Recursively determines if the given string is a palindrome.

    :param str s: The string to be tested for palindrome-ness.
    :return: True if the given string is a palindrome; False otherwise.
    :rtype: bool
    """
    # TODO 5: Remove the line below and complete the function as described in the lab document.
    if len(s) <= 1:
        return True
    elif not s[0].isalnum():
        return is_palindrome(s[1:])
    elif not s[-1].isalnum():
        return is_palindrome(s[:1])
    elif s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    else:
        return False
def in_order( tree ):
    """Prints an in-order traversal of the given tree, represented as nested lists.

    The parameter must be a properly formed nested list representing a binary tree.

    :param tree: A nested list representing a binary tree.
    :return: None
    """
    # Use the links in the reading to find and implement the appropriate algorithm.

    # TODO Challenge: Remove the line below and complete the function as described in the lab document.
    if tree:
        in_order(tree[1])
        print(tree[0], end=" ")
        in_order(tree[2])

# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()