import pandas as pd
import os
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from Sentiment import Sentiment
import re
from SvmClassification import SvmClassification 
from django.utils import encoding

class SentimentAnalysisNLTK:
    
    def __init__(self):    
        self.positive = list()
        self.negative = list()
        self.neutral =  list()
        self.compound = list()
        self.type = list()
        self.text = list()
        self.score = list()
        self.originalScore = list()
        self.calculatedScore = list()
        self.formatedText = list()
        self.correctScore = 0
    def calculateSentiment(self):
        for i in range(len(self.score)):            
            if(int(self.calculatedScore[i]) == int(self.score[i])):
                self.correctScore=self.correctScore+1
                
    def getSentiments(self,path):
        dirs = os.listdir( path )
        
        for file in dirs:
            filename = path+file
            self.positive.clear()
            self.positive.clear()
            self.negative.clear()
            self.neutral.clear()
            self.compound.clear()
            self.type.clear()
            self.text.clear()
            self.score.clear()
            self.originalScore.clear()
            self.calculatedScore.clear()
            self.formatedText.clear()
            self.correctScore = 0
            
            print(filename)
            count = 0
            with open(filename) as csvfile:
                print("here")
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    count = count+1
                    if count >1:
                        self.type.append(row[0])
                        self.text.append(row[1])
                        self.score.append((row[2]))
        
                    
                for i in range(len(self.text)):
                    
                    findSentimentText = self.text[i]
                    #print(findSentimentText)
                    findSentimentText = encoding.smart_str(findSentimentText, encoding='ascii', errors='ignore')
                    
                    findSentimentText = findSentimentText.lower()
                    findSentimentText = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',findSentimentText)
                    findSentimentText = re.sub('@[^\s]+','AT_USER',findSentimentText)
                    findSentimentText = re.sub('[\s]+', ' ', findSentimentText)
                    findSentimentText = re.sub(r'#([^\s]+)', r'\1', findSentimentText)
                    findSentimentText = findSentimentText.strip('\'"')
                    findSentimentText = re.sub('\\\[^\s]+','special_symbol',findSentimentText)
                    findSentimentText = re.sub('\\\[^\s]+','special_symbol',findSentimentText)
                    
                    sentiment = Sentiment()
                    scoreCal = sentiment.getSentimentNLTK(findSentimentText)
                    self.positive.append(scoreCal[2])
                    self.negative.append(scoreCal[1])
                    self.neutral.append(scoreCal[0])
                    self.compound.append(scoreCal[3])
                    
                    if(scoreCal[3]>0.5):
                        self.calculatedScore.append(1)
                    else:
                        self.calculatedScore.append(-1)
                        
                        
                        
                
               
            
        
            self.calculateSentiment()
            total = len(self.score)
            print(total)
            print(self.correctScore)
            accuracy = (self.correctScore/float(total))
            print(accuracy)
            
    
#         if(len(self.formatedText)>2):
#             svmClass = SvmClassification()
#             svmClass.classify(self.formatedText, self.score)
                
#             frames = [txtType, text, txtScore, originalScore, positive, negative, neutral, compound]
#             result = pd.concat(frames,axis=1)
#             result.to_csv("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\marged\\result.csv")
            
        
path = "C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\not_marged\\"
sentiAnalysis = SentimentAnalysisNLTK()
sentiAnalysis.getSentiments(path)  