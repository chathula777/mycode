#!/usr/bin/python3
import requests
import time
import reverse_geocoder as rg
import pprint

params = {
  'access_key': '5048a7d580057913b67e3f013f727c0c'
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

def main():

    api_response = requests.get(api_result).json()

    
    Airline=api_response['airline']['name']
    fn = api_response['flight']['iata']
    fa = api_response['departure']['airport']
    fd = api_response['departure']['iata']
    fda = api_response['arrival']['airport']
    fdaa = api_response['arrival']['iata']


    print(f"""
    Airline: {Airline}
    Flight Number : {fn}
    DAirport: {fa}
    Dairportcode: {fd}
    AAirport: {fda}
        """)



main()

if __name__ == "__main__":
    main()
