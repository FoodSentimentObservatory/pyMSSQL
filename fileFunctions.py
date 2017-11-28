import sys
import csv
from configparser import SafeConfigParser
import config
import re
import json

parser = SafeConfigParser()
parser.read('config.txt')


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

def generateJson(listOfDataForVis):
    
    dicList = []
    for row in listOfDataForVis:
            dic = {}
            dic['group']=row[0]
            dic['username']=row[1]
            dic['tweet']=row[2]
            dicList.append(dic)

    jsonFormat =  json.dumps(dicList,ensure_ascii=False).encode('utf8')

    return (jsonFormat)  