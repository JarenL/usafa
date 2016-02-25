"""CS 210, Introduction to Programming, Fall 2015, _YOUR_NAME_HERE_.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: _YOUR_DETAILED_DOCUMENTATION_STATEMENT_HERE_.
"""

# These are sample import statements; delete them if they are not used (also delete this comment).
import math                     # This imports the entire module.
from string import punctuation  # This only imports the specified item from the module.


def main():
    """Main program to demonstrate the import statements and string formatting."""

    # The following code is for demonstration only; delete if not used.

    # When the entire module is imported, the dot notation is used to access individual items.
    print( math.pi )

    # Example string formatting; for reference see https://mkaz.com/2012/10/10/python-string-format/
    print( "{:.4f}".format( math.pi ) )

    # When an individual item is imported, it can be used without the dot notation.
    print( punctuation )


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
