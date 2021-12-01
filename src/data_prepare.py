import pandas as pd
import numpy as np

df_tweets_full = pd.read_csv('dataset_tweets_midia.csv')

df_tweets = df_tweets_full[['user.name','full_text','user.followers_count']]
df_tweets['midia_formal'] = 0

df_tweets.to_csv('dataset_topic_modelling.csv',index=False)
