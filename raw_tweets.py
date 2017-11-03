import pymssql
import sys
import os
from itertools import groupby
from operator import itemgetter
import sqlQueries
import textCleanUp
import fileFunctions
import config
import inputManagment
import spacy
from spacy import en

nlp = spacy.load("en")
#this function works in a similar manner to test.py, however, instead of processing the tweet texts,
#it generates file with the raw tweet bodies
def connect():
        cursor = sqlQueries.connectionToDatabase()

        filterKeywords= fileFunctions.readKeywordFile()
        searchQuery = config.searchStringForSqlQuery()

        locationSc = "Scotland"
        locationEn = "England" 
        print("Generation of text files of raw tweets for summarisation")
        print ("--- --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ---")
        print (" ")

        for word in filterKeywords:
      
                #print ("Search for word '"+word+"' for all locations in the database has begun.")

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
                #count = countEn+countSc
                #print ("Search for '"+word+"' has finished. There were "+str(countSc)+" tweets containing '"+word+"' in the database." )
                #print (" ")
                if countSc>0:
                    rowSc = textCleanUp.removeDupsAndRetweets(resultSc, locationSc)
                    #rowEn = textCleanUp.removeDupsAndRetweets(resultEn, locationEn)
                    #rowEnCount = len(rowEn)
                    rowScCount = len(rowSc)
                    #countAllUniques = rowEnCount + rowScCount
                    #print ("There are a total of "+str(rowScCount)+" from Scotland.")
                    #print (" ")
                    
                    print(word)
                    #for r in rowSc:
                        #print(r[2])
                        
                    textGen(rowSc, locationSc, word)
                    #textGen(rowEn, locationEn, word)
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")    

def textGen(sortedRowS, location, word): 
        path = config.rawTweetsPath()
        directory = path+word
        #if the directory doesn't exist, create one
        if not os.path.exists(directory):
            os.makedirs(directory)

        compare = len(sortedRowS)
        wordCount = 0
        i = 1
        n = 0
        tweetText = []
        totalCount = 0
        numberOfLines=0
        for tweet in sortedRowS:
                filterWords = []
                text = tweet[2].lower()
                check = 1
                #check = textCleanUp.searchForKeywordCombos(filterKeywords, text, filterWords, nlp)
                if check == 1:
                    n += 1
                    numberOfLines+=1
                    totalCount+=1
                    delimiter = " "
                    stripped = text.replace("\n", " ")
                    addCount = len(text.split(delimiter))
                    print(stripped)
                    #print ("---------------------------------------------------------")
                    tweetText.append(stripped)
                    wordCount = wordCount + addCount
                    if wordCount >=500 or n==compare:
                        
                        #print(n)
                        #print(compare)
                        wordCount = 0
                        file = open("%s/%s_texts_%s.txt" %(directory,i, location), "w", encoding = "utf-8")
                        file.write ("<d_%s> %s\n" %(i,numberOfLines))
                        for line in tweetText:
                            lineS = ''.join(line)
                            file.write("%s\n" %lineS)
                        file.close()
                        tweetText.clear()
                        i += 1
                        numberOfLines=0
        #print ("There is a total of "+ str(totalCount)+ " tweets, containing "+word+" that have been saved to files for "+location+".")


connect()
