# Disaster Response Pipelines


## Table of Contents
 * [Project Motivation](#project-motivation)
 * [Requiremnts](#Requiremnts)
 * [File Descriptions](#file-descriptions)
 * [Components](#components)
 * [Acknowledgements](#licensing-authors-acknowledgements-etc)
 *
## Project Overview
In this project, I try to analyze disaster data to build a model for an API that classifies disaster messages. The dataset containing real messages that were sent during disaster events can be found here[https://github.com/nguyenduchuyvn/my_nanodegrees-/tree/main/MySecondProject/data]. 

I've created a machine learning pipeline to categorize these events. The detail can be found in here[https://github.com/nguyenduchuyvn/my_nanodegrees-/tree/main/MySecondProject/models].

Finally, this project also has a web app where an emergency worker can input a new message and get classification results in several categories


## Requiremnts
This project should be run with these following libraries
- numPy
- pandas
- nltk
- plotly
- sklearn
- flask
- sqlalchemy
- pickle

## File Descriptions
This project has 3 sub-repositories: 
1. Data 
That contains the python script "process_data.py"  that allows to:

- Loads the messages and categories datasets
- Merges the two datasets
- Cleans the data
- Stores it in a SQLite database

A jupyter notebook was used to do EDA to prepare the process_data.py python script.

2. ML Pipeline
A Python script, train_classifier.py, writes a machine learning pipeline that:

Loads data from the SQLite database
Splits the dataset into training and test sets
Builds a text processing and machine learning pipeline
Trains and tunes a model using GridSearchCV
Outputs results on the test set
Exports the final model as a pickle file
A jupyter notebook ML Pipeline Preparation was used to do EDA to prepare the train_classifier.py python script.

3. Flask Web App
The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. The outputs are shown below:

## Acknowledgements
- Thank Udacity for great project 
