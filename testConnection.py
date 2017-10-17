from os import getenv
import pymssql
#Please note that the default MS-SQL port setting is 1433, however in this code
#it is set to dynamic port 49386, To run normally just remove the port=49386 in
#the function call

def connect():
    try:
        
        #if using pymssql
        conn = pymssql.connect(server,database='Gnip-Test',port=1066)
        cursor = conn.cursor()

    
        #if using mssql
        #conn = _mssql.connect(server,user, password,database = 'testing')
        
        #Try to view top 10 agents from the Agent table
        cursor.execute('SELECT TOP 10 [Id], [agentType] FROM [TheDatabase].[dbo].[Agent]')
        #Fetch all agents from database which is < 10 
        row = cursor.fetchall() 
        
    except TypeError as e:
        print (e)
        return None

#if using mssql           
##    except _mssql.MssqlDatabaseException as e:
##        print "The system cannot connect to the Food Database"
##        print(e)
##        return None
    message = "Connected to the database"
    conn.close()
    return message

#Replace server with server name or IP address
server = 'localhost'


connect()
