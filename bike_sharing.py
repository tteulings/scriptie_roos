#!/usr/bin/python3
import requests 
import datetime
import json
import os

URL = "https://www.velo-antwerpen.be/availability_map/getJsonObject"
path = os.getcwd()

r = requests.post(URL)
data = r.json()
datetime = datetime.datetime.now()

with open(path + "/bike_sharing_data.json", "r") as fp:
    try:
        json_data = json.load(fp)
    except:
        json_data = {}

json_data[str(datetime)] = data


with open(path + "/bike_sharing_data.json", "w") as fp:
    json.dump(json_data, fp)