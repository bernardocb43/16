import folium

latitude = 40.208730
longetude = -8.413234


mapa_portugal = folium.Map(location=[latitude, longetude], zoom_start=6)

folium.Marker(
    location=[38.7071, -9.13594],
    popup='Lisboa',
    icon=folium.Icon(icon='cloud')


).add_to(mapa_portugal)

folium.Marker(
    location=[41.1579, -913549],
    popup='Porto',
    icon=folium.Icon(icon='cloud')


).add_to(mapa_portugal)


mapa_portugal.save('mapa_portugal.html')
