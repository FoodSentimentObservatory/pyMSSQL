from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.txt')

sprintOne = parser.get('sprint-number', 'SprintOne')
sprintTwo = parser.get('sprint-number', 'SprintTwo')
sprintThree = parser.get('sprint-number', 'SprintThree')

def searchDefinition():

    if int(sprintOne)==1:

        #searchLocation = parser.get('search-location', 'both')
        #defining the search type in the config file
        searchDefinitionsGen =  parser.get('search-definitions', 'general')
        searchDefinitionsFHIS = parser.get('search-definitions', 'fhis')
        searchDefinitionsFHRS= parser.get('search-definitions', 'fhrs')
        searchDefinitionsTextFiles = parser.get('search-definitions', 'textFiles')

        if int(searchDefinitionsGen)==1:
            sprintDefinition = "sprint1Gen"
        elif int(searchDefinitionsFHIS) == 1:
            sprintDefinition = "spint1fhis"
        elif int(searchDefinitionsFHRS) == 1:  
           sprintDefinition = "spint1fhrs"
        elif int(searchDefinitionsTextFiles) == 1:
            sprintDefinition = "spint1texts"  

        return sprintDefinition

    elif int(sprintTwo)==1:
        searchDefinitionCheese =  parser.get('search-definitions', 'cheese') 
        searchDefinitionBurgers =  parser.get('search-definitions', 'burgers')
        searchDefinitionExperimentThree =  parser.get('search-definitions', 'experimentThree') 

        if int(searchDefinitionCheese)==1:
            sprintDefinition = "cheese"
        elif int(searchDefinitionBurgers)==1:
            sprintDefinition = "burgers"
        elif int(searchDefinitionExperimentThree)==1:
            sprintDefinition = "experimentThree"

        return sprintDefinition    

    elif int(sprintThree)==1:
        print("There's no data for this experiment yet, please set another sprint value to one.")
        return                            

#defining where the statistics results will be stored based on the type of search defined
def resultPaths():
    sprintDefinition = searchDefinition()
    path = ""
    if sprintDefinition == "sprint1Gen":
        path = parser.get('result-paths', 'genBoth')
    elif sprintDefinition == "sprint1fhis":
        path = parser.get('result-paths', 'fhisBoth')
    elif sprintDefinition == "sprint1fhrs":
        path = parser.get('result-paths', 'fhrsBoth')
    elif sprintDefinition == "sprint1texts":
        path = parser.get('result-paths', 'textFiles')
    elif  sprintDefinition == "cheese":
        path = parser.get('result-paths', 'cheeseStats')
    elif  sprintDefinition == "burgers":
        path = parser.get('result-paths', 'burgersStats')
    elif  sprintDefinition == "experimentThree":
        path = parser.get('result-paths', 'experimentThreeStats')            
    return path
#getting the path for the raw tweets folder
def rawTweetsPath():
    sprintDefinition = searchDefinition()
    if sprintDefinition=="sprint1Gen" or sprintDefinition=="sprint1fhis" or sprintDefinition=="sprint1fhrs":
        path = parser.get('result-paths', 'rawTweets')
    elif sprintDefinition == "cheese":
        path = parser.get('result-paths','rawCheeseTweets')
    elif sprintDefinition == "burgers":
        path = parser.get('result-paths', 'rawBurgersTweets')
    elif sprintDefinition == "experimentThree":
        path = parser.get('result-paths', 'experimentThreeRawTweets')            
    return path    
#defining a folder where all processed tweet texts will be saved
def tweetFolders():
    sprintDefinition = searchDefinition()
    if sprintDefinition=="sprint1Gen" or sprintDefinition=="sprint1fhis" or sprintDefinition=="sprint1fhrs":
        path = parser.get('result-paths', 'alltweets')
    elif sprintDefinition == "cheese":
        path = parser.get('result-paths','cheeseTweets')
    elif sprintDefinition == "burgers":
        path = parser.get('result-paths', 'burgersTweets')
    elif sprintDefinition == "experimentThree":
        path = parser.get('result-paths', 'experimentThreeTweets')     
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
    sprintDefinition = searchDefinition()
    if sprintDefinition=="sprint1gen":
        searchQuery =parser.get('search-terms', 'genfoodhygiene')
    elif sprintDefinition=="sprint1fhis":
        searchQuery= parser.get('search-terms', 'fhisdiscourseboth')
    elif sprintDefinition=="sprint1fhrs":
        searchQuery = parser.get('search-terms', 'fhrsdiscourseboth')
    elif sprintDefinition=="cheese":
        searchQuery = parser.get('search-terms', 'cheeseTerm')
    elif sprintDefinition=="burgers":
        searchQuery = parser.get('search-terms', 'burgersTerm')
    elif sprintDefinition=="experimentThree":
        searchQuery = parser.get('search-terms', 'experimentThreeTerm')     

    return searchQuery
#defining which keyword file will be used
def keywordFileSelection():
        sprintDefinition = searchDefinition()
        if sprintDefinition=="sprint1gen":
            path =parser.get('file-paths', 'generaldiscourse')
        elif sprintDefinition=="sprint1fhis":
            path= parser.get('file-paths', 'fhisdiscourse')
        elif sprintDefinition=="sprint1fhrs":
            path = parser.get('file-paths', 'fhrsdiscourse')
        elif sprintDefinition=="cheese":
            path = parser.get('file-paths', 'cheeseFile')
        elif sprintDefinition=="burgers":
            path = parser.get('file-paths', 'burgerFile')
        elif sprintDefinition=="experimentThree":
            path = parser.get('file-paths', 'experimentThreeFile')        
        return path
#collecting database specifications 
def databaseName():
    sprintDefinition = searchDefinition()
    if sprintDefinition=="sprint1Gen" or sprintDefinition=="sprint1fhis" or sprintDefinition=="sprint1fhrs":
        database = parser.get('db-data', 'dbSprintOne')
    elif sprintDefinition=="cheese" or sprintDefinition=="burgers" or sprintDefinition=="experimentThree": 
        database = parser.get('db-data', 'dbSprintTwo')

    return database

def databasePort():
    dbPort = parser.get('db-data', 'port')
    return dbPort

def dbServer():
    server = parser.get('db-data', 'server')
    return server
