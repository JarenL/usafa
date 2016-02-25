"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

import easygui


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # Call each individual exercise; comment/un-comment these lines as you work.
    # exercise0()
    # exercise1()
    # exercise2()
    # exercise3()
    exercise4()


def exercise0():
    """Demonstrate various methods of reading the contents of a data file."""
    # In the folder containing this Python program is a data folder with the file Test.txt.
    filename = "./data/Test.txt"

    # Example 1: Read the entire contents of a file into a single string.
    with open( filename ) as data_file:
        data_string = data_file.read()
    # Un-indent after reading the file so the with construct will close the file.
    print( "Example 1:", data_string, sep="\n" )

    # Example 2: Read the entire contents of a file into a list of strings, one per word.
    with open( filename ) as data_file:
        data_words = data_file.read().split()
    print( "Example 2:", data_words, sep="\n" )

    # Example 3: Read the entire contents of a file into a list of strings, one per line.
    with open( filename ) as data_file:
        data_lines = data_file.read().splitlines()
    print( "Example 3:", data_lines, sep="\n" )

    # Example 4: Uses file open dialog to select a txt file from the data folder.
    # filename = easygui.fileopenbox( default="./data/*.txt" )
    # with open( filename ) as data_file:
    #     data_string = data_file.read()
    #
    # # The data_string can be split into words and lines _without_re-reading_ the file:
    # data_words = data_string.split()
    # data_lines = data_string.splitlines()
    # print( "Example 4:", data_string, data_words, data_lines, sep="\n" )


def exercise1():
    """Reads an entire file into a string, then estimates the number of words per sentence."""
    # TODO 1b: Write code to use the count_char function as described in the lab document.
    file = easygui.fileopenbox( default="./data/*.txt")
    with open( file ) as data_file:
        data_string = data_file.read()
    # Counts up the number of sentence enders in the string.
    sentences = count_char( ".", data_string) + count_char( "?", data_string) + count_char( "!", data_string)
    # Splits string by white space in between words.
    words = len(data_string.split())
    # Displays words per sentence in string, then displays the amount of words per sentence.
    easygui.msgbox( "{} / {} = {:.2f} words per sentence.". format( words, sentences, words / sentences))

# TODO 1a: In the space below, write the count_char function as described in the lab document.
def count_char(letter, sentence):
    """
    :param letter: The value being sought.
    :param sentence: The string being searched through.
    :return: Number of times sought value is in the larger string.
    """
    letter_count = 0
    for char in sentence:
        if char.lower() == letter:
            letter_count += 1
    return letter_count

def exercise2():
    """Reads a data file of Python keywords, then counts how many appear in a Python source file."""
    # TODO 2b: Write code to use the count_words function as described in the lab document.

    with open( "./data/Keywords.txt" ) as data_file:
        word_string1 = data_file.read().split()

    compare_file = easygui.fileopenbox( default="./data/*.txt")
    with open( compare_file ) as data_file:
        word_string2 = data_file.read().split()

    # Counts up the number of sentence enders in the string.
    match_count = count_words( word_string1, word_string2 )
    percent = match_count / len(compare_file) * 100
    # Displays words per sentence in string, then displays the amount of words per sentence.
    easygui.msgbox( "The first file and the second file share {} words. {:.2f}%". format( match_count, percent),
                    "Comparison")

# TODO 2a: In the space below, write the count_words function as described in the lab document.
def count_words(list1, list2):
    """

    :param list1: First list.
    :param list2: What the first list's words are compared to.
    :return:
    """
    match_count = 0
    for word in list2:
        if word in list1:
            match_count += 1
    return match_count





def exercise3():
    """Display file information until the user clicks Cancel."""
    # TODO 3b: Write code to use the file_info function as described in the lab document.
    file = easygui.fileopenbox( default="./data/*.txt")
    with open( file ) as data_file:
        count_file = file_info(data_file.read())
    easygui.msgbox( "{}". format( count_file ))

# TODO 3a: In the space below, write the file_info function as described in the lab document.

def file_info(file_name):
    """

    :param file_name: File being entered to be counted.
    :return: Print statement of counted lines, words, and characters.
    """
    num_words = len(file_name.split())
    num_char = len(file_name)
    num_lines = -1
    for line in file_name.split("\n"):
        num_lines += 1
    form = "Line: " + str(num_lines) + " " + "Words: " + " " + str(num_words) + " " + "Characters: " + str(num_char)
    return form

def exercise4():
    """Display files with line numbers until the user clicks Cancel."""
    # TODO 4b: Write code to use the print_file function as described in the lab document.
    file_name = easygui.fileopenbox( default="./data/*.txt")
    while len(file_name) > 1:
        print_file( file_name )
        file_name = easygui.fileopenbox( default="./data/*.txt" )


# TODO 4a: In the space below, write the print_file function as described in the lab document.
def print_file(file_name):
    """

    :param file_name:  The file to be printed
    :return: Nothing returned.
    """
    with open( file_name ) as data_file:
        data_lines = data_file.read().splitlines()

    line_number = 0
    for line in data_lines:
        line_number += 1
        print( "{} : {}".format(line_number, line))

# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()