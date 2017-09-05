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
import spacyStopWords


wordCount = [("Id","Text", "Count")]
allWords = []
nlp = spacy.load("en")
repeatedWords = []
uniqueWords = []
allWordsFrequency = []
spacyStopWords.stopWordsList(nlp)
allTexts = []

def articleCleanup(path):
    SKIP_FILES = {'cmds'}
    doc_set = []
    folderName = os.path.basename(os.path.normpath(path))

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
    counter = "text"
    for line in doc_set:
        lineS = str(line.lower())
        sentence = nlp(lineS)
        cleanText = []
        textCleanUp.textCleanup(allWords, sentence, cleanText)
        lineText.append(cleanText)
    textCleanUp.frequencyCount(nlp, allWords, repeatedWords, uniqueWords, allWordsFrequency,folderName)
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

    agent_sort.splitFile(allTexts, folderName)
