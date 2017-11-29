# Processing of Twitter data

Integrated interface for displaying results from the database. 

** Note: ** if you need to use the console application with its functionalities, use it from the master branch, as the code here is still under development in order to interact with the interface, so some of the functions had to be changed they won't work in console environment.

## Prerequisites

**Note:** the following steps are for Windows installation, the system hasn't been tested on any other OS yet.

### Required installations

* [Python 3.6](https://www.python.org/downloads/)

* [Spacy](https://spacy.io/docs/usage/)  - see installation description on their website

* pymssql 


```
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql and download the version of pymssql for your machine

(e.g. for a 64 bit machine with Python 3.6 you'll need the pymssql-2.1.3-cp36-cp36m-win_amd64.whl)

In command line, navigate to the folder that stores the wheel and type pip install pymssql-2.1.3-cp36-cp36m-win_amd64.whl
```

* [CherryPy](http://cherrypy.org/)
```
pip install cherrypy
```

* Jinja2
```
Go to http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute and donload the version of jinja2 to that has the filename
Jinja2-2.9.6-py2.py3-none-any.whl . In command line navigate to the folder that stores the wheel and type the following:
pip install Jinja2-2.9.6-py2.py3-none-any.whl
```

* [ScatterText](https://github.com/JasonKessler/scattertext)
```
pip install scattertext
```

### Other required setup

This project works with **Microsoft SQL Server Management Studio** as database environment.

Create a database using the **script.sql** (change the name of the database and the paths towards the MSQLSMS directory on your machine first). Populate the database using the [data-collectors](https://github.com/FoodSentimentObservatory/data-collectors) scripts.

Configuration of database and search terms now all done through the interface, no need to touch the config file.

## Running the code

As mentioned in the begining, this branch's main purpose is for interface development. For text file generation and csv file generation, please refer to the code in the main branch.

In order to access the interface, in commandline, navigate to the folder containing cherryPyTestConnection.py and run that file.
This will start the server and that script will take care of all tasks. Open a browser (the interface has been tested with Firefox and Chrome so far and it's working fine), go to `http://localhost:8080/index`. There you should find the home page. For navigating yourself through the web app, there is a short manual that can be accessed through the menu bar.

