import tweepy
import csv
import json
import pandas as pd
import datetime
import os
import sys
from datetime import date
from _csv import writer

class TweetAndRetweet:
    
    def Allclear(self):
        self.tweetID.clear()
        self.tweetDict.clear()
        self.tweetString.clear()
        self.replyStringList.clear()
        self.retweetStringDict.clear()
        self.fullText.clear()
        self.typeList.clear()
        self.idList.clear()
        self.keyList.clear()
    
    def __init__(self):
        self.tweetID = list()
        self.tweetDict = {}
        self.tweetString = list()
        self.replyStringList = list()
        self.retweetStringDict = {}
        self.fullText = list()
        self.typeList = list()
        self.idList = list()
        self.keyList = list()
        self.path = "C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\tweets\\"
        self.outpath = 'C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\getinfo\\'
        
    def getTweetList(self,path):
        with open(path) as json_data:
            data = json.load(json_data)
            for i in range(len(data)):
                if "retweeted_status" in data[i]:
                    newTweetID = data[i]["retweeted_status"]["id"] 
                    if newTweetID not in self.tweetID:
                        self.tweetID.append(newTweetID)
                        self.tweetStringDict[newTweetID] = data[i]["retweeted_status"]["text"] 
                    
                        
    def getRetweetList(self,path):
        
        with open(path) as json_data:
            data = json.load(json_data)
            for i in range(len(data)):
                if "retweeted_status" in data[i]:
                    preseentList = list()
                    newTweetID = data[i]["retweeted_status"]["id"]
                    if newTweetID in self.tweetDict:
                        retweetID = data[i]["id"]
                        tempID = self.tweetDict[newTweetID]
                        for j in range(len(tempID)):
                            preseentList.append(tempID[j])
                        preseentList.append(retweetID)  
                        self.tweetDict[newTweetID] = preseentList
                        self.retweetStringDict[retweetID] =  data[i]["text"]
                    else:
                        retweetID = data[i]["id"]
                        preseentList.append(newTweetID)
                        preseentList.append(retweetID)
                        self.tweetDict[newTweetID] = preseentList
                        self.retweetStringDict[retweetID] = data[i]["text"]
                        
    def getFullText(self):
        for tweetID,value in self.tweetDict.items():
            retweetIDs = self.tweetDict[tweetID]
            tweetString = self.tweetStringDict[tweetID]
            self.fullText.append(tweetString.encode('utf-8'))
            self.typeList.append("Tweet")
            self.idList.append(tweetID)
            
            
            
            for i in range(len(retweetIDs)-1):
                retweetID = retweetIDs[i+1]
                retweetString = self.retweetStringDict[retweetID]
                self.fullText.append(retweetString.encode('utf-8'))
                self.typeList.append("Retweet")
                self.idList.append(retweetID)
        
    def getReplyList(self, path):
        with open(path) as json_data:
            data = json.load(json_data)
            for i in range(len(data)):
                checkLang = data[i]["user"]["lang"]
                if(checkLang == 'en'  or checkLang == 'en-gb' ):
                    tempID = data[i]["in_reply_to_status_id_str"]
                    
                    if tempID is not None:
                        if tempID in self.tweetDict:
                            tempList = list()
                            tempString = self.tweetDict[tempID]
                            
                            for i in range(len(tempString)):
                                tempList.append(tempString[i])
                            tempList.append(data[i]["text"])
                            self.tweetDict[tempID] = tempList
                        else:
                            tempList = list()
                            #tempList.append("Reply")
                            tempList.append(data[i]["text"])
                            self.tweetDict[tempID] = tempList
                    
                
    def getTweets(self):
        CONSUMER_KEY = '0zplvEgFyR9vrn5JPTB6TptBV'
        CONSUMER_SECRET = 'lV7fGEZ6vXqJ8c4fFyiCvwqxxm9LWgdEl0WEydjvCmuSOlrwXJ'
        ACCESS_KEY = '813832637383053318-RMAyJIwV5jhcjF9oyJh7qXdmOYZIWhL'
        ACCESS_SECRET = '0iukegnY3pu5ETnfFu4Mv1rPk8Rv3ezyHeepaF8xml3zk'
        
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        
        try:        
            for key in self.tweetDict:
                data = api.get_status(key);
                jsoncontent =json.dumps(data._json)
                
                data = json.loads(jsoncontent)
                text = data["text"]
                self.tweetID.append(key)
            
                self.tweetString.append(text)
        except:
            print("Status is not present")
            #self.replyStringList.append(self.tweetDict[key])
            
            
    def getFullReplyText(self):
        
        
        
        for i in range(len(self.tweetID)):
            key = self.tweetID[i]
            tweetString = self.tweetString[i]
            self.fullText.append(tweetString.encode("utf-8"))
            self.typeList.append('Tweet')
            self.keyList.append(key)
            replyList = self.tweetDict[key]
            for j in range(len(replyList)):
                self.fullText.append(replyList[j].encode("utf-8"))
                self.typeList.append('Reply')
                self.keyList.append("")
        
    def TweetAndRetweetFunction(self):
        
        dirs = os.listdir(self.path)
        for file in dirs:
            self.Allclear()
            print(file)
            self.getReplyList(self.path+file)
            self.getTweets()
            self.getFullReplyText()
            print("****************************")
            l1 = len(self.keyList)
            l2 = len(self.typeList)
            l3 = len(self.fullText)
            
            fileName = file.split(".")[0]
            path_parse = self.outpath+fileName+".csv"        
            rows = zip(self.keyList,self.typeList,self.fullText)
             
            with open(path_parse,'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(["keyList","typeList","fullText"])
                #try:
                for row in rows:
                    writer.writerow(row)
                #
            
tweetAndRetweet = TweetAndRetweet()
tweetAndRetweet.TweetAndRetweetFunction()

