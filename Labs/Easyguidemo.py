"""CS 210, Introduction to Programming, Fall 2015, Dr Bower.

This program demonstrates a few common uses of the easygui module.

To install the easygui module:
    1. Click the Windows Start button and type "cmd" in the search box.
    2. Click cmd.exe to start a Windows command prompt.
    3. Type the following command and press enter:
        python -m pip install easygui
    4. If you see the message, "Successfully installed easygui", that's it;
       if you see any other message, ask your instructor for assistance.

Documentation: http://easygui.sourceforge.net/index.html.
"""

import easygui


def main():
    """Main program to demonstrate the easygui module."""

    # The most basic message box displays a message with an OK button.
    easygui.msgbox( "Your software installation is complete.\n\n" +
                    "This and the following dialogs are a\ndemonstration of the easygui module.\n\n" +
                    "Your responses to each dialog are\nprinted in the console window.\n\n" +
                    "You may find this module useful\nthroughout the semester." )

    # A default Yes/No box asks "Shall I continue?", shows Yes and No buttons,
    # and returns True if Yes is clicked, False if No is clicked.
    response = easygui.ynbox()
    print( type( response ), response )

    # The message/question and dialog title can be specified.
    response = easygui.ynbox( msg="Is your squad the best at USAFA?", title="Best Squad?" )
    print( type( response ), response )

    # The more generic Bool box allows different text in the Yes/No buttons.
    response = easygui.boolbox( msg="Is your squad the best at USAFA?", title="Best Squad?",
                                choices=[ "Hooah!", "Form 10" ] )

    # This is how you might use the response from a Yes/No or Bool box.
    # Note the variable 'response' is already True or False, so there is no
    # need to compare it to anything (i.e., response == True is not necessary).
    if response:
        # The message box displays a message and a button to close the box.
        easygui.msgbox( msg="Of course my squad is best!", title="Best Squad", ok_button="Hooah!" )
    else:
        # If not specified, the button says "OK", as you would expect.
        easygui.msgbox( msg="My squad improves every day.", title="Best Squad" )

    # A button box allows more than two choices.
    response = easygui.buttonbox( msg="Who is your favorite turtle?", title="Select",
                                  choices=[ "Leonardo", "Michelangelo", "Raphael", "Donatello" ] )
    print( type( response ), response )

    # The enter box returns a string and allows specification of the default value.
    response = easygui.enterbox( msg="Enter your favorite baseball team:",
                                 title="Go Cubs!", default="Chicago Cubs" )
    print( type( response ), response )

    # The integer box returns an int and allows specification of lower and upper bounds.
    response = easygui.integerbox( msg="What is the answer?", title="Input",
                                   default="42", lowerbound=0, upperbound=100 )
    print( type( response ), response )

    # The file open box is a standard file chooser dialog and returns the file name as a string.
    filename = easygui.fileopenbox( msg="Open file...", filetypes=[ "*.txt", "*.py" ] )
    print( type( filename ), filename )

    # Here is a simple way to read the entire contents of a file into a single string.
    with open( filename, "r" ) as data_file:
        data = data_file.read()

    # A code box displays editable text in a monospaced font and does not wrap lines;
    # (not shown here, but a textbox would use a proportional font and wrap lines).
    edited_data = easygui.codebox( msg=filename, title="Code Box", text=data )

    # The text in the code box is returned as a single string when the window is closed.
    if data == edited_data:
        easygui.msgbox( msg="No changes made to text." )
    else:
        # The file save box asks to confirm before overwriting an existing file.
        filename = easygui.filesavebox( msg="Save file...", filetypes=[ "*.txt", "*.py" ] )
        # The file name will be None if the user clicks Cancel.
        if filename is not None:
            # Here is a simple way to write the entire contents of a string to a file.
            # Note: If the filename already exists, it will be completely overwritten!!
            with open( filename, "w" ) as data_file:
                data_file.write( edited_data )


# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()
