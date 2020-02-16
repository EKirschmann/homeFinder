# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:39:34 2020

@author: Elija
"""

import requests
import pandas as pd

host = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {'sensor': 'false', 'address': 'Mountain View, CA'}

results = requests.get(host, params=params).json()

results = results['results']

location = results[0]['geometry']['location']

location['lat'], location['lng']


'https://geocoding.geo.census.gov/geocoder/locations/address?street=4600+Silver+Hill+Rd&city=Suitland&state=MD&zip=20746&benchmark=Public_AR_Census2010&format=json'

host2 = 'https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderWebServiceHttpNonParsed_V04_01.aspx?streetAddress=9405%20Thurston%20Court&city=Fairfax%20Station&state=va&zip=22039&apikey=demo&format=json&allowTies=false&tieBreakingStrategy=flipACoin&includeHeader=true&census=true&censusYear=allAvailable&notStore=false&version=4.01'


results = requests.get(host2).json()


#results['OutputGeocodes'][0]['OutputGeocode']['Latitude']
#results['OutputGeocodes'][0]['OutputGeocode']['Longitude']

df = pd.DataFrame(results)
