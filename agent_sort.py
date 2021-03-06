from itertools import groupby
import sys
import os
import config
from configparser import SafeConfigParser

#function to split text files into smaller text files for topic analysis
def splitFile(texts, folderName):
    textFile = []
    count = 0
    i = 0
    n=0
    path = config.resultPaths()
    for line in texts:
        lineS = ' '.join(line)
        textFile.append(lineS)
        lineCount = len(line)
        count = count + lineCount
        n+=1
        if count >=300:
            count = 0
            file = open("%s/%s_%s_texts.txt" %(path,folderName,i), "w")
            file.write("<d_%s> %s\n" %(i,n))
            for text in textFile:
                if text != "":
                    file.write("%s\n" %text)
            file.close()
            textFile.clear()
            i += 1
            n=0
    print (str(i) + " files have been created.")

#creating a file of processed tweets ordered by date, which is split into 'documents'.. 
#..using as threshold for the document length the original word count of the tweets..
#..each document must start with a line in format: <document_label> document_line_count
def textsByDate(tweets, origCount, counter):
    print ("Begining to generate text files of tweets ordered by date. ")
    count = len(tweets)
    wordCount = 0
    tweetText = []
    n=0
    i = 1
    fileCounter = 0
    #opening a file to store all texts together
    path = config.tweetFolders()

    with open("%s/%s_all_texts.txt" %(path,counter), "w", encoding = 'utf-8') as f:
        for tweet in tweets:
            n +=1
            tweetID = tweet[0]
            addCount = 0
            for tup in origCount:
                if tup[0]==tweetID:
                    addCount = tup[2]
            text = tweet[2]
            tweetText.append(text)
            wordCount += addCount

            if wordCount >=500 or n == count:
                wordCount = 0
                
                f.write("<d_%s> %s\n" %(i,n))
                for line in tweetText:
                     if len(line) == 0:
                         lineS = " "
                     else:
                         lineS = ' '.join(line)
                     
                     f.write("%s\n" %lineS)
                tweetText.clear()
                i += 1
                n=0

    print ("A text file with all processed tweets for word '"+counter+"' has been created.")
    
#currently not in use as we don't have enough tweets from the same users in order to group them..
#..by authors, keeping it in case, needs to be redone though as it's producing results..
#..in the required format
def textsByAgent(tweetsList, origCount):
    print ("Begining to generate text files of tweets grouped by agent and ordered by date. ")
    dicw ={}
    f = lambda x: x[1]
    for key, group in groupby(sorted(tweetsList, key=f), f):
        dicw[key] = list(group)
    for key, value in dicw.items():
        wordCount = 0
        tweets = sorted(value, key=lambda tweet: tweet[3])
        tweetText = []
        count = len(tweets)
        tweetIndex = 0
        i = 0

        for tweet in tweets:
             tweetID = tweet[0]
             addCount = 0
             #searching for the original number of words of the tweet
             for tup in origCount:
                 if tup[0]== tweetID:
                    addCount = tup[2]
             text = tweet[2]
             tweetText.append(text)
             #counting based on the original count values
             wordCount = wordCount + addCount
             #if count is over 400 or the last tweet from an agent has been reached,
             #save the current list of texts in a file and rstart the count
             if wordCount >= 500 or tweetIndex == count - 1:
                 wordCount = 0
                 file = open("./need_to_define_a_path_if_used/%s_%s_texts.txt" %(key,i), "w", encoding='utf-8')
                 file.write("<d_%s_%s>\n" %(key,i))
                 for line in tweetText:
                     if len(line) == 0:
                         lineS = " "
                     else:
                         lineS = ' '.join(line)
                     file.write("%s\n" %lineS)
                 file.close()
                 tweetText.clear()
                 i += 1
             tweetIndex +=1
        print (str(i)+" files have been generated for this agent.")
