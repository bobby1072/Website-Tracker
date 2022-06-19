import requests
import socket
import pymongo
def ip_get(web_dom):
    web_ip = socket.gethostbyname(web_dom)
    return web_ip
def data_grab(ip, url):
    data = requests.get("http://ipwhois.app/json/" + ip).json()
    if data["success"] == False:
        exit()
    else:
        client = pymongo.MongoClient(
            "mongodb+srv://dbuser:dbuser@cluster0.sssd1.mongodb.net/ipstore?retryWrites=true&w=majority")
        colec =  client["ipstore"]["ip"]
        post = {
            "IP": str(data["ip"]),
            "ISP" : str(data["isp"]),
            "latitude": float(data["latitude"]),
            "longitude": float(data["longitude"]),
            "URL" : str(url)
        }
        colec.insert_one(post)
        return data
