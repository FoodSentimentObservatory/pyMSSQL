import cherrypy
import sqlQueries
import inputManagment
import os
from Cheetah.Template import Template
import datetime
import textCleanUp
import re
from jinja2 import Environment, FileSystemLoader
from itertools import groupby
import html
import collections

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env=Environment(loader=FileSystemLoader(CUR_DIR),
trim_blocks=True)

class ServerConnection(object):
	def __init__(self):
		self.location=""
		self.searchQuery=""	

	@cherrypy.expose
	def index(self):
		
		searchNotesDic = inputManagment.getSearchNotes()

		template = env.get_template('interfaces/index.html')
		#sending the tweets and the group data to html
		return template.render(dicw=searchNotesDic, title="something")
		#eturn open('interfaces/index.html')

	@cherrypy.expose
	def manual(self):
		return open('interfaces/manual.html')	
	
	#direct towards the relevant script
	@cherrypy.expose
	def connectToScript(self, inputTypes, searchnoteID, dbName, start, endof,keywords):
		self.location = searchnoteID.split("-")[0]
		self.searchQuery = searchnoteID.split("- ")[1]
		self.dbName = dbName
		self.startDate = start
		self.endof = endof
		if inputTypes == "specKeywords":
			template = env.get_template('interfaces/keywordSearch.html')
			#sending the tweets and the group data to html
			return template.render(startDate=self.startDate, endDate=self.endof, title="something")

		else:	 
			return inputTypes 	
	#script for keyword searches
	@cherrypy.expose	
	def keywordSearch(self, group, groups, checkName,fromDate,toDate):			
			conn = sqlQueries.connectionToDatabaseTest(self.dbName)	
			cursor = conn.cursor()
			print(self.dbName)
			print (self.location)
			print (self.searchQuery)
			print (fromDate)
			print (toDate)
			print (group)
			listOfGroups=[]
			listOfTweets=[]
			#checking if there's only one or multiple keyword groups
			if isinstance(group, str):
				listofwords = group.split(",")
				listOfGroups.append(listofwords)
			else:
				for g in group:
					singleGroup = g.split(",")
					print(singleGroup)
					listOfGroups.append(singleGroup)
			#kinda pointless check but might be useful at a later stage....or not			
			if  len(group)>0:
				countOfGroups = len(listOfGroups)
				#getting all tweets with the specified keywords, the result is a list of lists, tweets are grouped in lists by keyword groups
				print(listOfGroups)
				tweets=inputManagment.fetchingTweetsContainingGroups(cursor,self.location,self.searchQuery,listOfGroups, fromDate, toDate)
				i=0
				tweetList=[]
				groupList = []
				#for each group of tweets (all tweets fetched for one group of keywords)
				for groupOfTweets in tweets:
					numberOfTweets = len(groupOfTweets)
					if len(listOfGroups)>1:
						strGroupOfTweets = ''.join(group[i])
						frequentWords = textCleanUp.frequencyCount(groupOfTweets,group[i])
					else:
						strGroupOfTweets = ''.join(group)	
						frequentWords = textCleanUp.frequencyCount(groupOfTweets,group)
					noCommaGroupOfTweets = strGroupOfTweets.replace(',','')
					#getting the most frequent words in that group
					
					
					#sending to html the keyword group name, ID, number of tweets in it and a list of the most frequent words		
					groupTup = (noCommaGroupOfTweets, strGroupOfTweets,i,numberOfTweets,frequentWords, groupOfTweets)
					groupList.append(groupTup)
					i+=1

					for tweet in groupOfTweets:
						tweetL = list(tweet)
						#making links clickable
						text = textCleanUp.clickableLinks(tweetL[0])
						tweetL.append(text)
						tweetL.append(noCommaGroupOfTweets)
						#sending the tweets to a list
						tweetList.append(tweetL)

				index=6
				dicw = textCleanUp.dictionaryGen(tweetList,index)

			template = env.get_template('interfaces/results.html')
			conn.close()
			#sending the tweets and the group data to html
			return template.render(dicw=dicw, title="something", groupList=groupList, i=0)

	@cherrypy.expose	
	def frequentKeywordSearch(self,group, tweets, word,groupIdStr,groupOriginalName):
		newGroups = []
		firstwordList =[]
		#the tweets list and the tuples of frequent keywords are returned as strs instead of lists..
		#..however, they do look like lists, so we need to strip them from the list chars and split them
		tweetsList=tweets.split("], [")
		tweetDataList=[]
		tweetDataListNoHtmlTags=[]
		for tweet in tweetsList:
			charList=['[[',']]','\n']
			check=1
			cleanTweet=textCleanUp.extraCharRemoval(tweet, charList,check)
			tweetData = cleanTweet.split("', '")
			text=html.escape(tweetData[0],quote=True)
			displayName = html.escape(tweetData[4],quote=True)
			newText = textCleanUp.clickableLinks(text)
			#making two lists, one that will be used for content and one for the hidden input field
			#difference is that the one for the hidden field doesn't contain html tags
			dataWithNoHtmlTags = [text,tweetData[1],tweetData[2],tweetData[3],displayName]
			filteredTweetData=[newText,tweetData[1],tweetData[2],tweetData[3],tweetData[4]]
			tweetDataList.append(filteredTweetData)
			tweetDataListNoHtmlTags.append(dataWithNoHtmlTags)
		#splitting the freqword str into a list
		groupListL=group.split("), (")
		cleanGroupList=[]
		for groups in groupListL:
			charList=['\'','[',']','(',')']
			check=0
			groups=textCleanUp.extraCharRemoval(groups, charList,check)
			groupTup = groups.split(", ")		
			cleanGroupList.append(groupTup[1])

		for tweet in tweetDataList:
			if word in tweet[0].lower():
				textCleanUp.addTweetToNewGroupsList(word,tweet,groupIdStr,newGroups)

		#searching if a frequent word is in a tweet			
		for freqWord in cleanGroupList:
			if freqWord!=word:
				for tweet in tweetDataList:
					if freqWord in tweet[0].lower():
						textCleanUp.addTweetToNewGroupsList(freqWord,tweet,groupIdStr,newGroups)
		#making a dictionary by frequent word				
		index=5
		dicw = textCleanUp.dictionaryGen(newGroups,index)
		i=0
		groupList=[]
		od = collections.OrderedDict(sorted(dicw.items()))
		for key, value in od.items():
			numberOfTweets=len(value)
			groupId=groupIdStr+key
			groupString=groupOriginalName+","+key
			frequentWords = textCleanUp.frequencyCount(value,groupString)
			listForInputValues=[]
			for tweet in tweetDataListNoHtmlTags:
				if key in tweet[0].lower():
					listForInputValues.append(tweet)
			groupTup = (key, groupString,i,numberOfTweets,frequentWords, listForInputValues)
			groupList.append(groupTup)
			i+=1

		template = env.get_template('interfaces/freqResults.html')
		#sending the tweets and the group data to html
		return template.render(dicw=od, groupOriginalName=groupOriginalName, groupList=groupList, word=word)	
		

if __name__ == '__main__':

	conf = {
		'/': {
			'tools.sessions.on': True,
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './public'
		}
	}

	cherrypy.quickstart(ServerConnection(), '/', conf)

