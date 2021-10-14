import pandas as pd

class TextFormatter:

  def format(self, df):
    print("\n\nComeça processamento de Textos!")
    df = pd.get_dummies(df, columns=["Primary Type"])
    print("Apos get dummies")
    print(df.columns)
    print("\n\nFim processamento de Textos!")
    return df