""" 
1. watch youtube tutorial: https://www.youtube.com/watch?v=8aY_uRPK0iE
2. go to https://pypi.org and search 'requests' library and know how to install it locally
3. go to 'requests' library document (https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
   and take a look at some examples in 'QuickStart' section.
4. practice the below code and run it locally.

"""

import io
import pandas as pd
import requests

URL = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"
resp = requests.get(URL)
if resp.status_code == 200:
   csvtext = resp.text
   csvbuffer = io.StringIO(csvtext)
   df = pd.read_csv(csvbuffer)
   print(df)
   df.to_csv('pokemon.csv')
