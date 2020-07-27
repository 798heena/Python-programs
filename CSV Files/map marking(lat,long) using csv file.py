#Python program to demonstrate map marking(lat,long) using csv files

import folium
import pandas
data = pandas.read_csv("Book1.csv")
lt = list(data["LAT"])
ln = list(data["LONG"])
cl = list(data["COLOR"])
map1 = folium.Map(location=(21.1938,81.3509),zoom_start=6)
fg = folium.FeatureGroup(name="My_Map")
for lt1,ln1,cl1 in zip(lt,ln,cl):
    fg.add_child(folium.Marker(location=(lt1,ln1),icon=folium.Icon(color=(cl1))))
map1.add_child(fg)
map1.save("cities.html")
