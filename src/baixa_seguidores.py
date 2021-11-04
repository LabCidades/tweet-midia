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

lista_perfis = ['@agmural','@perifasemove','@chavosodausp','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']
    
# extração dos tweets e criação do dataframe
followers = []

for perfil in lista_perfis:
    for follower in tw.Cursor(api.followers, screen_name=perfil, tweet_mode="extended").items():
      followers.append([perfil,follower])
    time.sleep(60)
    print('=== extraindo tweets do :',perfil)
df = pd.json_normalize(followers)

#salva csv
compression_opts = dict(method='zip',archive_name='dataset_seguidores.csv')
df.to_csv('dataset_seguidores.zip', index=False, compression=compression_opts)