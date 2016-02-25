import exifread
import easygui
import os
import sys
import imghdr


# def main():
#     start = easygui.buttonbox(msg="Picture or Folder?", title="Welcome to Where's My Ex! No you don't have a problem.!",
#                               choices=["Upload Directory", "Upload Picture", "Cancel"])
#     if start == "Upload Directory":
#         file_search = easygui.diropenbox()
#         directory_list = os.listdir(file_search)
#         for file in directory_list:
#             if imghdr.what(file) == "gif" or "jpeg":
#                 get_exif(file)
#             else:
#                 print("No image detected")
#                 sys.exit()
#     elif start == "Upload Picture":
#         file = easygui.fileopenbox(default="./data/")
#         if imghdr.what(file) == 'gif' or 'jpeg':
#             get_exif(file)
#         else:
#             print("No image detected")
#             sys.exit()
#     elif start == "Cancel":
#         sys.exit(0)  # Exit Program
        # Add Beijing, you'll want to use your geocoded points here:
        # map.add_point((39.9087, 116.397389))
def get_exif(picture):
    """
    :param picture: Is the image file user selects. Extract EXIF data.
    :return:
    """
    image = open(picture, 'rb')
    tags = exifread.process_file(image)
    gps_out = []
    what_i_need = ('GPS GPSLatitude', 'GPS GPSLatitudeRef', 'GPS GPSLongitude', 'GPS GPSLongitudeRef')
    for tag in what_i_need:
        try:
            val = "%s" % tags[tag]sssssss
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
    """Helper function to convert the GPS coordinates stored in the EXIF to degress."""
    lat_degrees = int(latitude[0]) + int(latitude[1]) / 60 + int(latitude[2]) / 3600
    long_degrees = int(longitude[0]) + int(longitude[1]) / 60.0 + int(longitude[2]) / 3600.0
    coords = [str(lat_degrees), str(long_degrees)]
    print(coords)
    # return coords


class Map(object):
    def __init__(self):
        self._points = []
        print(self._points)

    def add_point(self, coordinates):
        print(coordinates)
        self._points.append((coordinates))
        print(self._points)

    def __str__(self):
        centerLat = sum(( x[0] for x in self._points )) / len(self._points)
        centerLon = sum(( x[1] for x in self._points )) / len(self._points)
        markersCode = "\n".join(
            ["""new google.maps.Marker({{
                position: new google.maps.LatLng({lat}, {lon}),
                map: map
                }});""".format(lat=self._points[0], lon=self._points[1]) for x in self._points
             ])
        return """
            <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
            <div id="map-canvas" style="height: 100%; width: 100%"></div>
            <script type="text/javascript">
                var map;
                function show_map() {{
                    map = new google.maps.Map(document.getElementById("map-canvas"), {{
                        zoom: 8,
                        center: new google.maps.LatLng({centerLat}, {centerLon})
                    }});
                    {markersCode}
                }}
                google.maps.event.addDomListener(window, 'load', show_map);
            </script>
        """.format(centerLat=centerLat, centerLon=centerLon,
                   markersCode=markersCode)


# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    map = Map()
    start = easygui.buttonbox(msg="Picture or Folder?", title="Welcome to Where's My Ex! No you don't have a problem.!",
                              choices=["Upload Directory", "Upload Picture", "Cancel"])
    if start == "Upload Directory":
        file_search = easygui.diropenbox()
        directory_list = os.listdir(file_search)
        for file in directory_list:
            if imghdr.what(file) == "gif" or "jpeg":
                map.add_point(str(get_exif(file)))
            else:
                print("No image detected")
                sys.exit()
    elif start == "Upload Picture":
        file = easygui.fileopenbox(default="./data/")
        if imghdr.what(file) == 'gif' or 'jpeg':
            map.add_point(get_exif(str(file)))

        else:
            print("No image detected")
            sys.exit()
    elif start == "Cancel":
        sys.exit(0)
    with open("output.html", "w") as out:
        print(map, file=out)
