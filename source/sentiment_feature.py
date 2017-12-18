import tweepy
import csv
import json
import pandas as pd
import datetime
import  os
from datetime import date
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from SvmClassification import SvmClassification
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.ensemble.forest import RandomForestClassifier

class sentiment_feature:
    def getSentiment(self,path):
        dirs = os.listdir( path )
        for file in dirs:
            filename = path+file
            print(filename)

            df = pd.read_csv(filename, header=None)
            data_original = df.as_matrix()
            data = data_original[:,0:len(data_original[0])-1]
            score = data_original[:,len(data_original[0])-1]
             
            vectorizer = TfidfVectorizer(min_df=5,
                                      max_df = 0.8,
                                      sublinear_tf=True,
                                      use_idf=True,decode_error='ignore')
             
             
            train_data = []
            train_labels = []
            test_data = []
            test_labels = []
             
            totalLen = len(data)
            train = int(totalLen*0.7)
            test = totalLen - train
             
            train_data = data[0:train,:]
            train_labels = score[0:train]
            print(len(train_data))
            print(len(train_labels)) 
             
            test_data = data[train+1:totalLen,:]
            test_labels = score[train+1:totalLen]
            print(len(test_data))
            print(len(test_labels))
             
            classifier_rbf = svm.SVC()
            x = list()
            x =  train_data[:]
            classifier_rbf.fit(x, train_labels)
            accuracy = classifier_rbf.score(test_data,test_labels)
            print(accuracy)
             
             
            classifier_rmf = RandomForestClassifier(n_estimators=1500)
            classifier_rmf = classifier_rmf.fit(x, train_labels)
            accuracy = classifier_rmf.score(test_data,test_labels)
            print(accuracy)
        
path = "C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\not_marged_result\\"    
        
sentiment = sentiment_feature()
sentiment.getSentiment(path)