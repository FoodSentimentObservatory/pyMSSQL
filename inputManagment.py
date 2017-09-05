from configparser import SafeConfigParser
import sqlQueries
import config

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
    if len(keywords) !=0:

        counter = '_'.join(keywordsList)
        rowL = []

        stopCount = 0
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
    #if no keywords have been specified, fetch all tweets from the database
    else:
        stopCount = 0
        if len(location)!=0:
            row = sqlQueries.locationQuery(cursor,searchQuery,location)
        else:
            row = sqlQueries.retrieveAllTweets(cursor,searchQuery)

    return row
