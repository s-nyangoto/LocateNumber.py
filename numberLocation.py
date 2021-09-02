import phonenumbers

import folium


from folium import Map

from phonenumbers import geocoder

from myNumber import number

key = "93c521ccada84b2d9502bae63aceb66f"

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

# Get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#import opencagegeocoder
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

# display the location on a map


myMap: Map = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

#save file in html file

myMap.save("myLocation.html")
