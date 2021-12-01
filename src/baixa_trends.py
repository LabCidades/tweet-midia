# importa tweepy
import json
import tweepy as tw
import pandas as pd
import time
from decouple import config

API_KEY = config('twitter_apikey')
API_SECRET = config('twitter_apisecret')

# dados de autenticacao
my_api_key = API_KEY
my_api_secret = API_SECRET

# autenticacao
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

places = ['23424768']

# extração dos tweets e criação do dataframe
trends = []

brazil_trends = api.get_place_trends('23424768')

trends = json.dumps(brazil_trends, indent=1)
df = pd.json_normalize([brazil_trends])
print(df.head(20))
compression_opts = dict(method='zip',archive_name='dataset_trends_brasil.csv')
df.to_csv('dataset_trends_brasil.zip', index=False, compression=compression_opts)

""" for place in places:
    for trends in tw.Cursor(api.get_place_trends, id=place).items():
      trends.append([place,trends])
      #time.sleep(20)
    print('=== extraindo tweets do :',place)
    df = pd.json_normalize(trends)
    compression_opts = dict(method='zip',archive_name='dataset_trends_'+trends+'.csv')
    df.to_csv('dataset_tweets'+trends+'.zip', index=False, compression=compression_opts)
 """