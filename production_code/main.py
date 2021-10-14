# Pandas is used for data manipulation
import pandas as pd
from DateFormatter import DateFormatter
from TextFormatter import TextFormatter

dateFormatter = DateFormatter()
textFormatter = TextFormatter()

# Read in data and get dataframe
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#original_crimes_dataframe = oc_df
oc_df = pd.read_csv('./data/generated_file_aa.csv',index_col ="ID")
print(oc_df.head(5))

# we may review this
# depending on the granularity of these properties
# we may leave one with the assumption of the proximity of crimes
# Removing Location Description because its description varies A LOT
dropped_columns = ["IUCR", "Beat", "District", "Ward", "Community Area", "FBI Code", "X Coordinate", "Y Coordinate", "Updated On", "Case Number", "Location", "Location Description"]

# remove the following columns
# based on https://www.geeksforgeeks.org/python-delete-rows-columns-from-dataframe-using-pandas-drop/
oc_df.drop(dropped_columns, axis = 1, inplace = True)
# check how the data looks like after changes
print("Depois das mudanças")
print(oc_df.head(5))
print("Quantas entradas existem?")
print(len(oc_df.index))

# drop rows that are inconsistent
# https://stackoverflow.com/questions/44548721/remove-row-with-null-value-from-pandas-data-frame/44548976
print("\n\nRemover dados inconsistentes: qualquer coisa com null")
clean_data_frame = oc_df.dropna(how='any',axis=0) 
print("Quantas entradas existem apos limpeza dos dados?")
print(len(clean_data_frame.index))

# random forest seems to expect all columns to be numbers
# as described in here: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
# due do this we need to convert the string columns to be something meaninful to the RF
# Non number columns: Primary Type, Description, Location Description, Arrest, Domestic, Date

clean_data_frame = dateFormatter.format(clean_data_frame)

print("Como ficou o dataframe após as datas?")
print(clean_data_frame.columns)

clean_data_frame = textFormatter.format(clean_data_frame)
print("Como ficou o dataframe após os textos?")
print(clean_data_frame.columns)