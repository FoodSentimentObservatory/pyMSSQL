# Processing of Twitter data

Code to pull data from database and process it in different approaches.

## Prerequisites

**Note:** the following steps are for Windows installation, the system hasn't been tested on any other OS yet.

### Required installations

* [Python 3.6](https://www.python.org/downloads/)

* [Spacy](https://spacy.io/docs/usage/)  - see installation description on their website

* pymssql 

```
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql and download the version of pymssql for your machine

(e.g. for a 64 bit machine with Python 3.6 you'll need the pymssql-2.1.3-cp36-cp36m-win_amd64.whl)

In command line type pip install pymssql-2.1.3-cp36-cp36m-win_amd64.whl
```
### Other required setup

This project works with **Microsoft SQL Server Management Studio** as database environment.

Create a database using the **script.sql** (change the name of the database and the paths towards the MSQLSMS directory on your machine first). Populate the database using the [data-collectors](https://github.com/FoodSentimentObservatory/data-collectors) scripts.

There is a sample config file structure in config.txt. Need to specify result directory paths (see **Result directories**), paths to the keyword files contained in the data folder which already exists in the package and database configuration.

Sample keyword files for filtering and grouping in datasets are available in the data folder.

Before running the code, go to config.txt and set the desired search-definition value and the relevant sprint-number to 1.

```
If you want to process general food discourse data, in the search-definition tag set `general` to 1 and in sprint-number, set sprintOne to 1.

The code will then automatically select the needed keyword file, generalDiscourse.txt, available the data folder and it will connect to the relevant database.

It will also select the search term that will be needed to sift through the database and collect only tweets 
from that discourse search. In this case from the tag `search-terms` it will select `genfoodhygiene`.
```
#### Sprint 1 database
Relevant discourses: general, fhis and fhrs

#### Sprint 2 database
Relevant discourses: cheese, burgers, experiment three

#### Sprint 3 database
Not conducted yet.

## Running the code

The script can be ran either through main.py by selecting the desired funtionality or through the processing scripts:

### test_sql_login.py 

Can work with all tweets from the database or tweets from a specified keyword or multiple specified keywords. When running the code a prompt will ask you to specify any keywords to search with, either hit enter or type them in a similar format `burger glasgow` and then press enter. The script pulls the desired tweets rom the databse, filters them, generates statistics and text files to be used by jst. 

**Note:** If you search for keywords that are not in the original keyword list, the script will find them and create the above mentioned files, however, at this stage you can't get raw tweets to be used by the summarisation-scripts.

### test.py

Combines tweets by keyword and then by location, filters the texts and generates statistics files for those datasets, files for visualisation and text files in the format used by jst. Those files are generated for both locations separately.

**Note:** the script takes a list of keywords and goes through each of them automatically. Unlike in **test_sql_login.py**, here the user can't select a specific keyword. In **test_sql_login.py** the user can search for words that were not part of the original keyword lists.



### raw-tweets.py.

Similar functionality to test.py, however instead of processed texts, this script generates files of raw tweets, matching the order of the texts produced by the test.py.

To run the script, go to the directory of this package on your system in command line and type the following:

```
main.py 
```

You can run any of the other above mentioned scripts in the same way.

### articleCleanUp.py 

Used for filtering text files (e.g. articles from newspapers) and generating filtered text results ready for topic extraction. Takes as input the path to a folder containing text files (in txt format) that need to be processed.

**Note: ** this script can only be ran through main.py. When prompted to provide a path or hit enter, a path should be provided.

**Note: ** currently for sprint 2 the options for England have been commented out because they were creating confustion in the counts. Need to see what causes that problem.

## Result directories

### Needs directories for: 

* tweet text files results(all search definitions go in the same one with the current config file, however could be useful to add sub-directories for each search definition and send each result to its appropriate search definition dir; this would require modification of the config.txt structure), 

* statistics (within the statistics a separate folder for each search term), 

* raw-tweets (currently automatcally generating folders for the text files within the folder, however, could be useful to consider also splitting the results in search definition sub-directories as well; again would require modification of config.txt structure), 

* texts directory for the text files from the articleCleanUp.py. 

## Result files

All files from **test.py**, **articleCleanUp** and **raw-tweets** are automatically generated and have different relevant names so there is no overwritting. **test_sql_login.py** still generates files with the same name after each turn, so those results need to be saved somewhere else before the code would be ran again with different specifications.

### Types of output

* raw tweets, text files split in folders by keyword

* Statistics for each keyword set for each location

  * frequency counts of words for each keyword set, counts are done after filtering stop words, urls, numbers and words that only apeared once in the whole dataset

  * count of tweets by date

  * a csv file containing a tweet's original text, word count, filter text and new word count

  * a csv file used for visualisation of tweet contents

*  a csv count containing counts of how many tweets containing a given keyword are there after retweet removal, how many of them are from Scotland and how many are from England 

* for each keyword set from a location, a text file is created, which is in a ready to use format for jst, only needs to be copied to the data folder of jst

** Note: ** follow the folder structer from the result-paths tag in the config file, as it makes it easier to differentiate between sprint results.

## After processing

Take jst-ready text files which have names similar to `*keyword_location*_all_texts`, download the [jst](https://github.com/linron84/JST) tool, place text files in its data folder and follow the instructions for running it. 