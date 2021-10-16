import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

from DataPreparator import DataPreparator
from MapAnalyser import MapAnalyser

dataPreparator = DataPreparator()
mapAnalyser = MapAnalyser()

# Read in data and get dataframe
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#original_crimes_dataframe = oc_df
oc_df = pd.read_csv('./data/generated_file_aa.csv',index_col ="ID")
print("\n\nMeu tamanho é: ", oc_df.size)

print(oc_df.head(10))
print("\n\nMeu tamanho após filtro é: ", oc_df.size)
print("Dados filtrados")

# Data Preparation
labels, feature_list, features_np_array, train_features, test_features, train_labels, test_labels, clean_data_frame = dataPreparator.prepare(oc_df)

print("Random Forest vai começar!")
rf = RandomForestRegressor(n_estimators = 500, random_state = 42)
print("RF inicializado")
rf.fit(train_features, train_labels)
print("RF Treinado")

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
print("Random Forest finalizou as predições!")

# Calculate the absolute errors
errors = abs(predictions - test_labels)

# Print out the mean absolute error (mae)
print('Valores dos errors:',errors)
print('Media absolura dos erros:',np.mean(errors))


# RF execution

# In the end game I want to predict what crime can happen and where it will 
# But first I'll split them into two different predictions: 
#   1) tell where it will happen 
#   2) tell what will happen
#   3) Tell me what will happen and where