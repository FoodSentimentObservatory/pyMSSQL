# pyMSSQL
Code to pull data from database and process it in different approaches.
There is a sample config file structure in config.txt.
Sample keyword files for filtering and grouping in datasets are available in the data folder
Before running the code, go to config.txt and set the desired search-definition value to 1
The script can be ran either through main.py or through the processing scripts:
test_sql_login.py, test.py, articleCleanUp.py or raw-tweets.py.
Needs directories for tweet text files results(all search definitions go in the same one with the current config file, however could be useful to add sub-directories for each search definition), statistics (within the statistics a separate folder for each search term), raw-tweets (currently automatcally generating folders for the text files within the folder, however, could be useful to consider also splitting the results in search definition sub-directories as well.) and texts directory for the text files. 