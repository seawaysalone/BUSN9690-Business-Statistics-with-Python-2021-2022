import pandas as pd 
import os 


surveys_df = pd.read_csv("surveys.csv",header=0) 

#A surveys_df.info

#B surveys_df.head()

#C Survey=surveys_df.dropna()
#  Survey.info()

#D surveys_df.duplicated() len 35556

#E  surveys_df.drop_duplicates(inplce = True) len will be 35549