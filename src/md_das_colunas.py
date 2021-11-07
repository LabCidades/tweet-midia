import pandas as pd
import numpy as np

#importar as colunas
df_colunas = pd.read_csv('colunas_dataset_tweets.csv')
lista_colunas = df_colunas.to_numpy()[:,-1]

df_colunas.to_markdown('markdown_colunas.md')