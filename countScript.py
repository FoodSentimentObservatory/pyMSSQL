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
			filterKeywords= fileFunctions.readKeywordFile()
			#initiating a list for a total count statistics file
			listOfKeywords = [("keyword", "Scotland")]
			locationSc = "Scotland"
			locationEn = "England" 
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
				#count = countEn+countSc
				print ("Search for '"+word+"' has finished. There were "+str(countSc)+" tweets containing '"+word+"' in the database." )
				print (" ")

				wordTuple = (word, countSc)
			
				listOfKeywords.append(wordTuple)
				print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")	

			fileNameString = "keywordCount"
			fileFunctions.writeCsvFile(listOfKeywords, fileNameString)
			return    
connect()	