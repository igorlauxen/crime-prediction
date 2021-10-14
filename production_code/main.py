# Pandas is used for data manipulation
import pandas as pd

# Read in data and get dataframe
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#original_crimes_dataframe = oc_df
oc_df = pd.read_csv('./data/generated_file_aa.csv',index_col ="ID")
print(oc_df.head(5))

# we may review this
# depending on the granularity of these properties
# we may leave one with the assumption of the proximity of crimes
dropped_columns = ["IUCR", "Beat", "District", "Ward", "Community Area", "FBI Code", "X Coordinate", "Y Coordinate", "Updated On", "Case Number", "Location"]

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

print("\n\nProcessamento de datas!")

# dates have the format MM/DD/YYYY HH:MM:SS PM/AM
clean_data_frame[["NewDate", "TimeOfDay", "PeriodOfDay"]] = clean_data_frame["Date"].str.split(" ", expand = True)
# now we have a column like NewDate(MM/DD/YYYY), TimeOfDay(HH:MM:SS), PeriodOfDay(PM/AM)
# so we need to create our Month,Day,Year columns
clean_data_frame[["Month", "Day", "Year"]] = clean_data_frame["NewDate"].str.split("/", expand = True)
# Original date column will not be used anymore, bye byeeee
clean_data_frame.drop(["Date", "NewDate"], axis = 1, inplace = True)
print("Apos limpeza da Data com Mes,Dia,Ano")
print(clean_data_frame.columns)

# now we have to create the Hour,Minute,Seconds
clean_data_frame[["Hour", "Minute", "Seconds"]] = clean_data_frame["TimeOfDay"].str.split(":", expand = True)
clean_data_frame.drop(["TimeOfDay"], axis = 1, inplace = True)
print("Apos limpeza da Data com Hora,Minuto,Segundo")
print(clean_data_frame.columns)

# now we need to translate PM/AM to something meaninful (1/0)
clean_data_frame = pd.get_dummies(clean_data_frame, columns=["PeriodOfDay"])
print("Apos get dummies")
print(clean_data_frame.columns)

print("\n\nFim Processamento de datas!")