# importa tweepy
import json
import tweepy as tw
import pandas as pd
import time

# dados de autenticacao
my_api_key = "RKOGzIv2WtGF5DqI1ij4y1xJ8"
my_api_secret = "mzXrng0SK6mGaIiHQsfTv6nMS9LOICn11Rkjx6VNlw4dauyLUP"

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