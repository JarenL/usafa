"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: Dr. Bower / Col Gibson / LtCol Harder / LtCol (Ret) Christman

Documentation: None required; cooperation on labs is highly encouraged!
=======================================================================
"""

from CounterGui import Ui_CounterGui as Gui
from PyQt4 import QtCore, QtGui
import sys


def main():
    """Launch a GUI created with Qt Designer."""
    # Create a QApplication to handle event processing.
    qt_app = QtGui.QApplication( sys.argv )

    # Create an instance of the app and show the main window.
    my_app = App( "Blue" )
    my_app.main_window.show()

    my_app2 = App("Silver", 300)
    my_app.main_window.show()

    # Execute the QApplication, exiting when it returns (i.e., the window is closed).
    sys.exit( qt_app.exec_() )  # Note the underscore at the end of exec_().


class App:
    """Application class to create and control the gui."""

    def __init__( self, title="Counter", x=40, y=40, w=200, h=150 ):
        """Initialize the gui."""
        # Create the main window in which our gui will display.
        self.main_window = QtGui.QWidget()  # QMainWindow() for menu and status bar.

        # Create an instance of our gui and set it up in the m  ain window.
        self.gui = Gui()  # Generic name "Gui" from "as Gui" clause of import statement.
        self.gui.setupUi( self.main_window )

        self.gui.increment_button.clicked.connect(self.increment)
        self.gui.decrement_button.clicked.connect(self.decrement)

        self.main_window.setWindowTitle(title)
        self.main_window.setGeometry(x, y, w, h)

        self.counter = 0
    def increment(self):
        self.counter += 1
        self.gui.count_label.setText( str(self.counter))
    def decremenet(self):
        self.counter -= 1
        self.gui.count_label.setText( str(self.counter))



# The following two lines are always the last lines in a source file and they
# start the execution of the program; everything above was just definitions.
if __name__ == "__main__":
    main()