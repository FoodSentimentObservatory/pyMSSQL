import config
import pymssql
#connecting to database
def connectionToDatabase():
    server = config.dbServer()
    databased = config.databaseName()
    portd = config.databasePort()
    #connection to the database
    conn = pymssql.connect(server,database=databased,port=portd)
    #cursor = conn.cursor()
    print ("Connection to Database successfull")

    return conn

def connectionToDatabaseTest(dbName):
    server = config.dbServer()
    databased = dbName
    portd = config.databasePort()
    #connection to the database
    conn = pymssql.connect(server,database=databased,port=portd)
    #cursor = conn.cursor()
    print ("Connection to Database " +dbName+" was successfull")

    return conn

def closeDbConnection():
    conn = connectionToDatabase.conn
    conn.close()    
#collecting all tweets from all locations for a given search description
def retrieveAllTweets(cursor, searchDescription):
    cursor.execute("SELECT [Post].[Id],[Post].[hasCreator],\
    [Post].[body], [Post].[createdAt],\
    [Post].[platformPostID], [UserAccount].[platformAccountId], \
    [Search].[Note],[Post].[SearchId]\
    FROM [Post]\
    INNER join [UserAccount] ON [UserAccount].[Id]= [Post].[hasCreator]\
    INNER join [Search] ON [Post].[SearchId]=[Search].Id\
    WHERE [Search].[Note] LIKE '%"+ searchDescription +"%' ORDER BY [Post].[createdAt] ASC")

    row = cursor.fetchall()

    return row
#collecting all tweets containing a keyword from a given search
def retrieveTweetsByKeyword(cursor, keyword, searchDescription):
    cursor.execute("SELECT [Post].[Id],[Post].[hasCreator],\
    [Post].[body], [Post].[createdAt],\
    [Post].[platformPostID], [UserAccount].[platformAccountId], \
    [Search].[Note],[Post].[SearchId]\
    FROM [Post]\
    INNER join [UserAccount] on [UserAccount].[Id]= [Post].[hasCreator]\
    INNER join [Search] ON [Post].[SearchId]=[Search].Id\
    WHERE [Post].[body] LIKE '%"+ keyword +"%' AND  [Search].[Note] LIKE '%"+ searchDescription +"%'\
    ORDER BY [Post].[createdAt] ASC ")

    result = cursor.fetchall()
    return result
#collecting all tweets from a given search from a given location
def locationQuery(cursor,searchDescription, location):
     cursor.execute("SELECT [Post].[Id],[Post].[hasCreator],\
     [Post].[body], [Post].[createdAt],\
     [Post].[platformPostID], [UserAccount].[platformAccountId],\
     [Post].[SearchId] \
     FROM [Post] \
     INNER join [Search] ON [Post].[SearchId]=[Search].Id \
     INNER join [UserAccount] ON [UserAccount].[Id]= [Post].[hasCreator]\
     WHERE [Search].[Note] LIKE '%"+ searchDescription +"%' AND [Search].[Note] LIKE '%"+ location +"%'\
     ORDER BY [Post].[createdAt] ASC")
     row = cursor.fetchall()

     return row
#collecting all tweets from a given search from a given location containing a given keyword
def locationQueryKeyword(cursor, keyword,searchDescription, location):
     cursor.execute("SELECT [Post].[Id],[Post].[hasCreator],\
     [Post].[body], [Post].[createdAt], [Post].[platformPostID],\
     [UserAccount].[platformAccountId],[Search].[Note], [Post].[SearchId],\
     [UserAccount].[verified],[UserAccount].[displayName] \
     FROM [Post]\
     INNER join [Search] ON [Post].[SearchId]=[Search].Id\
     INNER join [UserAccount] ON [UserAccount].[Id]= [Post].[hasCreator]\
     WHERE [Search].[Note] LIKE '%"+ searchDescription +"%' AND [Search].[Note] LIKE '%"+ location +"%'\
     AND [Post].[body] LIKE '%"+ keyword +"%'\
     ORDER BY [Post].[createdAt] ASC")
     row = cursor.fetchall()

     return row

def sprintNotesQuery(cursor,dbName):
    cursor.execute("SELECT Distinct [Search].[Note]  FROM [Search]")

    row = cursor.fetchall()

    return row    

