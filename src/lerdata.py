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
df_colunas = pd.read_csv('colunas_dataset_tweets.csv')
lista_colunas = df_colunas.to_numpy()[:,-1]

lista_perfis = ['@agmural','@perifasemove','@chavosodausp','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']

for perfil in lista_perfis:
    df= pd.read_csv(pasta_dados + '\dataset_tweets_' + perfil + '.csv', dtype='unicode')
    if perfil == '@agmural':
        dataset_tweets = df[lista_colunas]
    dataset_tweets = np.r_[dataset_tweets, df[lista_colunas].to_numpy()]
    print("concatenando dataset do usuario " + perfil + "..." )

df = pd.DataFrame(dataset_tweets, columns=lista_colunas)
df.to_csv('dataset_tweets_midia.csv',encoding="utf_8")

