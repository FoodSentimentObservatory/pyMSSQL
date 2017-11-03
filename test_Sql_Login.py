from os import getenv
import pymssql
import csv
import spacy
import re
import sys
from spacy.attrs import ORTH
import numpy
import os
from spacy import en
from operator import itemgetter
from collections import Counter
import agent_sort
import textCleanUp
import spacyStopWords
import fileFunctions
import sqlQueries
import inputManagment
import temporalAnalysis
import config
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.txt')

finalTweetTexts=[]
wordCount = [("Id","Text", "Count")]
allWords = []
nlp = spacy.load("en")
repeatedWords = []
uniqueWords = []
allWordsFrequency = []
spacyStopWords.stopWordsList(nlp)

def connect():
    try:
        #connection to database
        conn = sqlQueries.connectionToDatabaseTest()
        cursor = conn.cursor()
       
        #getting the keywords file
        searchQuery = config.searchStringForSqlQuery()
        #getting location from user
        locationSc = "Scotland"
        locationEn = "England" 
        print ("--- --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ---")
        print (" ")

        #fetching tweets, either containing a keyword or all tweets
        rowSc = inputManagment.fetchingTweets(cursor, locationSc, searchQuery)
        rowEn = inputManagment.fetchingTweets(cursor, locationEn, searchQuery)

        print (len(rowSc))

        tweetCount = len(rowSc)+len(rowEn)

        print ("Found "+str(tweetCount)+" tweets.")
        #clean the list from duplicating tweets using removeDupsAndRetweets function and sorting the result by date
        rowScUniques=textCleanUp.removeDupsAndRetweets(rowSc,locationSc)
        rowEnUniques=textCleanUp.removeDupsAndRetweets(rowEn,locationEn)
        #sorting the tweets by date
        sortedRowSc = sorted(rowScUniques, key=itemgetter(3))
        sortedRowEn = sorted(rowEnUniques, key=itemgetter(3))

        totalUniques = len(sortedRowSc)+len(sortedRowEn)
        print ("There are a total of "+str(totalUniques)+ " unique tweets, "+str(len(sortedRowSc))+" from Scotland and "+str(len(sortedRowEn))+" from England.")
        print (" ")
            
        #loops through each tweet that has survived the retweet and location filtering
        print ("Beginning the cleanup of tweets text of stopwords, punctuation, numbers and sinle letter words.")
        visList=[]
        dateList=[]
        #sending both lists to be cleaned and split into text files
        rowFunction(sortedRowSc, dateList,visList, locationSc)
        rowFunction(sortedRowEn, dateList,visList, locationEn)
        #sending the resulting lists to generate csv files for dates and for visualisation
        fileStringVis="allTweets_forVis"
        fileStringDates = "allTweets_count_by_dates"
        temporalAnalysis.dateGrouping(dateList, fileStringDates)

        fileFunctions.writeCsvFile(visList, fileStringVis)

    except TypeError as e:
        print (e)
        return None
    
    return

#function for processing the tweets
def rowFunction(sortedRowS, dateList, visList, location):
    #takes a txt file of keywords that will be used for the filtering of tweets
    filterKeywords = fileFunctions.readKeywordFile()

    cleanTextWordCount = [("Id", "Count")]
    counter = ""
    totalCount = 0

    keywordOccurences = []
    keywordCombos = []

    allTweets = []
    cleanTextCounter = 0
#looping through each tweet in the list
    for data in sortedRowS:
            fiteredTexts = []
            text = data[2].lower()
            delimiter = " "
            filterWords = []
            #check how many words from the key words list are present in the tweet
            check = textCleanUp.searchForKeywordCombos(filterKeywords, text, filterWords,nlp)
            #if there are enough keywords in the tweet to suffice the condition, proceed with the text preprocessing
            if check == 1:
                totalCount += 1
                #generating a list with the original text and word count of each tweet for the csv file
                count = len(text.split(delimiter))
                countTuple = (data[0], text, count)
                wordCount.append(countTuple)
                #appending a list of keyword combos
                keywordOccurences.append(filterWords)
                sortedFilterWords = sorted(filterWords)
                sortedFilterWordsStr = ' '.join(sortedFilterWords)
                keywordCombos.append(sortedFilterWordsStr)

                sentence = nlp(text)
                cleanText = []

                #initial clean up of text
                textCleanUp.textCleanup(allWords,sentence, cleanText)

                cleanTextCounter += 1

                if cleanTextCounter%10000==0:
                    print (str(cleanTextCounter) + " tweet texts have been cleaned.")
                #saving tweet data + filtered text
                cleanTextStr = ' '.join(cleanText)
                tweetList = [data[0],data[1], cleanText, data[3]]
                allTweets.append(tweetList)

                stripped = data[2].replace("\n", " ")
                #checking which location does the search note contain
                #appending the visualisation list with location, tweets author and tweet body
                if len(stripped)>2:
                    if "Scotland" in data[6]:
                        locationString = "Scotland"
                    elif "England" in data[6]:
                        locationString = "England"
                    visTuple = (locationString,data[5], stripped)
                    visList.append(visTuple)
                #appending the list of dates
                date, space ,time = data[3].partition(" ")
                dateTuple = (data, date)
                dateList.append(dateTuple)

    print ("There are " +str(totalCount) + " tweets left after filtering.")
    print ("--- --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ---")
    print (" ")            

    #calling the frequencyCount function to split the words in two arrays based on frequency
    textCleanUp.frequencyCount(nlp, allWords, repeatedWords, uniqueWords, allWordsFrequency, fileString)
    #countKeywordOccurences(keywordOccurences)

    #removing all words that have only been mentioned once from tweet texts
    finalTextCount = []
    textCleanUp.removeUniqueWords(uniqueWords, allTweets, finalTweetTexts, finalTextCount)
    print ("--- --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ---")
    print (" ")

    agent_sort.textsByDate(finalTweetTexts,wordCount,counter)

    print ("Texts from "+location+" have been processed.")

#function used to deliver the occurence count of each keyword that has been mentioned along the selected tweets
def countKeywordOccurences(keywordOccurences):
    repeated = []
    unique = []
    allKeywordsFrequency = []
    keywordList = [word for sublist in keywordOccurences for word in sublist]
    textCleanUp.frequencyCount(nlp, keywordList, repeated, unique, allKeywordsFrequency)

connect()
