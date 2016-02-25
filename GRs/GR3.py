"""CS 210, Introduction to Programming, Fall 2015, Jaren Lynch.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: No help received; this GR is entirely individual effort.
=======================================================================
"""

import easygui
import math

""" The following code segments are provided for your reference.
    You are free to copy/paste them into your answers below.

    # An easygui message box to display a formatted string.
    easygui.msgbox( "pi = {:.2f}".format( 22 / 7 ), "Result" )

    # An easygui enter box for entering a string.
    s = easygui.enterbox( "Enter a string:", "Input" )

    # An easygui integer box for entering a positive integer.
    n = easygui.integerbox( "Enter a positive integer:", "Input", "", 1, 2 ** 31 )

    # Get a file name from the user with an easygui File Open Dialog.
    filename = easygui.fileopenbox( default="./data/*.txt" )

    # Read the entire contents of filename into a single string.
    with open( filename ) as data_file:
        data_string = data_file.read()

    # Read the entire contents of filename into a list of strings, one per word.
    with open( filename ) as data_file:
        data_words = data_file.read().split()

    # Read the entire contents of filename into a list of strings, one per line.
    with open( filename ) as data_file:
        data_lines = data_file.read().splitlines()
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print(__doc__)

    # Call each individual exercise; comment/un-comment these lines as you work.
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem5()
    # problem6()
    # problem7()
    # problem8()


def problem1():
    """Uses the specified function as described in the exam document."""
    # TODO 1b: Write code to use the function as described in the exam document.
    def longest_words(filename):
        with open(filename) as data_file:
            data_lines = data_file.read().splitlines()
        for word in data_lines:
            word_list = word.split(" ")
            for thing in word_list:
                greatest = 0
                gimme = 0
                if len(thing) >= greatest:
                    greatest = len(thing)
                    gimme = thing
            print(thing)

        # TODO 1a: In the space below, write the function as described in the exam document.

    longest_words(filename="./data/Test.txt")
    longest_words(easygui.fileopenbox(default="./data/*.txt"))


def problem2():
    """Uses the specified function as described in the exam document."""
    # TODO 2b: Write code to use the function as described in the exam document.
    def inches_to_yards(inches):
        yards = inches / 36.0
        return yards

    # TODO 2a: In the space below, write the function as described in the exam document.
    print("Inches    Yards")
    print("======   =======")
    for inch in range(30, 480, 30):
        print("  ", end="")
        print("{:3d}".format(inch), end="")
        if inch >= 360:
            print("    ", end="")
            print("{:.4f}".format(inches_to_yards(inch)))
        else:
            print("     ", end="")
            print("{:.4f}".format(inches_to_yards(inch)))


def problem3():
    """Uses the specified function as described in the exam document."""
    # TODO 3b: Write code to use the function as described in the exam document.
    def min_within(the_list, int1, int2):
        use = sorted(the_list)
        minimum = 100000
        if int1 < 0:
            int1 = 0
        elif int2 > len(use):
            int2 = len(use)
        for num in the_list[int(int1):int(int2) + 1]:
            if num <= minimum:
                minimum = num
        return minimum

    # TODO 3a: In the space below, write the function as described in the exam document.
    test1 = [23, 67, 15, 23, 18, 42, 14, 89]
    test2 = [11, 42, 78, 24, 13, 85, 27]
    test3 = [22, 58, 12, 10]
    test4 = [42, 17, 86, 29, 33]
    print(min_within(test1, 3, 5))
    print(min_within(test2, 1, 4))
    print(min_within(test3, -2, 2))
    print(min_within(test4, 2, 6))


def problem4():
    """Uses the specified function as described in the exam document."""
    # TODO 4b: Write code to use the function as described in the exam document.
    def rev_str(the_string):
        count = -1
        new = []
        for letter in the_string:
            new.append(the_string[count])
            count -= 1
        news = " ".join(new)
        return news

    # TODO 4a: In the space below, write the function as described in the exam document.
    print(rev_str("USAFA"))
    print(rev_str("CS 210"))
    print(rev_str("race car"))
    enter = rev_str(easygui.enterbox("Enter String"))
    easygui.msgbox(enter)


def problem5():
    """Uses the specified function as described in the exam document."""
    # TODO 5b: Write code to use the function as described in the exam document.
    def build_board(int1, str1, str2):
        board = []
        count = 0
        for num in range(int1):
            board.append([])
            for rw in board:
                if count == 0:
                    rw.append(str1)
                else:
                    rw.append(str2)
                    count = 0
                rw.append("-")

        return board

    # TODO 5a: In the space below, write the function as described in the exam document.
    print(build_board(8, "X", "Y"))


def problem6():
    """Uses the specified function as described in the exam document."""
    # TODO 6b: Write code to use the function as described in the exam document.
    def find_perfect(number):
        perfects = []
        perfect = 0
        for num in range(1, number, 1):
            for numb in range(1, num, 1):
                if num % numb == 0:
                    perfects.append(num)
        return perfects

    # TODO 6a: In the space below, write the function as described in the exam document.
    print(find_perfect(20))


def problem7():
    """Uses the specified class as described in the exam document."""
    # TODO 7b: Write code to use the class as described in the exam document.



    # TODO 7a: In the space below, write the class as described in the exam document.
    class Alarm:
        def __init__(self, int1, int2):
            minutes = 0
            hours = 0
            if int1 > 23:
                hours = int1 - 24
            elif int2 > 59:
                hours += 1
                minutes = int2 - minutes

        def __str__(self):
            return

        def snooze(self, add_minutest):
            pass


def problem8():
    """Uses the specified classes as described in the exam document."""
    # TODO 8b: Write code to use the classes as described in the exam document.



    # TODO 8a: In the space below, write the classes as described in the exam document.
    class Container:
        def __init__(self, contents):
            super(Container, self).__init__()

        def __str__(self):
            super(Container, self).__str__(Box, Cylinder, Sphere)

        def __lt__(self, container):
            super(Container, self).__lt__(Box, Cylinder, Sphere)


    class Box:
        def __init__(self, contents, width, height, depth):
            self.contents = "wine"
            self.width = 13
            self.height = 14
            self.depth = 15
            self.volume = self.width * self.height * self.depth

    class Cylinder:
        def __init__(self, contents, radius, height):
            self.contents = "milk"
            self.radius = 8
            self.height = 12
            self.volume = math.pi * self.height * self.radius ** 2

    class Sphere:
        def __init__(self, contents, radius):
            self.contents = "milk"
            self.radius = 10
            self.volume = (4 / 3) * math.pi * self.radius ** 3


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
