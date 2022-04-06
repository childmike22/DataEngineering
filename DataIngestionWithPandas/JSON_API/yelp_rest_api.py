import pandas as pd
from pandas.io.json import json_normalize
import requests
import os

# accessing yelp data on bookstores in San Francisco
api_url = 'https://api.yelp.com/v3/businesses/search'


# setup my paramaters using a dictionary (required params can be found in the documentation)
params = {'term': 'bookstore',
          'location': 'San Francisco'}


# setup header dictionary w/ API key (from documentation)
headers = {'Authorization': 'Bearer {}'.format(os.environ['YOUR_API_KEY'])}


# call the API!
response = requests.get(api_url,
                        params=params,
                        headers=headers)


# check to see if our call was successful
print(response.status_code)
print(response.json())


# create a dataframe with bookstores
result = response.json()
bookstores = json_normalize(result['businesses'], sep='_')


print(bookstores.head())
print(bookstores.info())
