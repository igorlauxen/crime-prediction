import pandas as pd
import seaborn as sns

from DataPreparator import DataPreparator
from MapAnalyser import MapAnalyser

dataPreparator = DataPreparator()
mapAnalyser = MapAnalyser()


# Read in data and get dataframe
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#original_crimes_dataframe = oc_df
oc_df = pd.read_csv('./data/generated_file_aa.csv',index_col ="ID")
print(oc_df.head(5))


# sns.scatterplot(oc_df['Latitude'], oc_df['Longitude'])

# Data Preparation
labels, feature_list, features_np_array, train_features, test_features, train_labels, test_labels, clean_data_frame = dataPreparator.prepare(oc_df)
# Baseline

mapAnalyser.createMap(clean_data_frame)


# RF execution

# In the end game I want to predict what crime can happen and where it will 
# But first I'll split them into two different predictions: 
#   1) tell where it will happen 
#   2) tell what will happen
#   3) Tell me what will happen and where