import folium

from FileCreator import FileCreator

fileCreator = FileCreator()


class MapAnalyser:

  def createMap(self, dataframe):
    # create the map.
    map_pickup = folium.Map( location=[41.864073157, -87.706818608])

    # adding the latitude and longitude points to the map.
    dataframe.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], row["Longitude"]] ).add_to(map_pickup), axis=1)

    # display the map: just ask for the object representation in juypter notebook.
    # map_pickup
    fileCreator.createEmptyFile()

    # optional: save the map.
    print("Começa processo para salvar mapa")
    map_pickup.save(fileCreator.getPathForFile())
    print("Termina processo para salvar mapa")