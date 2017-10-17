import spacy
import re
from spacy.attrs import ORTH
from spacy import en
import sys
import os
from operator import itemgetter
import fileFunctions
import spacyStopWords
from itertools import groupby

nlp = spacy.load("en")
spacyStopWords.stopWordsList(nlp)
#function to remove stop words, urls, punctuation, numbers and symbols using spacy. Goes through each tweet text and appends the result to two lists, one for the tweet and one for general statistics
def textCleanup(allWords,text):
    for word in text:
                words =re.sub(r'@', "", str(word))
                if word.is_stop != True and word.like_url != True and word.is_punct !=True and word.like_num != True and words.isalpha()== True and len(words)> 1:
                    #someList.append(words)
                    allWords.append(words.lower())
#does a frequency count of words across the whole corpus given to it using spacy and also generates a list of repeated words and unique words
def frequencyCount(tweets, group):

    allWords = []
    repeatedWords=[]
    uniqueWords=[]
    for tweet in tweets:
        text = tweet[0].lower()
        sentence = nlp(text)
        textCleanup(allWords, sentence)
    allWordsStr = ' '.join(allWords)
    doc = nlp(allWordsStr)
    counts = doc.count_by(ORTH)
    i = 0
    #checks how many times each word appears in the whole word list and puts it either in repeated words or in unique words
    for word_id, count in sorted(counts.items(), reverse=True, key=lambda item: item[1]):
        words = nlp.vocab.strings[word_id]

        #if words.isalpha() == True:
        frequencyTuple = (str(count), words.lower())
        frequencyTupleStr = ' '.join(frequencyTuple)
        #allWordsFrequency.append(frequencyTupleStr)
        if count > 1:
                    repeatedWordsTuple = (str(count), words.lower())
                    #repeatedWordsTupleStr = ' '.join(repeatedWordsTuple)
                    repeatedWords.append(repeatedWordsTuple)

        else:
                    uniqueWords.append(words.lower())
    print("Generated frequencies for current group") 

    n=0
    topTen=[]
    #removing the group keywords from that list because we clearly know they are frequent and select the top 10 remaining
    for tup in repeatedWords:
        if tup[1]not in group and n<15:
            topTen.append(tup)
            n+=1               
    return topTen                
    #generate a txt file with all words that have been repeated at least twice
    #fileNameStringAllFreq = "allFrequencies"
    #fileFunctions.writeTxtFrequencyFile(allWordsFrequency,fileNameStringAllFreq, counter)
    #print ("File with the frequencies of all words has been generated. ")

    #fileNameStringRep = "repeatedWords"
    #fileFunctions.writeTxtFrequencyFile(repeatedWords,fileNameStringRep,counter)

    #print ("File with the frequencies of all repeated words has been generated. ")

#removes any word from a tweet which doesn't appear at least twice across the whole tweet corpus
def removeUniqueWords(uniqueWords, allTweets, finalTweetTexts, finalTextCount):
        for tweet in allTweets:
            tweetText = []
            text = tweet[2]
            for word in text:
                words = str(word)
                if words not in uniqueWords:
                    tweetText.append(words)
            #generating a list with the processed text and word count of each tweet for the csv file
            tweetTextS = str(tweetText)
            tweetTextCount = len(tweetText)
            tweetTextTuple = (tweet[0], tweetTextS, tweetTextCount)
            finalTextCount.append(tweetTextTuple)
            #generating a list with the tweet data+filtered text
            tweetList = [tweet[0], tweet[1], tweetText, tweet[3]]
            finalTweetTexts.append(tweetList)
        print ("The unique words have been removed from all the tweets. ")
#removes duplicating tweets (based on platfrom ID) and retweets*
#* if we don't have the original tweet text, one retweet can get through the filtering..
# ..the retweet is stripped from the 'rt' and any mentions and the remaining string is compared to a list of originals
def removeDupsAndRetweets(row, location):
    twitterIDs = []
    origTexts = []
    retweetTexts = []
    rowS=[]
    i = 0
    sortedRow = sorted(row, key=itemgetter(3))
    for r in sortedRow:
        i = i+1
        if r[4] not in twitterIDs:
            twitterIDs.append(r[4])
            #rowS.append(r)
            text = r[2].lower()
            textList = text.split()
            textStrList = [word for word in textList if word.isalpha()]
            textStrRt = ' '.join(textStrList)
            textStr = re.sub(r'rt','',textStrRt)
            textStrStripped = textStr.strip()
            if textList[0]=="rt":
                if textStrStripped in origTexts:
                    retweetTexts.append(textStrStripped)
                else:
                    origTexts.append(textStrStripped)
                    rowS.append(r)

            elif textList[0]!="rt" and textStrStripped not in origTexts:
                origTexts.append(textStrStripped)
                rowS.append(r)

        if i%10000==0:
            print("processed "+ str(i) +  " tweets")

    print ("All tweets from "+location+" have been processed.")

    return rowS
#needs to be fixed in order to filter out properly tweets with shorter strings
def searchForKeywordCombos(filterKeywords, text, filterWords,nlp):
    filterCount = 0
    check = 0
    for word in filterKeywords:
        if str(word)!='fhis' and str(word)!='fhrs' and str(word)!='fsa' and str(word)!='fss':
            wordS=word
            if word in text:
                if word not in filterWords:
                    filterCount += 1
                    filterWords.append(word)
                if filterCount >=1:
                    check = 1
                else:check = 2
        else:
            wordS = "o"+word+"t"
            if word in text:
                textList=text.split()
                for t in textList:
                    if t==word and t.isalpha()==True and wordS not in str(t):
                        if word not in filterWords:
                            filterCount += 1
                            filterWords.append(word)
                        if filterCount >=1:
                            check = 1
                        else:check = 2
    return check

def wordCountGen(wordCount, finalTextCount, counter):
    fileNameString = counter+"_wordCount"
    wordCountFinal = []
    for count in wordCount:
        tweetID = count[0]
        oldCount = count[2]
        origText = str(count[1]).encode(sys.stdout.encoding, errors='replace')
        for cleanCount in finalTextCount:
            if cleanCount[0] == tweetID:
                newText = str(cleanCount[1]).encode(sys.stdout.encoding, errors='replace')
                finalCountTuple = (tweetID, origText, oldCount, newText, cleanCount[2])
                wordCountFinal.append(finalCountTuple)

    fileFunctions.writeCsvFile(wordCountFinal, fileNameString)

def clickableLinks(item):
    r = re.compile(r"(https://[^ ]+)")
    text= r.sub(r'<a href="\1">\1</a>', item)   

    return text 

def extraCharRemoval(item, charList,check):
    for ch in charList:
        if ch in item:
            item=item.replace(ch,"")
    if check==0:        
        itemS=item[1:]   
    elif check==1:
        itemS=item[1:-1] 
    else:
        itemS=item          

    return itemS

def addTweetToNewGroupsList(word,tweet,groupIdStr,newGroups):
    groupId=groupIdStr+word
    tweetWithWord = [tweet[0], tweet[1], tweet[2], tweet[3], tweet[4],word,groupId]
    newGroups.append(tweetWithWord)    

def dictionaryGen(tweetGroups,i):
    dicw={}
    f = lambda x: x[i]
    #putting the tweets in dictionary, split by keywordGroupId
    for key, group in groupby(sorted(tweetGroups, key=f), f):
        dicw[key] = list(group) 

    return dicw    