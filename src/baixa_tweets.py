# importa tweepy
import json
import tweepy as tw
import pandas as pd
import time
import os
from decouple import config

API_KEY = config('twitter_apikey')
API_SECRET = config('twitter_apisecret')

# dados de autenticacao
my_api_key = "RKOGzIv2WtGF5DqI1ij4y1xJ8"
my_api_secret = "mzXrng0SK6mGaIiHQsfTv6nMS9LOICn11Rkjx6VNlw4dauyLUP"

# autenticacao
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

lista_perfis = ['@agmural','@perifasemove','@chavosodausp','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']
    
# extração dos tweets e criação do dataframe
tweets = []

for perfil in lista_perfis:
  for status in tw.Cursor(api.user_timeline, screen_name=perfil, tweet_mode="extended").items(10):
      tweets.append(status._json)
  time.sleep(60)
  print('=== extraindo tweets do :',perfil)
df = pd.json_normalize(tweets)

#salva csv
compression_opts = dict(method='zip',archive_name='dataset_tweets.csv')
df.to_csv('dataset_tweets.zip', index=False, compression=compression_opts)