from configparser import SafeConfigParser
import sqlQueries
import config
import html

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

def fetchingTweets(cursor, location, searchQuery, keywords):
    #keywords = input("Please enter any keywords for search or press enter to continue: ")
    #keywordsList =keywords.split()
    keywordsList=keywords
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

def fetchingTweetsContainingGroups(cursor,location,searchQuery,listOfGroups):
    row=[]
    print(len(listOfGroups))
    if len(listOfGroups)>1:
        for group in listOfGroups:
            groupRow= groupSearch(cursor, location,searchQuery, group)        
            row.append(groupRow)
    else:
        for group in listOfGroups:
            groupRow= groupSearch(cursor, location,searchQuery, group)
            row.append(groupRow)         
    print("Found a total of "+str(len(row))+" tweets.")    
    return row                        
#function to search for tweets containing a group of keywords
def groupSearch(cursor, location,searchQuery, group):
    print("searching for group:")
    print (group)
    rowL=[]
    groupRow=[]
    #for eah word, fetch all tweets containing the word
    for word in group:
        print (word)
        result = sqlQueries.locationQueryKeyword(cursor, word,searchQuery, location)
        print(len(result))
        for r in result:
            rowL.append(r) 
         
    print("Found "+str(len(rowL))+" total results for the group")    
    #setting a treshhold for filtering so that from all the tweets, we'll only..
    #..get the ones containing all words from the group
    treshhold = len(group)
    print (treshhold)
    listOfTweetIDs = []
    for tweet in rowL:  
                textOr=tweet[2].replace("\n"," ")
                text=html.escape(textOr,quote=True)
                displayName = html.escape(tweet[9],quote=True)
                tweetID = tweet[0]
                count=0       
                alreadySeen=[]
                #for each word in the grop, checking if it exists in the text..
                #if it does, one up the counter and search for the next word in the group
                #if a word appears twice in tweet, we only count it once
                for word in group:
                    if word in tweet[2] and str(word) not in alreadySeen:
                        alreadySeen.append(word)
                        count+=1    
                #once the treshhold is reached and the tweet hasn't been added yet..
                #..add it to a list        
                if count==treshhold and tweetID not in listOfTweetIDs:
                    if tweet[8]==False:
                        verified="False"
                    elif tweet[8]==True:
                        verified="True"    
                    filteredTextTweet=[text,tweet[3],tweet[5],verified,displayName] 
                    listOfTweetIDs.append(tweetID) 
                    groupRow.append(filteredTextTweet)
    print ("Found "+str(len(groupRow))+" tweets containing all words from the group")   
    print ("-------------------------------------S")

    return groupRow