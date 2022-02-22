# Disaster Response Pipelines


## Table of Contents

 * [Project Overview](#project-overview)
 * [Requiremnts](#requiremnts)
 * [File Descriptions](#file-descriptions)
 * [Instructions To Run](#instructions-to-run)
 * [Acknowledgements](#acknowledgements)


## Project Overview
In this project, I try to analyze disaster data to build a model for an API that classifies disaster messages. The dataset containing real messages that were sent during disaster events can be found [here](https://github.com/nguyenduchuyvn/my_nanodegrees-/tree/main/MySecondProject/data). 

I've created a machine learning pipeline to categorize these events. The detail can be found in [here](https://github.com/nguyenduchuyvn/my_nanodegrees-/tree/main/MySecondProject/models).

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
This project has `3 sub-repositories`: 
1. `Data`: That contains 
    - a python script "process_data.py"  that allows to process data 
    - 02 data files to process : disaster_categories.csv   &  disaster_messages.csv 
    - a jupyter notebook was used to do EDA to prepare the process_data.py python script.

2. `Models`: That contains 
    - a python script, train_classifier.py, to run a machine learning pipeline 
    - a jupyter notebook ML Pipeline Preparation was used to do EDA to prepare the train_classifier.py python script.

3. `App`: That contains
    - a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

## Instructions To Run

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

## Acknowledgements
- Thank Udacity for great project 
