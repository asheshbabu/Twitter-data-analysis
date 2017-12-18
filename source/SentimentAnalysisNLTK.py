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
        
    def getSentiments(self,path):
        dirs = os.listdir( path )
        for file in dirs:
            formatedText = list()
            filename = path+file
            df = pd.read_csv(filename)
            self.type = df[['0']]
            type = self.type.values.tolist() 
            self.text = df[['1']]
            text = self.text.values.tolist() 
            self.originalScore = df [['2']]
            originalScore = self.originalScore.values.tolist() 
        
                    
            for i in range(len(text)):
                findSentimentText = text[i]
                #print(findSentimentText)
                findSentimentText = encoding.smart_str(findSentimentText, encoding='ascii', errors='ignore')
                
                findSentimentText = findSentimentText.lower()
                findSentimentText = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',findSentimentText)
                findSentimentText = re.sub('@[^\s]+','AT_USER',findSentimentText)
                findSentimentText = re.sub('[\s]+', ' ', findSentimentText)
                findSentimentText = re.sub(r'#([^\s]+)', r'\1', findSentimentText)
                findSentimentText = findSentimentText.strip('\'"')
                findSentimentText = re.sub('\\\[^\s]+','special_symbol',findSentimentText)
                
                formatedText.append(findSentimentText)
                
               
            
                
#                 sentimentCal = Sentiment()
#                 score = sentimentCal.getSentimentNLTK(findSentimentText)
#                 self.positive.append(score[2])
#                 self.negative.append(score[1])
#                 self.neutral.append(score[0])
#                 self.compound.append(score[3])
#                 
#                 if(score[3]<0.5):
#                     self.calculatedScore.append(-1)
#                 else:
#                     self.calculatedScore.append(-1)
#             text = pd.DataFrame(self.text)
#             txtType = pd.DataFrame(self.type)
#             txtScore = pd.DataFrame(self.score)
#             positive = pd.DataFrame(self.positive)
#             negative = pd.DataFrame(self.negative)
#             neutral = pd.DataFrame(self.neutral)
#             compound = pd.DataFrame(self.compound)
#             originalScore = pd.DataFrame(self.originalScore)
            
#             svmClass = SvmClassification()
#             svmClass.classify(formatedText, originalScore)
            
#             frames = [txtType, text, txtScore, originalScore, positive, negative, neutral, compound]
#             result = pd.concat(frames,axis=1)
#             result.to_csv("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\marged\\result.csv")
            
        
path = "C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\marged\\"
sentiAnalysis = SentimentAnalysisNLTK()
sentiAnalysis.getSentiments(path)  