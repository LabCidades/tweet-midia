import tweepy
from decouple import config
import time
import csv

consumer_key = config('twitter_apikey')
consumer_secret = config('twitter_apisecret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

lista_perfis2 = ['@agmural','@perifasemove','@chavosodausp','@favelaempauta','@ccsp_oficial','@PRODUTORAABANCA','@luanapsol','@RACIONAISCN','@criolomc','@CulturaSP','@ducavendish','@MajiwkiJacques','@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']
lista_perfis = ['@arthurmoledoval','@LuisAdorno','@augustosnunes','@jnascim','@J_LIVRES','@GuilhermeBoulos','@MidiaNINJA']

def get_followers(user_name):
    """
    get a list of all followers of a twitter account
    :param user_name: twitter username without '@' symbol
    :return: list of usernames without '@' symbol
    """
    api = tweepy.API(auth, wait_on_rate_limit=True,timeout=180)
    followers = []
    for page in tweepy.Cursor(api.get_followers, screen_name=user_name,count=200).pages(30):
        try:
            followers.extend(page)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    return followers

def save_followers_to_csv(user_name, data):
    """
    saves json data to csv
    :param data: data recieved from twitter
    :return: None
    """
    HEADERS = ["name", "screen_name", "description", "followers_count", "followers_count",
               'friends_count', "listed_count", "favourites_count", "created_at"]
    with open(user_name + "_followers_2.csv", 'w',encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(HEADERS)
        for profile_data in data:
            profile = []
            for header in HEADERS:
                profile.append(profile_data._json[header])
            csv_writer.writerow(profile)

for perfil in lista_perfis:
    data = get_followers(perfil)
    save_followers_to_csv(perfil,data)
