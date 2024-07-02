import requests
import folium

# Get geolocation data for your IP address
res = requests.get('https://ipinfo.io/')
data = res.json()
location = data['loc'].split(',')
lat = float(location[0])
log = float(location[1])

# Create a map centered at your location
my_map = folium.Map(location=[lat, log], zoom_start=7)

# Read the GeoJSON data from the file (replace with your actual GeoJSON file)
geojson_data = open('india_states.json', 'r', encoding='utf-8-sig').read()

# Add GeoJSON layer to the map
folium.GeoJson(data=geojson_data).add_to(my_map)

# Add a marker for your location
folium.Marker(location=[lat, log], popup='This is my location').add_to(my_map)

# Save the map to an HTML file
my_map.save("1.html")