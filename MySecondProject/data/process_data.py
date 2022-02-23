import sys
import pandas as pd
import sqlalchemy

def load_data(messages_filepath, categories_filepath):
    
    # load messages dataset
    messages = pd.read_csv(messages_filepath)
    
    # load categories dataset
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = pd.merge(messages, categories, on="id")
    
    return df


def clean_data(df):
    
    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(";",expand=True)
    
    # select the first row of the categories dataframe
    row = categories.loc[0,:]
    # extract a list of new column names for categories
    # takes everything up to the second to last character of each string with slicing
    category_colnames = row.apply(lambda x: x[:-2]).values
    
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    # Convert category values to just numbers 0 or 1.
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
    
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    # Convert category values to just numbers 0 or 1
    categories["related"] = categories["related"].apply(lambda x: 0 if x ==0 else 1)
    # drop the original categories column from `df`
    df = df.drop(columns = ["categories"])
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis= 1,sort=False)
    
    # drop duplicates
    df = df.drop_duplicates(subset=['message'], keep='last')
    return df


def save_data(df, database_filename):
    engine = sqlalchemy.create_engine('sqlite:///'+ str(database_filename))
    df.to_sql("disastermessages", engine, index=False,if_exists='replace')
    pass  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()