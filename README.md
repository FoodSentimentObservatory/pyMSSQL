# Processing of Twitter data

Code to pull data from database and process it in different approaches.

## Prerequisites

There is a sample config file structure in config.txt. Need to specify result directory paths (see **Result directories**), path to data folder that already exists and database configuration.

Sample keyword files for filtering and grouping in datasets are available in the data folder.

Before running the code, go to config.txt and set the desired search-definition value to 1.

```
If you want to process general food discourse data, set that search-definition to 1.

The code will then automatically select the needed keyword file, **generalDiscourse.txt**.

It will also select the search term that will be needed to sift through the database and collect only tweets from that discourse search.
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

## Result directories

### Needs directories for: 

* tweet text files results(all search definitions go in the same one with the current config file, however could be useful to add sub-directories for each search definition and send each result to its appropriate search definition dir; this would require modification of the config.txt structure), 

* statistics (within the statistics a separate folder for each search term), 

* raw-tweets (currently automatcally generating folders for the text files within the folder, however, could be useful to consider also splitting the results in search definition sub-directories as well; again would require modification of config.txt structure), 

* texts directory for the text files from the articleCleanUp.py. 