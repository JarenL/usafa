"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""


def main():
    """Main program to test solutions for each exercise."""
    # Print the docstring at the top of the file so your instructor can see your name.
    print( __doc__ )

    # TODO 2b: In the space below, use the class as described in the lab document.
    with open("./data/Kindle.txt") as data_file:
        data_lines = data_file.read().splitlines()
    books = []
    for lie in data_lines:
        data = line.split("|")
        books.append(Book(data[0], data[1], int(data[2]), int(data[3])))
    for book in books:
        print(book)
    print()
    books.sort(key=Book.progress)
    print("\n".join([str(book) for book in books]))
    print()


# TODO 2a: In the space below this comment, write the class as described in the lab document.

class Book:
    """

    """
    def __init__(self, title= "Untitled", author="Unknown", pages=0, page=0):
        """

        :param title:
        :param author:
        :param pages:
        :param page:
        :return:
        """
        self.title= title
        self.author= author
        self.total_pages = pages
        self.current_page = page
    def __str__(self):
        """

        :return:
        """
        return "{}, by {}\n{}{}".format(self.title, self.author, "=" * self.progress(), "-" * (100 - self.progress()))
    def progress(self):
        return int(100 * self.current_page // self.total_pages)
# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()