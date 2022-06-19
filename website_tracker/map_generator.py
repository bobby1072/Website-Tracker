import folium
import pymongo
def show_all():
    client = pymongo.MongoClient(
        "mongodb+srv://dbuser:dbuser@cluster0.sssd1.mongodb.net/ipstore?retryWrites=true&w=majority")
    colec = client["ipstore"]["ip"]
    cursor = colec.find({})
    m = folium.Map([0,0], control_scale=False, zoom_start= 1,
                   tiles="CartoDB dark_matter",
                   attr='Mapbox attribution')
    for document in cursor:
        folium.Marker([document["latitude"], document["longitude"]],
                      popup="<b>"+document["URL"]+"</b>\n<i>hosted by: " + document["ISP"] + "</i>\n<i>" + document["IP"] + "</i>").add_to(m)
    m.save("map.html")
    return ("map.html")
def map_gen(point, url):
    m = folium.Map([point["latitude"], point["longitude"]], control_scale=False, zoom_start=18, tiles="CartoDB dark_matter",
                   attr='Mapbox attribution')
    folium.Marker([point["latitude"], point["longitude"]], popup="<b>"+ url+"</b>\n<i>hosted by: "+ point["isp"] +"</i>\n<i>" + point["ip"] + "</i>").add_to(m)
    m.save("map.html")
    return ("map.html")
