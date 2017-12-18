import tweepy
import csv
import json
import pandas as pd
import datetime
from datetime import date

textType = list()
textList = list()
scoreList = list()



df = pd.read_csv('C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\USA_02_14_01.csv')
dfList = df.values.tolist()

for i in range(len(dfList)):
    type = dfList[i][1]
    text = dfList[i][2]
    score = dfList[i][3]
    
    if(type=="Tweet"):
        textType.append(type)
        textTemp = text
        textList.append(textTemp)
        scoreList.append(score)
    else:
        textType.append(type)
        textTemp = textTemp+text
        textList.append(textTemp)
        scoreList.append(score)
        
textTypeDf = pd.DataFrame(textType)     
textListDf = pd.DataFrame(textList)        
scoreListDf = pd.DataFrame(scoreList)                
result = pd.concat([textTypeDf,textListDf,scoreListDf],ignore_index=True,axis=1)
print(result)

result.to_csv("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\USA_02_14_01_result.csv", sep=',')
