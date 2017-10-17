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
  
			cursor = sqlQueries.connectionToDatabase()
			filterKeywords= fileFunctions.readKeywordFile()
			#initiating a list for a total count statistics file
			listOfKeywords = [("keyword", "total count", "England", "Scotland")]
			locationSc = "Scotland"
			locationEn = "England" 
			searchQuery = config.searchStringForSqlQuery()

			for word in filterKeywords:
				print ("Search for word '"+word+"' for all locations in the database has begun.")
				resultSc = sqlQueries.locationQueryKeyword(cursor, word,searchQuery, locationSc)
				resultEn = sqlQueries.locationQueryKeyword(cursor, word,searchQuery, locationEn)

				countEn = len(resultEn)
				countSc = len(resultSc)
				count = countEn+countSc
				print ("Search for '"+word+"' has finished. There were "+str(count)+" tweets containing '"+word+"' in the database." )
				print (" ")

				if count>0:
					wordTuple = (word, count, countEn, countSc)
				else:
					wordTuple = (word, count, countEn, countSc)

				listOfKeywords.append(wordTuple)
				print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")	

			fileNameString = "keywordCount"
			fileFunctions.writeCsvFile(listOfKeywords, fileNameString)
			return    
connect()	