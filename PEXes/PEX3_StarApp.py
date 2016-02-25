"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: LtCol (Ret) Christman

Documentation: Had an issue where my program would not run. Asked LtCol Christman for assistance and he recommended I
change the object name of the "none" button. This fixed my error. Read on stackoverflow.com about tuples and why my
draper, harvard, and name search weren't working. Had to make it no longer a tuple. Seen starting on line 97. Referanced
the spot lab and used that as the base for my code. Changed values, but similar structure.
=======================================================================
"""

from PEXes.PEX3_StarGui import Ui_PEX3_StarGui as Gui
from PyQt4 import QtCore, QtGui
import math
import sys


def main():
    """Launch a GUI created with Qt Designer.
    return: none
    """
    # Create a QApplication to handle event processing.
    qt_app = QtGui.QApplication(sys.argv)

    # Create an instance of the app and show the main window.
    my_app = App()
    my_app.main_window.show()

    # Execute the QApplication, exiting when it returns (i.e., the window is closed).
    sys.exit(qt_app.exec_())  # Note the underscore at the end of exec_().


class App:
    """Application class to create and control the gui."""

    def __init__(self):
        """Initialize the gui.
        return: none
        """
        # Create the main window in which our gui will display.
        self.main_window = QtGui.QMainWindow()  # QMainWindow() for menu and status bar.
        # Create an instance of the gui and set it up in the main window.
        self.gui = Gui()  # Generic name "Gui" from "as Gui" clause of import statement.
        self.gui.setupUi(self.main_window)
        # Connect the menu buttons to methods.
        self.gui.action_exit.triggered.connect(self.main_window.close)
        # Opens file explorer when "file" menu item is clicked.
        self.gui.actionOpen_2.triggered.connect(self.open_file)
        # Dialog box to add Name when menu item is clicked.
        self.gui.action_name.triggered.connect(self.search_name)
        # Dialog box to add Draper number when menu item is clicked.
        self.gui.action_draper.triggered.connect(self.search_draper)
        # Dialog box to add harvard number when menu item is clicked.
        self.gui.action_Harvard_Revised_Number.triggered.connect(self.search_harvard)
        # Displays "about" information when menu item is clicked.
        self.gui.action_about.triggered.connect(self.about)
        # Connect the color button group to know when any button in the group is clicked.
        self.gui.ConstellationGroup.buttonClicked.connect(self.button_click)
        # Connect mouse clicks to know when user clicks on star map.
        self.gui.drawing_widget.mousePressEvent = self.mouse_click
        # Enables drawing stars.
        self.gui.drawing_widget.paintEvent = self.paint_event
        width = self.gui.drawing_widget.width()
        height = self.gui.drawing_widget.height()
        if width > height:
            self.scale = height
        else:
            self.scale = width
        # List of stars
        self.star_list = []
        # List of constellations.
        self.constellation = []
        # is none until click or menu search
        self.current_star = None
        self.current_constellation = None

        with open("./data/StarData/Stars_All.txt") as star_lines:
            star_lines = star_lines.read().splitlines()
        for thing in star_lines:
            self.star_list.append(Star(thing, self.scale))


    def open_file(self):
        """ Prompts user to open file in file explorer when menu item is clicked.
        return: none
        """
        self.star_list = []
        star_file = QtGui.QFileDialog.getOpenFileName(directory= "./data/StarData", filter="Stars_*")
        with open(star_file) as starfile:
            lines = starfile.read().splitlines()
            for line in lines:
                self.star_list.append(Star(line, self.scale))

    def about(self):
        """Shows the about dialog."""
        # The QMessageBox works fine, but for reasons I cannot figure out, PyCharm shows warnings.
        QtGui.QMessageBox.about(self.main_window, "About", "CS 210, Fall 2015, StarMap\n\nAuthor: Jaren Lynch")

    def search_draper(self):
        """ Prompts use to enter draper number when menu item is clicked.
        :return: none
        """
        desired_draper = QtGui.QInputDialog.getText(self.main_window, "Input", "Enter Draper Number:")
        # desired_draper is a tuple. Have to use "draper" to call first part of it. Which is what I want.
        draper = desired_draper[0]
        for star in self.star_list:
            if star.draper_number == draper:
                    self.current_star = star
                    # Update the drawing widget.
                    self.gui.drawing_widget.update()

    def search_name(self):
        """ Prompts user to enter name when user clicks menu item.
        :return: None
        """
        desired_name = QtGui.QInputDialog.getText(self.main_window, "Input", "Enter New Name:")
        # desired_name is a tuple. Have to use "name" to call first part of it. Which is what I want.
        name = desired_name[0]
        for star in self.star_list:
            if len(star.find_values) > 6:
                names = star.name.split(";")
                for thing in names:
                    if thing == str(name).upper():
                        self.current_star = star
                        # Update the drawing widget.
                        self.gui.drawing_widget.update()


    def search_harvard(self):
        """ Prompts user to enter harvard number when user clicks menu item.
        :return:
        """
        desired_harvard = QtGui.QInputDialog.getText(self.main_window, "Input", "Enter Harvard Number:")
        # desired_harvard is a tuple. Have to use "harvard" to call first part of it. Which is what I want.
        harvard = desired_harvard[0]
        for star in self.star_list:
            if star.harvard_number == harvard:
                    self.current_star = star
                    # Update the drawing widget.
                    self.gui.drawing_widget.update()

    def mouse_click(self, click):
        """
        :param click: The place where user clicked mouse.
        :return:
        """
        # Get the (x,y) coordinate of the click.
        x, y = click.x(), click.y()
        # Find the Star at the click.
        index = 0
        self.current_star = self.star_list[0]
        while index < len( self.star_list ):
            for star in self.star_list:
                if math.hypot(x - star.newx, y - star.newy ) < \
                        math.hypot(x - self.current_star.newx, y - self.current_star.newy):
                    self.current_star = star
                index += 1

        # Show a message in the status bar; if current_spot is None, this shows "None".
        self.gui.statusbar.showMessage( "Star at ({},{}): {}".format( self.current_star.newx, self.current_star.newy,
                                                                      self.current_star ) )
        # Update the drawing widget.
        self.gui.drawing_widget.update()

    def button_click(self, button):
        """
        :param button: Assignment for button user clicks.
        :return:
        """
        # Assigns current_constellation to button clicked.
        print(self.gui.Cassiopeia)
        if button == self.gui.BigDipper:
            self.current_constellation == button
        elif button == self.gui.BigDipper:
            self.current_constellation == button
        elif button == self.gui.Bootes:
            self.current_constellation == button
        elif button == self.gui.Cassiopeia:
            self.current_constellation == button
        elif button == self.gui.Cygnet:
            self.current_constellation == button
        elif button == self.gui.Gemini:
            self.current_constellation == button
        elif button == self.gui.Hydra:
            self.current_constellation == button
        elif button == self.gui.UrsaMajor:
            self.current_constellation == button
        elif button == self.gui.UrsaMinor:
            self.current_constellation == button
        self.gui.drawing_widget.update()
        print(self.constellation)

    def paint_event( self, paint_event ):
        """Called automatically whenever the drawing widget needs to repaint.

        :param PyQt.QtGui.QPaintEvent q_paint_event: The event object from PyQt (not used).
        """
        # Get a QPainter object that can paint on the drawing widget.
        painter = QtGui.QPainter( self.gui.drawing_widget )

        width = self.gui.drawing_widget.width()
        height = self.gui.drawing_widget.height()
        if width > height:
            self.scale = height
        else:
            self.scale = width

        # Draw the Stars.
        for star in self.star_list:
            star.draw( painter, self.scale )

        if self.current_star is not None:
            self.current_star.draw( painter, self.scale )
            painter.setBrush( QtCore.Qt.red )  # The brush determines the fill color.
            painter.setPen( QtCore.Qt.red )    # The pen determines the outline color.
            # The parameters to drawEllipse are the (x,y) of the upper-left corner and width, height.
            painter.drawEllipse( self.current_star.newx - 1, self.current_star.newy - 1, 2, 2 )
        elif self.current_constellation is not None:
            self.current_constellation.draw( painter, self.scale )
            painter.setBrush( QtCore.Qt.red )  # The brush determines the fill color.
            painter.setPen( QtCore.Qt.red )    # The pen determines the outline color.
            # The parameters to drawLines are the constellations in the text file.
            painter.drawLines( self.current_constellation.newx - 2, self.current_constellation.newy - 2, 4, 4 )

class Star:
    def __init__(self, string, scale):
        """ Initiates Star class.
        :param string: The string input into class.
        :param scale: The window scale.
        :return: none
        """
        self.find_values = string.split()
        self.x = float(self.find_values[0])
        self.y = float(self.find_values[1])
        self.magnitude = float(self.find_values[3])
        self.draper_number = self.find_values[4]
        self.harvard_number = self.find_values[5]
        self.name = " ".join(self.find_values[6:])
        self.newx = (self.x + 1) * scale // 2
        self.newy = (-self.y + 1) * scale // 2
        " ".join(self.name)

    def __str__(self):
        """ Prints string in lower left of gui window.
        :return: String with information about star.
        """
        if len(self.find_values) > 6:
            return "{} {} {} {} {} {}".format(self.x, self.y, self.magnitude, self.draper_number, self.harvard_number,
                                              self.name)
        else:
            return "{} {} {} {} {}".format(self.x, self.y, self.magnitude, self.draper_number, self.harvard_number)
    def draw(self, painter, scale):
        """Draws stars.
        :param painter: Determines the colors of the stars.
        :param scale: Determines window size.
        :return: none.
        """
        grey = 255 * 2.512 ** (-self.magnitude) * 10
        if grey > 255:
            grey = 255
        elif grey < 0:
            grey = 0
        painter.setBrush(QtGui.QColor(grey, grey, grey))
        painter.drawEllipse(self.newx - 1, self.newy - 1, 2, 2)

class Constellation:
    """Draws connected stars as constellations
    return: String in lower left of window with constellation name.
    """
    def __init__(self, constellation, scale):
        self.constellations = "Constellation_" + constellation + ".txt"
        with open("./data/StarData/" + constellation + ".txt") as constellation_points:
            points = constellation_points.read().splitlines()
            list(set(points))
        for star in points:
            self.constellation.append(Constellation(star, scale))
    def __str__(self):
        return "{}".format(self.constellation)
    def draw(self, painter, scale):
        pass
if __name__ == "__main__":
    main()
