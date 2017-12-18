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



class ExtractFeature:
    
    
    
    def findPoS(self,tweetText):
        train_text = state_union.raw("2005-GWBush.txt")
        custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
        tokenized = custom_sent_tokenizer.tokenize(tweetText)
        posDict = {'CC':0,'CD':0,'DT':0,'EX':0,'FW':0,'IN':0,'JJ':0,'JJR':0,'JJS':0,'LS':0,'MD':0,'NN':0,'NNS':0,'NNP':0,'NNPS':0, 'PDT':0,'POS':0,
                   'PRP':0,'PRP$':0,'RB':0,'RBR':0,'RBS':0,'RP':0,'TO':0,'UH':0,'VB':0,'VBD':0,'VBG':0,'VBN':0,'VBP':0,'VBZ':0,'WDT':0,'WP':0,'WP$':0,
                   'WRB':0}
        
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)     
            
            for j in range(len(tagged)):
                x = tagged[j]
                y = x[1]
                if(y in posDict):
                    count = int(posDict[y])
                    posDict[y] = count+1
            
        return posDict
        
    
    def getSentimentNLTK(self,tweetSentence):
        score = []
        try:
            #print('==============getSentimentNLTK starts ====================')
            sid = SentimentIntensityAnalyzer()
            sentimentScore = sid.polarity_scores(tweetSentence)
            score.append(sentimentScore['neu']) 
            score.append(sentimentScore['neg']) 
            score.append(sentimentScore['pos']) 
            score.append(sentimentScore['compound']) 
            #print(tweetSentence)
            #print('score = ',score)
            #print('==============getSentimentNLTK ends ====================')
        except :
            score = [0,0,0,0]
            #print('score = ',score)
        return score   
    
    def dictToList(self,dictionaryNew):
        self.CCList.append(dictionaryNew['JJS'])
        self.CDList.append(dictionaryNew['POS'])
        self.DTList.append(dictionaryNew['VBD'])
        self.EXList.append(dictionaryNew['NN'])
        self.FWList.append(dictionaryNew['RP'])
        self.INList.append(dictionaryNew['TO'])
        self.JJList.append(dictionaryNew['JJ'])
        self.JJRList.append(dictionaryNew['RB'])
        self.JJSList.append(dictionaryNew['VBG'])
        self.LSList.append(dictionaryNew['UH'])
        self.MDList.append(dictionaryNew['IN'])
        self.NNList.append(dictionaryNew['WDT'])
        self.NNSList.append(dictionaryNew['EX'])
        self.NNPList.append(dictionaryNew['PDT'])
        self.NNPSList.append(dictionaryNew['VB'])
        self.PDTList.append(dictionaryNew['NNS'])
        self.POSList.append(dictionaryNew['LS'])
        self.PRPList.append(dictionaryNew['NNPS'])
        self.PRPDList.append(dictionaryNew['NNP'])
        self.RBList.append(dictionaryNew['WRB'])
        self.RBRList.append(dictionaryNew['JJR'])
        self.RBSList.append(dictionaryNew['VBZ'])
        self.RPList.append(dictionaryNew['CD'])
        self.TOList.append(dictionaryNew['WP'])
        self.UHList.append(dictionaryNew['PRP'])
        self.VBList.append(dictionaryNew['RBR'])
        self.VBDList.append(dictionaryNew['DT'])
        self.VBGList.append(dictionaryNew['FW'])
        self.VBNList.append(dictionaryNew['MD'])
        self.VBPList.append(dictionaryNew['CC'])
        self.VBZList.append(dictionaryNew['VBN'])
        self.WDTList.append(dictionaryNew['VBP'])
        self.WPList.append(dictionaryNew['WP'])
        self.WPDList.append(dictionaryNew['RBS'])
        self.WRBList.append(dictionaryNew['PRP'])
    
        
        
        
        
    
    def __init__(self):    
        self.dict1 = {}
        self.dictCount = {}
        self.hashtagList = list()
        self.hashtagCount = list()
        self.directMessageList = list()
        self.urlChkList = list()
        self.hashTagList = list()
        self.questionMarkList = list()
        self.exclamationMarkList = list()
        self.positiveList = list()
        self.negativeList = list()
        self.neutralList = list()
        self.combinedList = list()
        self.positiveEmoticon = list()
        self.negativeEmoticon = list()
        self.posDictList = list()
        self.originalScore = list()
        self.CCList=list()
        self.CDList=list()
        self.DTList=list()
        self.EXList=list()
        self.FWList=list()
        self.INList=list()
        self.JJList=list()
        self.JJRList=list()
        self.JJSList=list()
        self.LSList=list()
        self.MDList=list()
        self.NNList=list()
        self.NNSList=list()
        self.NNPList=list()
        self.NNPSList=list()
        self.PDTList=list()
        self.POSList=list()
        self.PRPList=list()
        self.PRPDList=list()
        self.RBList=list()
        self.RBRList=list()
        self.RBSList=list()
        self.RPList=list()
        self.TOList=list()
        self.UHList=list()
        self.VBList=list()
        self.VBDList=list()
        self.VBGList=list()
        self.VBNList=list()
        self.VBPList=list()
        self.VBZList=list()
        self.WDTList=list()
        self.WPList=list()
        self.WPDList=list()
        self.WRBList=list()
        
        
        
        
            
    def directMsg(self,tweetText):
        if('@' in tweetText ):
            self.directMessageList.append(1)
        else:
            self.directMessageList.append(0)
            
    def urlCheck(self,tweetText):
        if('https' in tweetText):
            self.urlChkList.append(1)
        else:
            self.urlChkList.append(0)
        
    def hashCheck(self,tweetText):
        if('#' in tweetText):
            self.hashTagList.append(1)
        else:
            self.hashTagList.append(0)
                
    def questionCheck(self,tweetText):
        if('?' in tweetText):
            self.questionMarkList.append(1)
        else:
            self.questionMarkList.append(0)
            
    def exclamationCheck(self,tweetText):
        if('!' in tweetText):
            self.exclamationMarkList.append(1)
        else:
            self.exclamationMarkList.append(0)
            
    def checkEmoticon(self,tweetText):
        if(':)' in tweetText):
            self.positiveEmoticon.append(1)
        else:
            self.positiveEmoticon.append(0)
            
        if(':(' in tweetText):
            self.negativeEmoticon.append(1)
        else:
            self.negativeEmoticon.append(0)
            
    def features(self,path):
        dirs = os.listdir( path )
        for file in dirs:
            filename = path+file
            print(filename)
            df = pd.read_csv(filename)
            dfList = df.values.tolist()
            for i in range(len(dfList)):
                type = dfList[i][0]
                text = dfList[i][1]
                self.directMsg(text[1:len(text)])
                self.urlCheck(text[1:len(text)])
                self.hashCheck(text[1:len(text)])
                self.questionCheck(text[1:len(text)])
                self.exclamationCheck(text[1:len(text)])
                sentiScore = self.getSentimentNLTK(text[1:len(text)])
                self.neutralList.append(sentiScore[0])
                self.negativeList.append(sentiScore[1])
                self.positiveList.append(sentiScore[2])
                self.combinedList.append(sentiScore[3])
                self.checkEmoticon(text[1:len(text)])
                posDict = self.findPoS(text[1:len(text)])
                self.dictToList(posDict)
                self.posDictList.append(posDict)
                self.originalScore.append(dfList[i][2])
                
                
            
            
             
            directMsg = pd.DataFrame(self.directMessageList)
            urlCheck = pd.DataFrame(self.urlChkList)
            hashCheck = pd.DataFrame(self.hashTagList)
            questionCheck = pd.DataFrame(self.questionMarkList)
            exclamationCheck = pd.DataFrame(self.exclamationMarkList)
            neutralList = pd.DataFrame(self.neutralList)
            negativeList = pd.DataFrame(self.negativeEmoticon)
            positiveList = pd.DataFrame(self.positiveEmoticon)
            combinedList = pd.DataFrame(self.combinedList)
            CCListDf = pd.DataFrame(self.CCList)
            CDListDf = pd.DataFrame(self.CDList)
            DTListDf = pd.DataFrame(self.DTList)
            EXListDf = pd.DataFrame(self.EXList)
            FWListDf = pd.DataFrame(self.FWList)
            INListDf = pd.DataFrame(self.INList)
            JJListDf = pd.DataFrame(self.JJList)
            JJRListDf = pd.DataFrame(self.JJRList)
            JJSListDf = pd.DataFrame(self.JJSList)
            LSListDf = pd.DataFrame(self.LSList)
            MDListDf = pd.DataFrame(self.MDList)
            NNListDf = pd.DataFrame(self.NNList)
            NNSListDf = pd.DataFrame(self.NNSList)
            NNPListDf = pd.DataFrame(self.NNPList)
            NNPSListDf = pd.DataFrame(self.NNPSList)
            PDTListDf = pd.DataFrame(self.PDTList)
            POSListDf = pd.DataFrame(self.POSList)
            PRPListDf = pd.DataFrame(self.PRPList)
            PRPDListDf = pd.DataFrame(self.PRPDList)
            RBListDf = pd.DataFrame(self.RBList)
            RBRListDf = pd.DataFrame(self.RBRList)
            RBSListDf = pd.DataFrame(self.RBSList)
            RPListDf = pd.DataFrame(self.RPList)
            TOListDf = pd.DataFrame(self.TOList)
            UHListDf = pd.DataFrame(self.UHList)
            VBListDf = pd.DataFrame(self.VBList)
            VBDListDf = pd.DataFrame(self.VBDList)
            VBGListDf = pd.DataFrame(self.VBGList)
            VBNListDf = pd.DataFrame(self.VBNList)
            VBPListDf = pd.DataFrame(self.VBPList)
            VBZListDf = pd.DataFrame(self.VBZList)
            WDTListDf = pd.DataFrame(self.WDTList)
            WPListDf = pd.DataFrame(self.WPList)
            WPDListDf = pd.DataFrame(self.WPDList)
            WRBListDf = pd.DataFrame(self.WRBList)
            scoreDf = pd.DataFrame(self.originalScore)
            
            frames = [directMsg, urlCheck, hashCheck, questionCheck, exclamationCheck, neutralList, negativeList,positiveList, combinedList,
                      CCListDf,CDListDf,DTListDf,EXListDf,FWListDf,INListDf,JJListDf,JJRListDf,JJSListDf,LSListDf,MDListDf,NNListDf,NNSListDf,
                      NNPListDf,NNPSListDf,PDTListDf,POSListDf,PRPListDf,PRPDListDf,RBListDf,RBRListDf,RBSListDf,RPListDf,TOListDf,UHListDf,
                      VBListDf,VBDListDf,VBGListDf,VBNListDf,VBPListDf,VBZListDf,WDTListDf,WPListDf,WPDListDf,WRBListDf,scoreDf]
            
            #frames = [self.directMessageList,self.urlChkList,self.hashTagList,self.questionMarkList,self.exclamationMarkList,self.neutralList,self.negativeEmoticon,self.positiveEmoticon,self.combinedList,self.CCList,self.CDList,self.DTList,self.EXList,self.FWList,self.INList,self.JJList,self.JJRList,self.JJSList,self.LSList,self.MDList,self.NNList,self.NNSList,self.NNPList,self.NNPSList,self.PDTList,self.POSList,self.PRPList,self.PRPDList,self.RBList,self.RBRList,self.RBSList,self.RPList,self.TOList,self.UHList,self.VBList,self.VBDList,self.VBGList,self.VBNList,self.VBPList,self.VBZList,self.WDTList,self.WPList,self.WPDList,self.WRBList]
            
#             print(frames)
#             svm_classification = SvmClassification()
#             svm_classification.classify(frames, scoreDf)
            
            
            result = pd.concat(frames,axis=1)
            result.to_csv("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\not_marged_result\\"+file.split(".")[0]+".csv")

            print("C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\not_marged_result\\"+file.split(".")[0]+".csv")

path = "C:\\Users\\ahatua\\Desktop\\usm\\research\\shorttext\\labled\\not_marged\\"

# for file in dirs:
#     fullpath = path+file
#     print(fullpath)
    
extrctFeature = ExtractFeature()
extrctFeature.features(path) 