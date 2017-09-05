from os import getenv
import pymssql
import csv
import spacy
import re
import sys
from spacy.attrs import ORTH
import numpy
import os
from spacy import en
from operator import itemgetter
from collections import Counter
import textCleanUp
import agent_sort


wordCount = [("Id","Text", "Count")]
allWords = []
nlp = spacy.load("en")
repeatedWords = []
uniqueWords = []
allWordsFrequency = []
newStopWords = ['co', 'couldnt', 'describe', 'eg', 'find', 'found', 'hasnt', 'im', 'ie', 'ltd', 'mill', 'un', 'de', 'rt', 'pm', \
                'hi', 'hello', 'hey', 'pre', 'retweet', 'http', 'htt', 'ht', 'mr', 'ms', 'mrs', 'maybe', 'app', 'ha', 'haha', 'till'\
                'til', 'cv', 'ya', 'vs', 'st', 'dm', 'https']
for stopw in newStopWords:
    en.English.Defaults.stop_words.add(stopw)
notStopWords = ['part', 'again', 'last', 'using', 'almost', 'together', 'cannot', 'well', 'rather', 'without', 'various',\
                'same', 'empty', 'however', 'back', 'against', 'top', 'throughout', 'several', 'nevertheless', 'out', 'quite'\
                'nobody', 'say', 'anything', 'alone', 'whole', 'full', 'first', 'always', 'across', 'least', 'third', 'please'\
                'front', 'nothing', 'less', 'make', 'perhaps', 'behind', 'not', 'enough', 'really','used', 'side', 'move', \
                'none', 'must', 'should', 'many', 'very', 'most', 'regarding', 'few', 'below', 'never', 'over', 'beyond', \
                'show', 'bottom', 'before', 'indeed', 'already', 'down', 'beforehand', 'above','now', 'unless', 'further', 'nowhere',\
                'serious']
for word in en.English.Defaults.stop_words:
    lexeme = nlp.vocab[word]
    if word not in notStopWords:
        lexeme.is_stop = True
    else:
        lexeme.is_stop = False
allTexts = []
def articleCleanup(path):
    SKIP_FILES = {'cmds'}
    doc_set = []

    #reading the files in the folder
    for root, dir_names, file_names in os.walk(path):
            for path in dir_names:
                read_files(os.path.join(root, path))
            for file_name in file_names:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    past_header, lines = False, []
                    f = open(file_path, encoding="latin-1")
                        #reading file and adding each line to list
                    for line in f:
                        doc_set.append(line)
                    f.close()
    #loops through each line of text and removes stop words,urls, punctuation, numbers and other non-alphabetical symbols
    lineText = []
    for line in doc_set:
        lineS = str(line.lower())
        sentence = nlp(lineS)
        cleanText = []
        textCleanUp.textCleanup(allWords, sentence, cleanText)
        lineText.append(cleanText)
    textCleanUp.frequencyCount(nlp, allWords, repeatedWords, uniqueWords, allWordsFrequency)
    i = 0
    allTextsS = []
    #adding each word that has been repeated in the list of all texts
    for line in lineText:
        newLine = []
        for word in line:
            if word not in uniqueWords:
                allTextsS.append(word)
                newLine.append(word)
        allTexts.append(newLine)

    agent_sort.splitFile(allTexts)
