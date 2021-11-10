import pandas as pd
import numpy as np
import sys
import os

fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)
parentDir = os.path.dirname(fileDir)
print(parentDir)
pasta_dados = os.path.join(parentDir,'data')

#importar as colunas
""" df_colunas = pd.read_csv('colunas_dataset_tweets.csv')
lista_colunas = df_colunas.to_numpy()[:,-1] """

lista_perfis = ['@agmural','@perifasemove','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']

for perfil in lista_perfis:
    df= pd.read_csv(pasta_dados + '\\' + perfil + '_followers.csv', dtype='unicode')
    if perfil == '@agmural':
        dataset_tweets = df
        dataset_tweets['ref'] = perfil
    else:
        dataset_tweets = pd.concat([dataset_tweets,df])
        dataset_tweets['ref'] = perfil
    print("concatenando dataset de seguidores do usuario " + perfil + "..." )

#df = pd.DataFrame(dataset_tweets, columns=lista_colunas)
dataset_tweets.to_csv('dataset_followers_midia.csv',encoding="utf_8")