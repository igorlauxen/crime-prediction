# Pandas is used for data manipulation
import pandas as pd
import numpy as np
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split

from DateFormatter import DateFormatter
from TextFormatter import TextFormatter
from BooleanFormatter import BooleanFormatter

# Without it pandas truncate the columns when I display =(
# https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

dateFormatter = DateFormatter()
textFormatter = TextFormatter()
booleanFormatter = BooleanFormatter()

class DataPreparator:
  def prepare(self, dataframe): 
    # I may review this
    # depending on the granularity of these properties
    # I may leave one with the assumption of the proximity of crimes
    # Removing Location Description because its description varies A LOT
    # Removing Description because it has a lot of values as well. I may consider this to be re-add
    dropped_columns = [
      "Description", "Location Description", # I may consider reusem these columns
      "District", "Ward", "Community Area", "Location","Block",# I may consider reusem these columns
      "IUCR", "Beat", "FBI Code", "X Coordinate", "Y Coordinate", "Updated On", "Case Number"]

    # remove the following columns
    # based on https://www.geeksforgeeks.org/python-delete-rows-columns-from-dataframe-using-pandas-drop/
    dataframe.drop(dropped_columns, axis = 1, inplace = True)
    # check how the data looks like after changes
    #print("Depois das mudanças")
    #print(dataframe.head(5))
    #print("Quantas entradas existem?")
    #print(len(dataframe.index))

    # drop rows that are inconsistent
    # https://stackoverflow.com/questions/44548721/remove-row-with-null-value-from-pandas-data-frame/44548976
    print("\n\nRemover dados inconsistentes: qualquer coisa com null")
    crime_df = dataframe.dropna(how='any',axis=0) 
    #print("Quantas entradas existem apos limpeza dos dados?")
    #print(len(crime_df.index))

    # random forest seems to expect all columns to be numbers
    # as described in here: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
    # due do this I need to convert the string columns to be something meaninful to the RF
    # Non number columns: Primary Type, Description, Location Description, Arrest, Domestic, Date

    crime_df = dateFormatter.format(crime_df)

    #print("Como ficou o dataframe após as datas?")
    #print(crime_df.columns)

    crime_df = textFormatter.format(crime_df)
    #print("Como ficou o dataframe após os textos?")
    #print(crime_df.columns)

    crime_df = booleanFormatter.format(crime_df)
    #print(crime_df.head(5))

    # like Thanos, erase half of data
    # doing this due to performance issues
    # Random Forest was taking more than 30 minutes to run
    # crime_df = crime_df.drop(crime_df.index[350000:500000])

    clean_data_frame = crime_df

    print("O que nós temos antes de começar o processamento? ", clean_data_frame.head(1))
    print("\n\nMeu tamanho é: ", clean_data_frame.size)

    # The target, also known as the label, is the value we want to predict
    # The features are all the columns the model uses to make a prediction

    # https://stackoverflow.com/questions/43160575/how-to-create-an-array-from-two-columns-in-pandas
    # Labels are the values we want to predict
    labels = np.array(crime_df[['Latitude', 'Longitude']])
    # Remove the labels from the features
    crime_df = crime_df.drop(['Latitude', 'Longitude'], axis = 1)
    # Saving feature names for later use
    feature_list = list(crime_df.columns)
    # Convert to numpy array
    features_np_array = np.array(crime_df)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(crime_df, labels, test_size = 0.25, random_state = 42)

    print('Training Features Shape:', train_features.shape)
    print('Training Labels Shape:', train_labels.shape)
    print('Testing Features Shape:', test_features.shape)
    print('Testing Labels Shape:', test_labels.shape)
    return labels, feature_list, features_np_array, train_features, test_features, train_labels, test_labels, clean_data_frame