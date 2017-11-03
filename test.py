from os import getenv
import pymssql
import csv
import spacy
import re
import sys
import numpy
import os
from spacy import en
from operator import itemgetter
from collections import Counter
import textCleanUp
import agent_sort
import spacyStopWords
import fileFunctions
import sqlQueries
import inputManagment
import temporalAnalysis
import config
#function to process all tweets split in datasets by keywords and by location
nlp = spacy.load("en")
server = 'localhost'
spacyStopWords.stopWordsList(nlp)
def connect():
            conn = sqlQueries.connectionToDatabaseTest()
            cursor = conn.cursor()
            #cursor = sqlQueries.connectionToDatabase()
            filterKeywords= fileFunctions.readKeywordFile()
            #initiating a list for a total count statistics file
            listOfKeywords = [("keyword", "total count",  "Scotland")]
            locationSc = "Scotland"
            #locationEn = "England" 
            searchQuery = config.searchStringForSqlQuery()

            for word in filterKeywords:
                print ("Search for '"+word+"' for all locations in the database has begun.")
                #searching and collecting from database all words with that keyword in two datasets by location
                if "+" in word:
                    wordList = word.split("+")
                    print (wordList)
                    resultSc=inputManagment.searchForGroup(cursor, wordList,searchQuery,locationSc)
                    #resultEn=inputManagment.searchForGroup(cursor, wordList,searchQuery,locationEn)
                else:
                    resultSc = inputManagment.searchForKeyword(cursor, word,searchQuery,locationSc)
                    #resultEn = inputManagment.searchForKeyword(cursor, word,searchQuery,locationEn)

                #countEn = len(resultEn)
                countSc = len(resultSc)
                count = countSc
                print ("Search for '"+word+"' has finished. There were "+str(countSc)+" tweets containing '"+word+"' in the database." )
                print (" ")
                #if any tweets have been discovered, move to the processing texts stage
                if count>0:
                    fileString=word+"_forVis"

                    rowSc = textCleanUp.removeDupsAndRetweets(resultSc, locationSc)
                    #rowEn = textCleanUp.removeDupsAndRetweets(resultEn, locationEn)
                    print (word)
                    for r in rowSc:
                        print(r[2])
                    #rowEnCount = len(rowEn)
                    rowScCount = len(rowSc)
                    countAllUniques =  rowScCount
                    print ("There are a total of "+str(countAllUniques)+ " unique tweets, "+str(rowScCount)+" from Scotland.")
                    print("/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*/*\*")
                    print (" ")
            
                    visList=[("location","author","text")]
                    sortingTweets(rowSc, visList, locationSc,word)
                    #sortingTweets(rowEn, visList, locationEn,word)
                    fileFunctions.writeCsvFile(visList, fileString)

                    wordTuple = (word, countAllUniques, rowScCount)
                #if there were no tweets retrieved, only add the count to the total count list   
                else:
                    wordTuple = (word, count, countSc)

                listOfKeywords.append(wordTuple)
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")    
            
            fileNameString = "keywordCount"
            fileFunctions.writeCsvFile(listOfKeywords, fileNameString)

            sqlQueries.closeDbConnection()
            return
#function to loop through tweets and filter and clean them
def sortingTweets(rowS, visList, location, word):
    repeatedWords = []
    uniqueWords=[]
    allWords = []
    allWordsFrequency = []
    wordCount = []
    allTweets = []
    finalTextCount = []
    finalTweetTexts=[]
   
    dateList = []
    fileNameString = word+"_"+location

    for row in rowS:
        text = row[2].lower()
        filterWords=[]
        #currently check is set to one as we are only searching for all tweets containing a given keyword, 
        #so the searchForKeywordCombos function is rather redundant right now, however, it can be used in..
        #..case we decide to filter our tweets 
        check = 1
        #check = textCleanUp.searchForKeywordCombos(filterKeywords, text, filterWords,nlp)
        if check==1:
            count = len(text.split(" "))
            countTuple = (row[0], text, count)
            wordCount.append(countTuple)
            sentence = nlp(text)
            cleanText = []
            textCleanUp.textCleanup(allWords,sentence,cleanText)
            cleanTextStr = ' '.join(cleanText)
            tweetList = [row[0],row[1], cleanText, row[3]]
            allTweets.append(tweetList)
            #appending visualisation list
            stripped = row[2].replace("\n", " ")
            if "Scotland" in row[6]:
                locationString = "Scotland"
            elif "England" in row[6]:
                locationString = "England"
            strippedDot = stripped+"."    
            visTuple = (locationString,row[5], strippedDot)
            visList.append(visTuple)
            #appending date list
            date, space ,time = row[3].partition(" ")
            dateTuple = (row, date)
            dateList.append(dateTuple)
    #calling a function for date grouping
    temporalAnalysis.dateGrouping(dateList, fileNameString)
    
    textCleanUp.frequencyCount(nlp, allWords, repeatedWords, uniqueWords, allWordsFrequency, fileNameString)
    textCleanUp.removeUniqueWords(uniqueWords, allTweets, finalTweetTexts, finalTextCount)
    textCleanUp.wordCountGen(wordCount, finalTextCount, fileNameString)
    print(" ")
    #function to create a text file in a format used by the jst tool
    agent_sort.textsByDate(allTweets, wordCount, fileNameString)
    print("Tweets from "+location+" have been processed.")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

connect()
