from configparser import SafeConfigParser
import sqlQueries
import config
import html
import re
import textCleanUp
import json
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

def fetchingTweetsContainingGroups(cursor,location,searchQuery,listOfGroups, fromDate, toDate):
    row=[]
    print(len(listOfGroups))
    if len(listOfGroups)>1:
        for group in listOfGroups:
            groupRow= groupSearch(cursor, location,searchQuery, group,  fromDate, toDate)        
            row.append(groupRow)
    else:
        for group in listOfGroups:
            groupRow= groupSearch(cursor, location,searchQuery, group,  fromDate, toDate)
            row.append(groupRow)         
    print("Found a total of "+str(len(row))+" tweets.")    
    return row                        
#function to search for tweets containing a group of keywords
def groupSearch(cursor, location,searchQuery, group, fromDate, toDate):
    print("searching for group:")
    print (group)
    rowL=[]
    groupRow=[]
    #for eah word, fetch all tweets containing the word
    for word in group:
        print (word)
        result = sqlQueries.locationQueryKeyword(cursor, word,searchQuery, location, fromDate, toDate)
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
                tweetID = tweet[4]
                count=0       
                alreadySeen=[]

                date = tweet[3].rpartition('.')[0]
                #for each word in the grop, checking if it exists in the text..
                #if it does, one up the counter and search for the next word in the group
                #if a word appears twice in tweet, we only count it once
                for word in group:
                    regex = r'\b'+word+'\\b'
                    listL=re.findall(regex,tweet[2].lower())
                    if  len(listL)>0 and str(word) not in alreadySeen:
                        alreadySeen.append(word)
                        count+=1    
                #once the treshhold is reached and the tweet hasn't been added yet..
                #..add it to a list        
                if count==treshhold and tweetID not in listOfTweetIDs:
                    if tweet[8]==False:
                        verified="False"
                    elif tweet[8]==True:
                        verified="True"    
                    filteredTextTweet=[text,date,tweet[5],verified,displayName] 
                    listOfTweetIDs.append(tweetID) 
                    groupRow.append(filteredTextTweet)
    print ("Found "+str(len(groupRow))+" tweets containing all words from the group")   
    print ("-------------------------------------S")

    return groupRow
#main function to get data for each sprint's notes
def getSearchNotes():
    dbSprintOne = config.getDbSprintOne()
    dbSprintTwo = config.getDbSprintTwo()

    sprintOne = "Sprint-1"
    sprintTwo = "Sprint-2"
    #getting the sprint notes for each sprint
    sprintOneNotes = getSprintNotes(dbSprintOne,sprintOne)
    sprintTwoNotes = getSprintNotes(dbSprintTwo,sprintTwo)

    sprintNotesList = [sprintOneNotes,sprintTwoNotes]

    noteList = [item for sprint in sprintNotesList for item in sprint]
    n=5
    newNoteList =[]
    #giving an id that would be used for the creation of radio buttons in the interface
    for note in noteList:
        idstr= "radio"+str(n)
        newNoteTup = (note[0],note[1],note[2],idstr, note[3],note[4],note[5],note[6], note[7], note[8])
        newNoteList.append(newNoteTup)
        n+=1
    #creating a dictionary, key is the sprint    
    i = 1
    dicNotes = textCleanUp.dictionaryGen(newNoteList,i)

    return dicNotes
#helper function to connect to each database, pull the search notes from it and gather all relevant search data
def getSprintNotes(sprintDb, sprint):
    conn = sqlQueries.connectionToDatabaseTest(sprintDb)
    cursor = conn.cursor()
    #query to get all unique notes
    sprintNotes = sqlQueries.sprintNotesQuery(cursor, sprintDb)   
    newSprintNoteList=[]
    alreadySeenNotes = []
    #the result is returned in an odd format, so the following lines extract the
    #relevant parts of the search string - discourse and general location
    for note in sprintNotes:
        #sprint one has some random numbers attached to each search note, 
        #hence select distinct doesn't work on it
        if "(" in note[0]:
            newNoteS = note[0].split("(",1)[0]
            searchNote=newNoteS
            newNoteM = newNoteS.split("-")[-1]
            location = note[0].split(" ",1)[0]
            newNote = location + " -"+newNoteM
        else:
            searchNote=note[0]
            newNoteM = str(note[0]).split("-")[-1] 
            locationS = str(note[0]).split("-")[0]
            location = locationS.split(" ")[0]
            newNote = location + " -"+newNoteM

        
           
        #because of the random numbers mentioned above, after we clean the note string
        #we need to check if we've already encoutered it before, if not, continue with the rest    
        if newNote not in alreadySeenNotes:
            coordinates = getCoordinates(cursor, newNoteM, location)
            print(coordinates) 
            #getting the earliest and the most recent tweet from db and removing the milliseconds
            earliestSearchDate = sqlQueries.getEarliestDate(cursor,newNoteM,location)
            mostRecentDate = sqlQueries.getMostRecentDate(cursor,newNoteM,location)

            dateEarliest = earliestSearchDate.rpartition('.')[0]
            dateRecent = mostRecentDate.rpartition('.')[0]
            #using a function to pull the search keyword strings for each sprint
            keywords = getSprintQueryKeywords(cursor,newNoteM,location)
            count = sqlQueries.getCount(cursor, newNoteM,location)
            countInt = count[0][0]
            countWithCommas = '{0:,}'.format(countInt)
            print(count)
            #for each note we create a tuple containing data to display
            noteTup = (newNote, sprint, location,sprintDb,dateEarliest,dateRecent,keywords,countWithCommas,coordinates)
            newSprintNoteList.append(noteTup)
            alreadySeenNotes.append(newNote)
      
    return newSprintNoteList 
    conn.close()
#function to pull keyword string for search notes from database and put them together
def getSprintQueryKeywords(cursor,note,location):
    keywordQueryList = sqlQueries.getQueryKeywords(cursor, note, location)
    queryList = []
    for query in keywordQueryList:
        newQuery=[]
        editedQuery = []
        check=2
        #making a list of words and removing extra characters
        for word in query:
            wordList=word.split(" OR ")
            charList = ['"','(',')']
            for w in wordList:
                w = textCleanUp.extraCharRemoval(w, charList,check)
                wNew = w.replace("'",' ')
                queryList.append(wNew)
    #sorting list aplhabetically, ignoring whether word starts with capital or small letter            
    sortedEditedQuery = sorted(queryList, key=str.lower)
    queryString = '; '.join(sortedEditedQuery)

    return queryString

def getCoordinates(cursor, newNoteM, location):
        coordinates = sqlQueries.getLocationOfSearch(cursor, newNoteM, location)

        return coordinates