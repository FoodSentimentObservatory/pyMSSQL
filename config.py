from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.txt')

searchLocation = parser.get('search-location', 'both')
#defining the search type in the config file
searchDefinitionsGen =  parser.get('search-definitions', 'general')
searchDefinitionsFHIS = parser.get('search-definitions', 'fhis')
searchDefinitionsFHRS= parser.get('search-definitions', 'fhrs')
searchDefinitionsTextFiles = parser.get('search-definitions', 'textFiles')

#defining where the statistics results will be stored based on the type of search defined
def resultPaths():
    path = ""
    if int(searchDefinitionsGen) == 1:
        path = parser.get('result-paths', 'genBoth')
    elif int(searchDefinitionsFHIS) == 1:
        path = parser.get('result-paths', 'fhisBoth')
    elif int(searchDefinitionsFHRS) == 1:
        path = parser.get('result-paths', 'fhrsBoth')
    elif int(searchDefinitionsTextFiles) == 1:
        path = parser.get('result-paths', 'textFiles')
    return path
#getting the path for the raw tweets folder
def rawTweetsPath():
    path = parser.get('result-paths', 'rawTweets')
    return path    
#defining a folder where all processed tweet texts will be saved
def tweetFolders():
    path = parser.get('result-paths', 'alltweets')
    return path
#can be used in case we'd want to specify location manually
def setLocation(location):
    if location.lower() == "scotland":
         parser.set('search-location', 'scotland', '1')
         parser.set('search-location', 'england', '0')
         parser.set('search-location', 'both', '0')
    elif location.lower() == "england":
        parser.set('search-location', 'england', '1')
        parser.set('search-location', 'scotland', '0')
        parser.set('search-location', 'both', '0')
    elif location.lower() == "-":
        parser.set('search-location', 'both', '1')
        parser.set('search-location', 'scotland', '0')
        parser.set('search-location', 'england', '0')

    with open('config.txt', 'w') as configfile:
        parser.write(configfile)

def setTextFileMode(): 
    parser.set('search-definitions', 'textFiles', '1')  
    parser.set('search-definitions', 'general', '0') 
    parser.set('search-definitions', 'fhis', '0') 
    parser.set('search-definitions', 'fhrs', '0')      
#defining what search we'll be looking for within the search query
def searchStringForSqlQuery():

    if int(searchDefinitionsGen)==1:
        searchQuery =parser.get('search-terms', 'genfoodhygiene')
    elif int(searchDefinitionsFHIS)==1:
        searchQuery= parser.get('search-terms', 'fhisdiscourseboth')
    elif int(searchDefinitionsFHRS)==1:
        searchQuery = parser.get('search-terms', 'fhrsdiscourseboth')

    return searchQuery
#defining which keyword file will be used
def keywordFileSelection():

        if int(searchDefinitionsGen)==1:
            path =parser.get('file-paths', 'generaldiscourse')
        elif int(searchDefinitionsFHIS)==1:
            path= parser.get('file-paths', 'fhisdiscourse')
        elif int(searchDefinitionsFHRS)==1:
            path = parser.get('file-paths', 'fhrsdiscourse')

        return path
#collecting database specifications 

def databasePort():
    dbPort = parser.get('db-data', 'port')
    return dbPort

def dbServer():
    server = parser.get('db-data', 'server')
    return server

def getAllDatabases():
    databaseList = parser.items('db-names')
    return databaseList