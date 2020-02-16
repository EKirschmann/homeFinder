# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:07:23 2020

@author: Elija
"""

import requests
import pandas as pd
from pandas.io.json import json_normalize
import geopandas as gpd
from pprint import pprint


key = 'st0S7qhC8fauybqw9R9kZjaEZpSChUsLo9uUz9cZ'
location = 'Denver+CO'

thing = requests.get(f'https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key={key}&location={location}').json()

df = pd.DataFrame(thing)

gdf = gpd.GeoDataFrame(thing)



