import requests 
import datetime
import json

URL = "https://www.velo-antwerpen.be/availability_map/getJsonObject"

r = requests.post(URL)
data = r.json()
datetime = datetime.datetime.now()

with open("bike_sharing_data.json", "r") as fp:
    try:
        json_data = json.load(fp)
    except:
        json_data = {}

json_data[str(datetime)] = data

with open("bike_sharing_data.json", "w") as fp:
    json.dump(json_data, fp)