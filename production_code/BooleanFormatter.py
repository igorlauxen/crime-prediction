
class BooleanFormatter:
  def format(self, df):
    print("\n\nComeça processamento de Booleans!")
    # https://stackoverflow.com/questions/21608228/conditional-replace-pandas
    df.loc[(df.Arrest == True), 'Arrest'] = 1
    df.loc[(df.Arrest == False), 'Arrest'] = 0
    df.loc[(df.Domestic == True), 'Domestic'] = 1
    df.loc[(df.Domestic == False), 'Domestic'] = 0
    print("\n\nFim processamento de Booleans!")
    return df;