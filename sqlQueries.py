import config
import pymssql
#connecting to database
def connectionToDatabase():
    server = config.dbServer()
    databased = config.databaseName()
    portd = config.databasePort()
    #connection to the database
    conn = pymssql.connect(server,database=databased,port=portd)
    cursor = conn.cursor()
    print ("Connection to Database successfull")

    return cursor

def closeDbConnection():
    conn = connectionToDatabase.conn
    conn.close()    
#collecting all tweets from all locations for a given search description
def retrieveAllTweets(cursor, searchDescription):
    cursor.execute("SELECT [Sprint-1].[dbo].[Post].[Id],[Sprint-1].[dbo].[Post].[hasCreator],\
    [Sprint-1].[dbo].[Post].[body], [Sprint-1].[dbo].[Post].[createdAt],\
    [Sprint-1].[dbo].[Post].[platformPostID], [Sprint-1].[dbo].[UserAccount].[platformAccountId], \
    [Sprint-1].[dbo].[Search].[Note],[Sprint-1].[dbo].[Post].[SearchId]\
    FROM [Sprint-1].[dbo].[Post]\
    INNER join [Sprint-1].[dbo].[UserAccount] ON [Sprint-1].[dbo].[UserAccount].[Id]= [Sprint-1].[dbo].[Post].[hasCreator]\
    INNER join [Sprint-1].[dbo].[Search] ON [Sprint-1].[dbo].[Post].[SearchId]=[Sprint-1].[dbo].[Search].Id\
    WHERE [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ searchDescription +"%' ORDER BY [Sprint-1].[dbo].[Post].[createdAt] ASC")

    row = cursor.fetchall()

    return row
#collecting all tweets containing a keyword from a given search
def retrieveTweetsByKeyword(cursor, keyword, searchDescription):
    cursor.execute("SELECT [Sprint-1].[dbo].[Post].[Id],[Sprint-1].[dbo].[Post].[hasCreator],\
    [Sprint-1].[dbo].[Post].[body], [Sprint-1].[dbo].[Post].[createdAt],\
    [Sprint-1].[dbo].[Post].[platformPostID], [Sprint-1].[dbo].[UserAccount].[platformAccountId], \
    [Sprint-1].[dbo].[Search].[Note],[Sprint-1].[dbo].[Post].[SearchId]\
    FROM [Sprint-1].[dbo].[Post]\
    INNER join [Sprint-1].[dbo].[UserAccount] on [Sprint-1].[dbo].[UserAccount].[Id]= [Sprint-1].[dbo].[Post].[hasCreator]\
    INNER join [Sprint-1].[dbo].[Search] ON [Sprint-1].[dbo].[Post].[SearchId]=[Sprint-1].[dbo].[Search].Id\
    WHERE [Sprint-1].[dbo].[Post].[body] LIKE '%"+ keyword +"%' AND  [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ searchDescription +"%'\
    ORDER BY [Sprint-1].[dbo].[Post].[createdAt] ASC ")

    result = cursor.fetchall()
    return result
#collecting all tweets from a given search from a given location
def locationQuery(cursor,searchDescription, location):
     cursor.execute("SELECT [Sprint-1].[dbo].[Post].[Id],[Sprint-1].[dbo].[Post].[hasCreator],\
     [Sprint-1].[dbo].[Post].[body], [Sprint-1].[dbo].[Post].[createdAt],\
     [Sprint-1].[dbo].[Post].[platformPostID], [Sprint-1].[dbo].[UserAccount].[platformAccountId],\
     [Sprint-1].[dbo].[Post].[SearchId] \
     FROM [Sprint-1].[dbo].[Post] \
     INNER join [Sprint-1].[dbo].[Search] ON [Sprint-1].[dbo].[Post].[SearchId]=[Sprint-1].[dbo].[Search].Id \
     INNER join [Sprint-1].[dbo].[UserAccount] ON [Sprint-1].[dbo].[UserAccount].[Id]= [Sprint-1].[dbo].[Post].[hasCreator]\
     WHERE [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ searchDescription +"%' AND [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ location +"%'\
     ORDER BY [Sprint-1].[dbo].[Post].[createdAt] ASC")
     row = cursor.fetchall()

     return row
#collecting all tweets from a given search from a given location containing a given keyword
def locationQueryKeyword(cursor, keyword,searchDescription, location):
     cursor.execute("SELECT [Sprint-1].[dbo].[Post].[Id],[Sprint-1].[dbo].[Post].[hasCreator],\
     [Sprint-1].[dbo].[Post].[body], [Sprint-1].[dbo].[Post].[createdAt], [Sprint-1].[dbo].[Post].[platformPostID],\
     [Sprint-1].[dbo].[UserAccount].[platformAccountId],[Sprint-1].[dbo].[Search].[Note], [Sprint-1].[dbo].[Post].[SearchId] \
     FROM [Sprint-1].[dbo].[Post]\
     INNER join [Sprint-1].[dbo].[Search] ON [Sprint-1].[dbo].[Post].[SearchId]=[Sprint-1].[dbo].[Search].Id\
     INNER join [Sprint-1].[dbo].[UserAccount] ON [Sprint-1].[dbo].[UserAccount].[Id]= [Sprint-1].[dbo].[Post].[hasCreator]\
     WHERE [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ searchDescription +"%' AND [Sprint-1].[dbo].[Search].[Note] LIKE '%"+ location +"%'\
     AND [Sprint-1].[dbo].[Post].[body] LIKE '%"+ keyword +"%'\
     ORDER BY [Sprint-1].[dbo].[Post].[createdAt] ASC")
     row = cursor.fetchall()

     return row
