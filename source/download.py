import tweepy
import csv
import json
import pandas as pd
import datetime
from datetime import date




CONSUMER_KEY = '0zplvEgFyR9vrn5JPTB6TptBV'
CONSUMER_SECRET = 'lV7fGEZ6vXqJ8c4fFyiCvwqxxm9LWgdEl0WEydjvCmuSOlrwXJ'
ACCESS_KEY = '813832637383053318-RMAyJIwV5jhcjF9oyJh7qXdmOYZIWhL'
ACCESS_SECRET = '0iukegnY3pu5ETnfFu4Mv1rPk8Rv3ezyHeepaF8xml3zk'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)




#df = df.as_matrix;
#for index, row in df.iterrows():
#    print (row['TweetID'])

with open('C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\twitter-train-full-A.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    #nTweet = 0
    #flag = 1
    i = 0
    for row in spamreader:
        i = i+1
        id =str(row[0])
        id = id.split(",")[0]
        try:
            data = api.get_status(id);
            with open("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\downloads\\"+id+".json", 'w') as outfile:
                #outfile.write('[')
                outfile.write(json.dumps(data._json))
                print(id)
        except:
                print("No status"+id)
                