import pandas as pd
import sklearn
import matplotlib


hearing = pd.read_csv('DataFiles/Hearing.csv')
hearing_pd = pd.DataFrame(hearing).head()

hearing_pd.plot.scatter(x='Perceived_Hearing_Meaning', y='Daily_Headphone_Use')

 






