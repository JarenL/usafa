from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

 # Create an application
app = QApplication([])
 
# And a window
win = QWidget()
win.setWindowTitle('QWebView Interactive Demo')
 
# And give it a layout
layout = QVBoxLayout()
win.setLayout(layout)
 
# Create and fill a QWebView
view = QWebView()
view.setHtml('''
    var citymap = {
      chicago: {
        center: {lat: 41.878, lng: -87.629},
        population: 2714856
      },
      newyork: {
        center: {lat: 40.714, lng: -74.005},
        population: 8405837
      },
      losangeles: {
        center: {lat: 34.052, lng: -118.243},
        population: 3857799
      },
      vancouver: {
        center: {lat: 49.25, lng: -123.1},
        population: 603502
      }
    };

    function initMap() {
      // Create the map.
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: {lat: 37.090, lng: -95.712},
        mapTypeId: google.maps.MapTypeId.TERRAIN
      });

      // Construct the circle for each value in citymap.
      // Note: We scale the area of the circle based on the population.
      for (var city in citymap) {
        // Add the circle for this city to the map.
        var cityCircle = new google.maps.Circle({
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          map: map,
          center: citymap[city].center,
          radius: Math.sqrt(citymap[city].population) * 100
        });
      }
    }
''')
 
# A button to call our JavaScript
button = QPushButton('Set Full Name')
 
# Interact with the HTML page by calling the completeAndReturnName
# function; print its return value to the console
def complete_name():
    frame = view.page().mainFrame()
    print(frame.evaluateJavaScript('completeAndReturnName();'))
 
# Connect 'complete_name' to the button's 'clicked' signal
button.clicked.connect(complete_name)
 
# Add the QWebView and button to the layout
layout.addWidget(view)
layout.addWidget(button)
 
# Show the window and run the app
win.show()
app.exec_()