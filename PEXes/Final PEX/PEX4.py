"""CS 210, Introduction to Programming, Fall 2015, Lynch_Jaren.

Instructor: LtCol (Ret) Christman

Documentation: Had to do a lot of reading for this project, bit off more than I could chew in the end and found myself
trying to learn javascript so it would prettier instead of relying on pyqt like I should have. "maphtml" on line 26
was developed from the Google Map Python API posted on google's developer sight. Used this to build write the javascript
and the Browser class. Read on stackoverflow about the imghdr and exifread libraries. I used the exifread library to
extract EXIF data from photos I used the method provided in the exifread library documentation.
Imghdr was used to check if files were images. Used on line 93. Also read on wikipedia.org the formula for converting 
longitudinal coordinates to degree coordinates.
=======================================================================
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
import exifread
import easygui
import os
import sys
import imghdr

maphtml = '''
<!DOCTYPE html>
<html>
  <head>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=drawing"></script>
    <script>
      function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(37.5, -122.2),
          zoom: 10,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

        var drawingManager = new google.maps.drawing.DrawingManager({
          drawingMode: google.maps.drawing.OverlayType.MARKER,
          drawingControl: true,
          drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: [google.maps.drawing.OverlayType.MARKER]
          },
          polygonOptions: {editable: true, draggable: true},
        });
        drawingManager.setMap(map);

        var thePolygon = null;

        google.maps.event.addListener(drawingManager, 'markercomplete', function (marker) {
          marker.getPosition().for(function (xy, i) {
            self.markercomplete(xy.lat(), xy.lng(), i);
          });
        });
      }

      google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
'''


def main():
    """
    Begins the program. Prompts user for image file and then passes this to get_exif function. Only file no directory.
    :return:
    """
    start = easygui.buttonbox(msg="Picture or Folder?", title="Welcome to Where's My Ex! Choose a Picture",
                              choices=["Upload Picture", "Cancel"])
    # if start == "Upload Directory":
    #     file_search = easygui.diropenbox()
    #     directory_list = os.listdir(file_search)
    #     for file in directory_list:
    #         if imghdr.what(file) == "gif" or "jpeg":
    #             get_exif(file)
    #         else:
    #             print("No image detected")
    #             sys.exit()
    if start == "Upload Picture":
        file = easygui.fileopenbox(default="./data/")
        if imghdr.what(file) == 'gif' or 'jpeg':
            get_exif(file)
        else:
            print("No image detected")
            sys.exit()
    elif start == "Cancel":
        sys.exit(0)  # Exit Program


def get_exif(picture):
    """
    :param picture: Is the image file user selects. Extract EXIF data.
    :return: Passes latittude/longitude data to latlong_to_degrees function to turn into degrees.
    """
    image = open(picture, 'rb')
    tags = exifread.process_file(image)
    gps_out = []
    what_i_need = ('GPS GPSLatitude', 'GPS GPSLatitudeRef', 'GPS GPSLongitude', 'GPS GPSLongitudeRef')
    for tag in what_i_need:
        try:
            val = "%s" % tags[tag]
            if isinstance(val, list):
                gps_out.extend(map(str, float(val)))
            else:
                gps_out.append(val)
        except KeyError:
            print('Key %s does not exists' % tag)

    # Had a list of strings and had to do following code so they wouldn't break when I calculated them.
    list1 = gps_out[0]
    list2 = gps_out[2]
    latitude = list1.strip("[]").split(",")
    longitude = list2.strip("[]").split(",")
    last_number_lat = latitude[2].split("/")
    last_number_long = longitude[2].split("/")
    latitude[2] = int(last_number_lat[0]) / int(last_number_lat[1])
    longitude[2] = int(last_number_long[0]) / int(last_number_long[1])
    latlong_to_degress(latitude, longitude)


def latlong_to_degress(latitude, longitude):
    """
    Function to convert the GPS coordinates stored in the EXIF to degrees.
    :param latitude: Latitude in degrees
    :param longitude: Longitude in degrees
    :return: Returns list of latitude and longitude data in degrees.
    """
    lat_degrees = int(latitude[0]) + int(latitude[1]) / 60 + int(latitude[2]) / 3600
    long_degrees = int(longitude[0]) + int(longitude[1]) / 60.0 + int(longitude[2]) / 3600.0
    coords = [lat_degrees, long_degrees]
    print(coords)
    return lat_degrees, long_degrees

main()

class Browser(QApplication):
    """
    Used to build the map window. SHOULD have taken the latlong data from the the above functions and printed them on
    the map.
    """
    def __init__(self):
        QApplication.__init__(self, [])
        self.window = QWidget()
        self.window.setWindowTitle("Google Google Maps Maps");

        self.web = QWebView(self.window)
        self.web.setMinimumSize(800,800)
        self.web.page().mainFrame().addToJavaScriptWindowObject('self', self)
        self.web.setHtml(maphtml)

        self.text = QTextEdit(self.window)

        self.layout = QVBoxLayout(self.window)
        self.layout.addWidget(self.web)
        self.layout.addWidget(self.text)

        self.window.show()
        self.exec_()

    @pyqtSlot(float, float, int)
    def markercomplete(self, lat, lng, i):
        # if i == 0:
        #     self.text.clear()
        self.text.append("Point #{} ({}, {})".format(i, lat, lng))

Browser()
