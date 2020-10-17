import tweepy
import pandas as pd
import time
import os
import configparser
from flask import Flask
import json

app = Flask(__name__)


#putting all secrets in config file
config = configparser.ConfigParser()
config.read(r'C:\Users\Ankesh Prasad\Desktop\My Works\Product\Twitter Trend App\config.ini')
keys = config['keys']

#Readig keys from config file. Replace it while running the file
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# print("Authenticated")

tweets = []

@app.route("/save_top_tweets", methods = ['GET'])
def trending_tweets_to_csv():
    try:      
        # Creation of query method using parameters
        # tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
        tweets = api.trends_place(id = 1)
        # print("tweets ==> ", tweets)

        # Pulling information from tweets iterable object
        tweets_list = [[tweet['name'], tweet['url'], tweet['tweet_volume']] for tweet in tweets[0]['trends']]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list,columns=['Tweet', 'Tweet URL', 'Tweet Volume'])

        # Converting dataframe to CSV 
        path=r'C:\Users\Ankesh Prasad\Desktop\My Works\Product\Twitter Trend App'
        tweets_df.to_csv(os.path.join(path,'trending_tweets_{}.csv'.format(tweets[0]['created_at'][0:10])), sep=',', index = False)

    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)
    
    return "File Saved!"

# Calling function to turn username's past X amount of tweets into a CSV file
# trending_tweets_to_csv()

@app.route("/get_top_tweets", methods = ['GET'])
def trending_tweets():
    data_dict = {}
    try:      
        # Creation of query method using parameters
        # tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
        tweets = api.trends_place(id = 1)
        # print("tweets ==> ", tweets)

        # Pulling information from tweets iterable object
        for tweet in tweets[0]['trends']:
            data_dict[tweet['name']] = {
                "url":tweet['url'],
                "volume": tweet['tweet_volume']
            }




    except BaseException as e:
          print('failed on_status,',str(e))
          time.sleep(3)
    
    return json.dumps(data_dict,indent=4)

if __name__ == "__main__":
    app.run()