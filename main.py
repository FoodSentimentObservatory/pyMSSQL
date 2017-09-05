import sys
import os
import config
def mainCall():
    task = input("Please provide a directory for text files to be cleaned up or press enter to connect to database: ")
    if len(task) > 0:
        config.setTextFileMode()
        import articleCleanUp
        articleCleanUp.articleCleanup(task)
    else:
        taskDB = input("For text generation on all tweets type 'all'; for text generation based on keyword occurence type 'keywords'\
        for text generation of raw tweets type 'raw': ")
        taskSelection(taskDB)

def taskSelection(taskDB):
    if taskDB== 'all':
        import test_Sql_Login
    elif taskDB=='keywords':
        import test
    elif taskDB== 'raw':
        import raw_tweets    


mainCall()
