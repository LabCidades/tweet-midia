# importa tweepy
import json
import tweepy as tw
import pandas as pd
import time
import os
#from decouple import config

API_KEY = 'RKOGzIv2WtGF5DqI1ij4y1xJ8'
API_SECRET = 'mzXrng0SK6mGaIiHQsfTv6nMS9LOICn11Rkjx6VNlw4dauyLUP'

# dados de autenticacao
my_api_key = API_KEY
my_api_secret = API_SECRET

# autenticacao
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#parametros de busca
lista_perfis = ['@agmural','@perifasemove','@chavosodausp','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']
lista_perfis_2 = ['@agmural']
data_desde = "2020-02-26"
    
# extração dos tweets e criação do dataframe

for perfil in lista_perfis_2:
  tweets = []
  for status in tw.Cursor(api.user_timeline, screen_name=perfil, tweet_mode="extended",count=200).items(10000):
      tweets.append(status._json)
  print('=== extraindo tweets do :',perfil)
  df = pd.json_normalize(tweets)
  compression_opts = dict(method='zip',archive_name='dataset_tweets_'+perfil+'.csv')
  df.to_csv('dataset_tweets_3_'+perfil+'.zip', index=False, compression=compression_opts)
  time.sleep(300)

""" perfil = '@favelaempauta'
tweets = []
for status in tw.Cursor(api.user_timeline, screen_name=perfil, tweet_mode="extended").items():
    tweets.append(status._json)
print('=== extraindo tweets do :',perfil)
df = pd.json_normalize(tweets)
compression_opts = dict(method='zip',archive_name='dataset_tweets_'+perfil+'.csv')
df.to_csv('dataset_tweets'+perfil+'.zip', index=False, compression=compression_opts) """


#salva csv
""" compression_opts = dict(method='zip',archive_name='dataset_tweets.csv')
df.to_csv('dataset_tweets.zip', index=False, compression=compression_opts) """