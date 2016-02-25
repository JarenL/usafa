"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: LtCol (Ret) Christman

Documentation: Stuck on how to remove separating punctuation from list items. Read on stackoverflow.com to look into
"map" function. Implemented what I learned and it removed separating punctuation. As seen on Line 173. Stuck on how to
check validity of 3x3 square. Read on stackoverflow.com how to properly nest several For loops within each other to
solve. Seen on line 310. Read on stackoverflow.com how to check list for duplicates using set function. Utilized this
beginning on line 302. LtCol Christman helped me in his office with for loops and resolved a issue I had with
print_sudoku and create_sudoku not working.
"""

import easygui  # For easygui.fileopenbox.
# import os  # For os.path.basename.

# from PEXes.PEX2_Puzzles import PUZZLE, PUZZLE_SOLVED, PUZZLE_INVALID, DATA, DATA_SOLVED

PUZZLE = [[1, 8, 0, 6, 0, 9, 0, 5, 7],
          [5, 0, 0, 0, 0, 0, 0, 0, 3],
          [0, 0, 2, 0, 8, 0, 4, 0, 0],
          [7, 0, 0, 8, 4, 5, 0, 0, 1],
          [0, 0, 3, 2, 0, 1, 9, 0, 0],
          [2, 0, 0, 9, 6, 3, 0, 0, 5],
          [0, 0, 1, 0, 5, 0, 8, 0, 0],
          [8, 0, 0, 0, 0, 0, 0, 0, 4],
          [9, 4, 0, 3, 0, 8, 0, 7, 2]]

PUZZLE_SOLVED = [[1, 8, 4, 6, 3, 9, 2, 5, 7],
                 [5, 9, 7, 1, 2, 4, 6, 8, 3],
                 [6, 3, 2, 5, 8, 7, 4, 1, 9],
                 [7, 6, 9, 8, 4, 5, 3, 2, 1],
                 [4, 5, 3, 2, 7, 1, 9, 6, 8],
                 [2, 1, 8, 9, 6, 3, 7, 4, 5],
                 [3, 7, 1, 4, 5, 2, 8, 9, 6],
                 [8, 2, 5, 7, 9, 6, 1, 3, 4],
                 [9, 4, 6, 3, 1, 8, 5, 7, 2]]

PUZZLE_INVALID = [[1, 8, 0, 6, 3, 9, 0, 5, 7],
                  [5, 0, 0, 0, 0, 0, 0, 0, 3],
                  [0, 0, 2, 0, 8, 0, 4, 0, 0],
                  [7, 0, 0, 8, 4, 5, 0, 0, 1],
                  [0, 0, 3, 2, 3, 1, 9, 0, 0],
                  [2, 0, 0, 9, 6, 3, 0, 0, 5],
                  [0, 0, 1, 0, 5, 0, 8, 0, 0],
                  [8, 0, 0, 0, 0, 0, 0, 0, 4],
                  [9, 4, 0, 3, 0, 8, 0, 7, 2]]

DATA = """1 8 0 6 0 9 0 5 7
          5 0 0 0 0 0 0 0 3
          0 0 2 0 8 0 4 0 0
          7 0 0 8 4 5 0 0 1
          0 0 3 2 0 1 9 0 0
          2 0 0 9 6 3 0 0 5
          0 0 1 0 5 0 8 0 0
          8 0 0 0 0 0 0 0 4
          9 4 0 3 0 8 0 7 2"""

DATA_SOLVED = """1 8 4 6 3 9 2 5 7
                 5 9 7 1 2 4 6 8 3
                 6 3 2 5 8 7 4 1 9
                 7 6 9 8 4 5 3 2 1
                 4 5 3 2 7 1 9 6 8
                 2 1 8 9 6 3 7 4 5
                 3 7 1 4 5 2 8 9 6
                 8 2 5 7 9 6 1 3 4
                 9 4 6 3 1 8 5 7 2"""


def main():
    """Main program to do Sudoku, so here's a Sudoku haiku:

    One through nine in place
    To open the matrix door
    Let logic guide you
    """
    # TODO 1b: Test the str_sudoku function with the given puzzles.
    # print( str_sudoku(PUZZLE))
    # print( str_sudoku( PUZZLE_SOLVED ) )

    # TODO 2b: Test the print_sudoku function with the given puzzles.
    # print_sudoku( PUZZLE )
    # print_sudoku( PUZZLE_SOLVED )

    # TODO 3b: Test the create_sudoku puzzle with the given data.
    # print_sudoku( create_sudoku( DATA ) )
    # print_sudoku( create_sudoku( DATA_SOLVED ) )

    # TODO 4b: Test the open_sudoku function with the given files.
    # print_sudoku( open_sudoku( "./data/Sudoku_Blank.txt" ) )
    # print_sudoku(open_sudoku("./data/Sudoku00.txt"))
    # print_sudoku( open_sudoku( "./data/Sudoku01.txt" ) )
    # print_sudoku( open_sudoku( "./data/Sudoku02.txt" ) )

    # TODO 5b: Test the is_solved function with the given puzzles.
    # print( is_solved( PUZZLE ), is_solved( PUZZLE_SOLVED ) )

    # TODO 6b: Test the is_valid function with the given puzzles.
    # print( is_valid( PUZZLE ), is_valid( PUZZLE_SOLVED ), is_valid( PUZZLE_INVALID ) )

    # TODO 7: Implement the main program as described in the PEX document.
    starting_directory = './Data/*.txt'
    choose = easygui.fileopenbox(title="Choose File", default=starting_directory)
    print_sudoku(open_sudoku(choose))
    if is_valid(open_sudoku(choose)):
        if is_solved(open_sudoku(choose)):
            print("The puzzle IS valid and IS solved.")
        elif not is_solved(open_sudoku(choose)):
            print("The puzzle IS valid and NOT solved.")
    else:
        if not is_solved(open_sudoku(choose)):
            print("The puzzle is NOT valid and is NOT solved.")


# TODO 1a: Implement the str_sudoku function as described in the PEX document.
def str_sudoku(puzzle):
    """Creates a string of puzzle values suitable for printing to a file.

    The string created by this function is formatted such that it could be
    passed to create_sudoku function and recreate the same puzzle.

    Note: This function DOES NOT modify the puzzle.

    :param list[list[int]] puzzle: The Sudoku puzzle as a 9x9 nested list of integers.
    :return: A string suitable for printing to a file or passing to create_sudoku.
    """
    for row in puzzle:
        make_string = " ".join(str(x) for x in row)
        print(make_string)


# TODO 2a: Implement the print_sudoku function as described in the PEX document.
def print_sudoku(puzzle):
    """Prints the nested list structure in pretty rows and columns.

    For example, PEX2_Puzzles.PUZZLE would print as follows:
    +===+===+===+===+===+===+===+===+===+
    # 1 | 8 |   # 6 |   | 9 #   | 5 | 7 #
    +---+---+---+---+---+---+---+---+---+
    # 5 |   |   #   |   |   #   |   | 3 #
    +---+---+---+---+---+---+---+---+---+
    #   |   | 2 #   | 8 |   # 4 |   |   #
    +===+===+===+===+===+===+===+===+===+
    # 7 |   |   # 8 | 4 | 5 #   |   | 1 #
    +---+---+---+---+---+---+---+---+---+
    #   |   | 3 # 2 |   | 1 # 9 |   |   #
    +---+---+---+---+---+---+---+---+---+
    # 2 |   |   # 9 | 6 | 3 #   |   | 5 #
    +===+===+===+===+===+===+===+===+===+
    #   |   | 1 #   | 5 |   # 8 |   |   #
    +---+---+---+---+---+---+---+---+---+
    # 8 |   |   #   |   |   #   |   | 4 #
    +---+---+---+---+---+---+---+---+---+
    # 9 | 4 |   # 3 |   | 8 #   | 7 | 2 #
    +===+===+===+===+===+===+===+===+===+

    Note: This function DOES NOT modify the puzzle.

    :param list[list[int]] puzzle: The Sudoku puzzle as a 9x9 nested list of integers.
    :return: None
    """
    # print(puzzle)
    space = "+===+===+===+===+===+===+===+===+===+"
    space2 = "+---+---+---+---+---+---+---+---+---+"
    separations = ["# ", " | ", " | ", " # ", " | ", " | ", " # ", " | ", " | ", " #"]
    count = 0
    i = 0
    while count <= 18:
        if count == 0 or count == 6 or count == 12 or count == 18:
            print(space)
            count += 1
        elif count == 2 or count == 4 or count == 8 or count == 10 or count == 14 or count == 16:
            print(space2)
            count += 1
        elif count == 1 or count == 3 or count == 5 or count == 7 or count == 9 or count == 11 or count == 13 or count \
                == 15 or count == 17:
            print_only_one_row = True
            while print_only_one_row:
                combine_lists = []
                # Puts the separation between sudoku numbers.
                add_separation = list(zip(separations, puzzle[i]))
                add_separation.append(" #")
                # Makes nested lists into one list. Also replaces "0" with blank - " ".
                for y in add_separation:
                    for x in y:
                        if str(x) == "0":
                            x = " "
                        combine_lists.append(x)
                print("".join(map(str, combine_lists)))
                # Sets to false so only one row prints at a time.
                print_only_one_row = False
                count += 1
                i += 1


# TODO 3a: Implement the create_sudoku function as described in the PEX document.
def create_sudoku(data):
    """Creates a 9x9 nested list of integers from a string with 81 separate values.

    :param str data: A string with 81 separate integer values, [0-9].
    :return: The Sudoku puzzle as a 9x9 nested list of integers.
    :rtype: list[list[int]]
    """

    sudoku_list = []
    data_list = data.split()
    row = []
    for value in data_list:
        row.append(int(value))
        if len(row) == 9:
            sudoku_list.append(row)
            row = []
    return sudoku_list


# TODO 4a: Implement the open_sudoku function as described in the PEX document.
def open_sudoku(filename):
    """Opens the given file, parses the contents, and returns a Sudoku puzzle.

    This function prints to the console any comment lines in the file.

    :param str filename: The file name.
    :return: The Sudoku puzzle as a 9x9 nested list of integers.
    :rtype: list[list[int]]
    """
    # takes list
    with open(filename) as data_file:
        data_string = data_file.read().split()
    number_list = []
    for value in data_string:
        if value.isnumeric():
            number_list.append(value)

    return create_sudoku(" ".join(number_list))


# TODO 5a: Implement the is_solved function as described in the PEX document.
def is_solved(puzzle):
    """Determines if a Sudoku puzzle is valid and complete.

    Note: This function DOES NOT modify the puzzle.

    :param list[list[int]] puzzle: The Sudoku puzzle as a 9x9 nested list of integers.
    :return: True if the puzzle is valid and complete; False otherwise.
    """
    row_good = 0
    col_good = 0
    square_good = 0
    col_list = []
    square_list = []
    i = 0
    if len(puzzle) == 9:
        # Checks the rows for proper length and validity.
        for row in puzzle:
            if len(row) == 9 and sorted(row) == sorted(list(range(1, 10))):
                row_good += 1
        # Checks the columns in puzzle for valdiity.
        for col in range(9):
            col = []
            for row in range(9):
                col.append(puzzle[row][i])
                if len(col) == 9 and sorted(col) == sorted(list(range(1, 10))):
                    col_good += 1
                elif len(col) == 9:
                    col_list.append(col)
                    i += 1
                    col = []
        # Checks the 3x3 squares in puzzle for validity.
        for row in range(3):
            for col in range(3):
                three_three = []
                for row2 in range(3):
                    for col2 in range(3):
                        three_three.append(puzzle[3 * row + row2][3 * col + col2])
                square_list.append(three_three)
        for row in square_list:
            if sorted(row) == sorted(list(range(1, 10))):
                square_good += 1
        if square_good and col_good and row_good == 9:
            return True
        else:
            return False
    else:
        return False


# TODO 6a: Implement the is_valid function as described in the PEX document.
def is_valid(puzzle):
    """Determines if a Sudoku puzzle is valid, but not necessarily complete.

    Note: This function DOES NOT modify the puzzle.

    :param list[list[int]] puzzle: The Sudoku puzzle as a 9x9 nested list of integers.
    :return: True if the puzzle is valid; False otherwise.
    """
    # The variables with "good" in them are used to track number of row/column/square that are valid.
    # Used structure from "is_solved" for this function with some changes. Does not work properly. Unsure how to code
    # for valdiity. Function currently checks for repeated numbers, but sinze zero is valid and came be repeated fails.
    # Not sure how to check for validity.
    row_good = 0
    col_good = 0
    square_good = 0
    col_list = []
    square_list = []
    i = 0
    if len(puzzle) == 9:
        # Checks the rows for proper length and validity.
        for row in puzzle:
            if len(row) == 9 and len(row) == len(set(row)):
                row_good += 1
        # Checks the columns in puzzle for valdiity.
        for col in range(9):
            col = []
            for row in range(9):
                col.append(puzzle[row][i])
                if len(col) == 9 and len(col) == len(set(col)):
                    col_good += 1
                elif len(col) == 9:
                    col_list.append(col)
                    i += 1
                    col = []
        # Checks the 3x3 squares in puzzle for validity.
        for row in range(3):
            for col in range(3):
                three_three = []
                for row2 in range(3):
                    for col2 in range(3):
                        three_three.append(puzzle[3 * row + row2][3 * col + col2])
                square_list.append(three_three)
        for row in square_list:
            if len(row) == len(set(row)):
                square_good += 1
        if square_good and col_good and row_good == 9:
            return True
        else:
            return False
    else:
        return False


# TODO 8: Implement the solve_sudoku function as discussed in class (lesson 20 and/or 21).
def solve_sudoku(puzzle, cell=0, value=1):
    """Recursive function to solve a Sudoku puzzle with brute force.

    Note: This function DOES modify the puzzle!!!

    :param list[list[int]] puzzle:  The 9x9 nested list of integers.
    :return: None
    """
    row = cell // 9
    col = cell % 9
    if not is_solved(puzzle) and is_valid(puzzle) and cell <= 80 and value <= 9:
        if puzzle[row][col] == 0:
            solve_sudoku(puzzle, cell + 1, 1)
            if not is_solved(puzzle):
                # Remove the value and try the next value in the same cell.
                puzzle[row][col] = 0
                solve_sudoku(puzzle, cell, value + 1)
            else:
                # Cell already has a value, so move on to the next cell.
                solve_sudoku(puzzle, cell + 1, 1)


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
