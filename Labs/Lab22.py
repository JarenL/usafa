"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import string


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    exercise0()
    exercise1()
    exercise2()
    exercise3()
    exercise4()


def exercise0():
    """Demonstrate building a dictionary."""
    # TODO 0: Read, discuss, and understand the following code.

    # Lists are created with square brackets and can be thought of as
    # "mapping" an index, also called a "key", to a value.
    color_list = [ "red", "green", "blue", "cyan", "yellow", "magenta" ]
    # Here, the integer 2 is the key and the string "blue" is the value.
    print( color_list[ 2 ], end=" " )

    # Dictionaries are created with curly brackets and also map keys to values.
    color_dict = { 0: "red", 1: "green", 2: "blue", 3: "cyan", 4: "yellow", 5: "magenta" }
    # Again, the integer 2 is the key and the string "blue" is the value.
    print( color_dict[ 2 ], end=" " )

    # The color_dict example illustrates mapping a key to a value, but is not very useful.
    # Consider this example which maps strings to strings.
    house_dict = { "bathroom": "yellow", "bedroom": "cyan", "kitchen": "blue", "yard": "green" }
    # Here, the string "kitchen" is the key and the string "blue" is the value.
    print( house_dict[ "kitchen" ] )

    # Dictionaries can be traversed in several ways; first, by keys.
    for key in house_dict.keys():
        print( key, end=" " )
    print()

    # Also by values:
    for value in house_dict.values():
        print( value, end=" " )
    print()

    # And finally by (key, value) pairs:
    for key, value in house_dict.items():
        print( "{}:{}".format( key, value ), end=" " )
    print()

    # Many familiar operations work with dictionaries:
    print( "len( house_dict ) = {}.".format( len( house_dict ) ) )
    # The min and max operations find the min and max key in the dictionary (not value).
    print( "min( house_dict ) = {}, max( house_dict ) = {}.".format(
        min( house_dict ), max( house_dict ) ) )
    # Similarly, the "in" operator works with the dictionary keys, not values.
    print( "'kitchen' in house_dict = {}, 'blue' in house_dict = {}".format(
        'kitchen' in house_dict, 'blue' in house_dict ) )

    # The get( key ) method works the same as [ key ] if the key is in the dictionary.
    print( "house_dict.get( 'kitchen' ) = {}".format( house_dict.get( 'kitchen' ) ) )
    # However, if the key is not in the dictionary, it returns None (where [ key ] causes an error).
    print( "house_dict.get( 'basement' ) = {}".format( house_dict.get( 'basement' ) ) )
    # The get method also allows specifying a default value if the key is not in the dictionary.
    print( "house_dict.get( 'den', 'white' ) = {}".format( house_dict.get( 'den', 'white' ) ) )

    # Finally, key/value pairs can be added and deleted from a dictionary.
    print( house_dict )
    house_dict[ "garage" ] = "red"
    print( house_dict )
    del house_dict[ 'yard' ]
    print( house_dict )
    print()


def exercise1():
    """Tests the function as described in the lab document."""
    # Test the load_dictionary function with a small dictionary file.
    print( load_dictionary( "./data/House.txt" ) )

    # Test with a few larger dictionary files when the above test works.
    print( load_dictionary( "./data/Pirate.txt" ) )
    print( load_dictionary( "./data/Sms.txt" ) )
    print()


def load_dictionary( filename ):
    """Load a dictionary from the given file.

    Each line in the given file must contain a key/value pair separated by a colon.

    :param str filename: The file name containing a dictionary.
    :return: A dictionary with key/value pairs from the file.
    :rtype: dict[str, str]
    """
    # Start with an empty dictionary.
    d = {}

    # TODO 1: In the space below, complete the function as described in the lab document.
    with open(filename) as data_file:
        data_lines = data_file.read().splitlines()
    for line in data_lines:
        k = line.split(":")[0]
        v = line.split(":")[1]
        d[k] = v
    # Return the entire dictionary.
    return d


def exercise2():
    """Tests the function as described in the lab document."""
    # I don't know right now, ask later okay?
    print( translate( "Idk rn, ask l8r k?", load_dictionary( "./data/Sms.txt" ) ) )
    # Aye, Captain, th' grog be in th' galley.
    print( translate( "Yes, Sir, the rum is in the kitchen.", load_dictionary( "./data/Pirate.txt" ) ) )
    print()


def translate( s, d ):
    """Translates words from the sentence s using the dictionary d.

    Note: Punctuation is stripped from each individual word as it is translated,
    but is retained in the fully translated sentence.

    :param str s: The sentence/string to be translated.
    :param dict[str, str] d: The translation dictionary.
    :return: The translated sentence/string.
    :rtype: str
    """
    # TODO 2: In the space below, complete the function as described in the lab document.
    result = []
    for token in s.split():
        word = token.strip(string.punctuation)
        trans = d.get(word.lower(), word.lower())
        if word.isupper():
            trans = trans.upper()
        elif word[0].isupper():
            trans = trans[0].upper() + trans[1:]
        result.append(token.replace(word, trans))


def exercise3():
    """Tests the function as described in the lab document."""
    # Test the word_count function with a small file.
    print( word_count( "./data/Test.txt" ) )

    # Test with a few larger files when the above test works.
    print( word_count( "./data/Captain.txt" ) )
    print( word_count( "./data/Address.txt" ) )
    print()


def word_count( filename ):
    """Builds a dictionary of word counts in the given file.

    The key/value pairs in the dictionary are string/integer where the string
    is a word in the file and the integer is the number of times the word
    occurs in the file.

    For example, the Test.txt file from the Resources page
    of the course website would produce the following dictionary:
        {'a': 2, 'voice': 1, 'emergency': 1, 'have': 1, 'big': 1, 'is': 2,
        'this': 3, 'would': 1, 'an': 1, 'been': 1, 'only': 1, 'test': 2,
        'you': 1, 'heard': 1, 'actual': 1, 'had': 1}
    Note: The items in a dictionary are unordered, so yours may appear in a different order.

    Note: The words used as keys should be lower-case with no punctuation on the ends
          (though a contraction such as "can't" will have punctuation within the word).

    Note: Do NOT use one of Python's built-in count() methods (either string or list);
          doing so would result in a highly inefficient solution.

    :param str filename: The file name for which the words are to be counted.
    :return: A dictionary of word counts.
    :rtype: dict[str, int]
    """
    # Start with an empty dictionary.
    d = {}

    # TODO 3: In the space below, complete the function as described in the lab document.
    with open(filename) as data_file:
        data_words = data_file.read().split()
    for word in data_words:
        word = word.strip(string.punctuation).lower()
        if word:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    # Return the entire dictionary.
    return d


def exercise4():
    """Uses the specified function as described in the lab document."""
    """Tests the function as described in the lab document."""
    for filename in [ "./data/Test.txt", "./data/Captain.txt", "./data/Address.txt" ]:
        # Get the word count dictionary.
        d = word_count( filename )

        # Print the file name and then show the 8 most common words in the file.
        print( "{}:\n{}".format( filename, "=" * len( filename ) ) )
        show_largest( 8, d )

        # Make sure the dictionary was not changed by show_largest.
        if d != word_count( filename ):
            print( "ERROR: Dictionary changed by show_largest function!" )

        print()


def show_largest( n, d ):
    """Shows the n key/value pairs with the largest values.

    Note: If there is a tie for the nth most common word, arbitrarily choose one.

    Note: The values in the dictionary may be changed while this function executes,
          but the dictionary MUST be returned to its original state upon completion.

    Note: Refer to the following for a simple, concise, "Pythonic" method of finding
    the maximum value in a dictionary:
        http://stackoverflow.com/questions/14091636/get-dict-key-by-max-value

    :param int n: The number of key/value pairs to show.
    :param dict[str, int] d: The dictionary.
    :return: None
    """
    # TODO 4: In the space below, complete the function as described in the lab document.
    n = min(n, len(d))
    for _ in range(n):
        k = max(d, key=d.get)
        print("{}:{}".format(k, d[k]))
        d[k] *= -1
    for k in d:
        d[k] = abs(d[k])


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()