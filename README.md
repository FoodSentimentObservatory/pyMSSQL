# Processing of Twitter data

Code to pull data from database and process it in different approaches.

## Prerequisites

**Note:** the following steps are for Windows installation, the system hasn't been tested on any other OS yet.

### Required installations

* Python 3.6

* [Spacy](https://spacy.io/docs/usage/)  - see installation description on their website

* pymssql 

```
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql and download the version of pymssql for your machine

(e.g. for a 64 bit machine with Python 3.6 you'll need the **pymssql-2.1.3-cp36-cp36m-win_amd64.whl**)

In command line type **pip install pymssql-2.1.3-cp36-cp36m-win_amd64.whl**
```
### Other required setup

This project works with **Microsoft SQL Server Management Studio** as database environment.

Create a database using the **script.sql** (change the name of the database and the paths towards the MSQLSMS directory on your machine first). Populate the database using the [data-collectors](https://github.com/FoodSentimentObservatory/data-collectors) scripts.

There is a sample config file structure in config.txt. Need to specify result directory paths (see **Result directories**), paths to the keyword files contained in the data folder which already exists in the package and database configuration.

Sample keyword files for filtering and grouping in datasets are available in the data folder.

Before running the code, go to config.txt and set the desired search-definition value to 1.

```
If you want to process general food discourse data, set that search-definition to 1.

The code will then automatically select the needed keyword file, **generalDiscourse.txt**.

It will also select the search term that will be needed to sift through the database and collect only tweets 
from that discourse search.
```

## Running the code

The script can be ran either through main.py by selecting the desired funtionality or through the processing scripts:

### test_sql_login.py 

Can work with all tweets from the database or tweets from a specified keyword or multiple specified keywords. Filters texts, generates statistics and text files to be used by jst.

### test.py

Combines tweets by keyword, filters the texts and generates statistics files for those datasets, files for visualisation and text files in the format used by jst.

**Note:** the script takes a list of keywords and goes through each of them automatically. Unlike in **test_sql_login.py**, here the user can't select a specific keyword. In **test_sql_login.py** the user can search for words that were not part of the original keyword lists.

### articleCleanUp.py 

Used for filtering text files (e.g. articles from newspapers) and generating filtered text results ready for topic extraction.

### raw-tweets.py.

Similar functionality to test.py, however instead of processed texts, this script generates files of raw tweets, matching the order of the texts produced by the test.py.

To run the script, go to the directory of this package on your system in comman line and type the following:

```
main.py 
```

You can run any of the other above mentioned scripts in the same way.

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

* #### Statistics for each keyword set for each location

  * frequency counts of words for each keyword set, counts are done after filtering stop words, urls, numbers and words that only apeared once in the whole dataset

  * count of tweets by date

  * a csv file containing a tweet's original text, word count, filter text and new word count

  * a csv file used for visualisation of tweet contents