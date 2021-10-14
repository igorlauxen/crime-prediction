import pandas as pd

# this class is responsible for cleaning the date in the dateframe
class DateFormatter:

  # receives dataframe that will be cleaned
  # returns dataframe with dates in each column
  def format(self, df):
    print("\n\nProcessamento de datas!")
    # dates have the format MM/DD/YYYY HH:MM:SS PM/AM
    df[["NewDate", "TimeOfDay", "PeriodOfDay"]] = df["Date"].str.split(" ", expand = True)
    # now we have a column like NewDate(MM/DD/YYYY), TimeOfDay(HH:MM:SS), PeriodOfDay(PM/AM)
    # so we need to create our Month,Day,Year columns
    df[["Month", "Day", "Year"]] = df["NewDate"].str.split("/", expand = True)
    # Original date column will not be used anymore, bye byeeee
    df.drop(["Date", "NewDate"], axis = 1, inplace = True)
    print("Apos limpeza da Data com Mes,Dia,Ano")
    print(df.columns)

    # now we have to create the Hour,Minute,Seconds
    df[["Hour", "Minute", "Seconds"]] = df["TimeOfDay"].str.split(":", expand = True)
    df.drop(["TimeOfDay"], axis = 1, inplace = True)
    print("Apos limpeza da Data com Hora,Minuto,Segundo")
    print(df.columns)

    # now we need to translate PM/AM to something meaninful (1/0)
    df = pd.get_dummies(df, columns=["PeriodOfDay"])
    print("Apos get dummies")
    print(df.columns)

    print("\n\nFim Processamento de datas!")
    return df