from configparser import SafeConfigParser
import sqlQueries
import config
import re
parser = SafeConfigParser()
parser.read('config.txt')

def locationDef():
    locationQuery = input("Please type Scotland for tweets from Scotland, England for tweets from England or press enter if you want all tweets: ")

    if locationQuery.lower() =="scotland":
        location = "Scotland"
    elif locationQuery.lower() =="england":
        location = "England"
    else:
        location = "-"

    config.setLocation(location)

    return location

def fetchingTweets(cursor, location, searchQuery):
    keywords = input("Please enter any keywords for search or press enter to continue: ")
    keywordsList =keywords.split()
    row=[]
    listOfTweetIds=[]
    if len(keywords) !=0:
        rowL = keywordGroupSearch(keywordsList,cursor,searchQuery,location)
        for tweet in rowL:
            if tweet[4] not in listOfTweetIds:
                row.append(tweet)
                listOfTweetIds.append(tweet[4])
    else:
        stopCount = 0
        if len(location)!=0:
            rowL = sqlQueries.locationQuery(cursor,searchQuery,location)
            for tweet in rowL:
                if tweet[4] not in listOfTweetIds:
                    row.append(tweet)
                    listOfTweetIds.append(tweet[4])
        else:
            row = sqlQueries.retrieveAllTweets(cursor,searchQuery)

    return row

def keywordGroupSearch(keywordsList,cursor,searchQuery,location):
    row=[]
    rowL = []
    for keyword in keywordsList:
        if len(location)!=0:
            result = sqlQueries.locationQueryKeyword(cursor, keyword,searchQuery, location)
            rowL.append(result)
        else:
            result = sqlQueries.retrieveTweetsByKeyword(cursor, keyword, searchQuery)
            rowL.append(result)

        for sublist in rowL:
            for tweet in sublist:
                row.append(tweet)
    return row

def searchForGroup(cursor, wordList,searchQuery,location):
    row = keywordGroupSearch(wordList,cursor,searchQuery,location)
    groupRow=[]
    treshhold = len(wordList)
    print (treshhold)
    listOfTweetIDs = []
    for tweet in row:
        count=0       
        alreadySeen=[]

        for word in wordList:
            regex = r'\b'+word+'\\b'
            listL=re.findall(regex,tweet[2].lower())
            if len(listL)>0 and str(word) not in alreadySeen:
                alreadySeen.append(word)
                count+=1 
            if count==treshhold and tweet[4] not in listOfTweetIDs:
                groupRow.append(tweet)   
                listOfTweetIDs.append(tweet[4])
    return groupRow    

def searchForKeyword(cursor, word,searchQuery,location):
    row=sqlQueries.locationQueryKeyword(cursor, word,searchQuery, location)  

    listOfTweetIDs=[]
    newRow=[]
    for tweet in row: 
        regex = r'\b'+word+'\\b'
        listL=re.findall(regex,tweet[2].lower())
        if len(listL)>0 and tweet[4]not in listOfTweetIDs:
            newRow.append(tweet)
            listOfTweetIDs.append(tweet[4])

    return newRow   

