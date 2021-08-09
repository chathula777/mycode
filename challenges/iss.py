#!/usr/bin/env python3
import time
# imports always go at the top of your code
import requests
import reverse_geocoder as rg
import pprint


# Define our "base" API
URL= "http://api.open-notify.org/iss-now.json" 

def main():
    resp = requests.get(URL).json()

    lat = resp["iss_position"]["latitude"]
    lon = resp["iss_position"]["longitude"]
    ts = resp["timestamp"]



    #string from time
    hr_ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    

      # return an ordered dictionary using our lat/lon
    locator_resp= rg.search((lat, lon))

     # slice that object to return the city name only
    city= locator_resp[0]["name"]

    print(f"""
    ISS LOCATION:
    Lat: {lat}
    Lon: {lon}
    Time : {ts}
    City: {city}
    """)

main()


if __name__ == "__main__":
    main()


