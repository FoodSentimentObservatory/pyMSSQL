from os import getenv
import pymssql
#Please note that the default MS-SQL port setting is 1433, however in this code
#it is set to dynamic port 49386, To run normally just remove the port=49386 in
#the function call

def connect():
    try:
        
        #if using pymssql
        conn = pymssql.connect(server,user, password,database = 'TheDatabase',port=49386)
        cursor = conn.cursor()

        print "Connection to Database successfull"
        #if using mssql
        #conn = _mssql.connect(server,user, password,database = 'testing')
        
        #Try to view top 10 agents from the Agent table
        cursor.execute('SELECT TOP 10 [Id], [agentType] \
        FROM [TheDatabase].[dbo].[Agent]')
        #Fetch all agents from database which is < 10 
        row = cursor.fetchall() 
        for data in row:
            print data
            
    except TypeError as e:
        print (e)
        return None

#if using mssql           
##    except _mssql.MssqlDatabaseException as e:
##        print "The system cannot connect to the Food Database"
##        print(e)
##        return None
    
    conn.close()
    return

#Replace server with server name or IP address
server = 'localhost'
#your SQL username
user = 'username_here'
#your SQL password
password = 'passwordhere'

print "Please wait while the Food system is connecting to database"

connect()

