import sys
import csv
import config
import re

def readKeywordFile():
    pathk = config.keywordFileSelection()
    keywordFile = open(pathk, "r")
    filterKeywordList = [line.split(", ") for line in keywordFile.readlines()]
    filterKeywordsUnsorted = [item.lower() for sublist in filterKeywordList for item in sublist]
    filterKeywords=sorted(filterKeywordsUnsorted)

    filterKeywordsStr = ', '.join(filterKeywords)
    print (filterKeywordsStr)
    print ("--- --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- --- --- --- --- ------ --- --- --- --- --- ---")
    print (" ")

    return filterKeywords

def writeCsvFile(tupleList, fileNameString):
    removedSpaces = fileNameString.replace(" ","_")
    path = config.resultPaths()
    with open('%s/%s.csv'%(path,removedSpaces),'w',newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(tupleList)

    print ("A spreadsheet "+fileNameString+" has been generated.")

def writeTxtFrequencyFile(listOfWords, fileNameString,counter):
    path = config.resultPaths()
    file = open("%s/%s_%s.txt"%(path,counter,fileNameString), "w", encoding = 'utf-8')
    for word in listOfWords:
        file.write("%s\n" %word)
    file.close()
