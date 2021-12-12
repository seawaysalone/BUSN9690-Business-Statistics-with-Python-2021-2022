# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:49:13 2021

Q1 Download adult.csv from Moodle. Read this file to Python and then use the simple random sampling method to sample 4000 observations from the 
dataset.
"""
import pandas as pd


adult_Data = pd.read_csv(r"adult.csv")

sampleData=adult_Data.sample(n=4000,replace=False)


"""
Q2 On variable age in the sampled data from Exercise 1, provide

 Mean sampleData.age.mean()
 Median sampleData.age.median()
 Min sampleData.age.min()
 Max sampleData.age.max()
 Standard deviation sampleData.age.std()
 The 1st quartile sampleData.age.quantile(0.25)
 The 3rd quartile sampleData.age.quantile(0.75)
"""


"""
Q3 Use the systematic sampling method to sample every 1000th observation from Adult.csv
"""

import numpy as np

len1 = len(adult_Data) #to assign the sample size of adult_Data to len1
newAdult = [] #initialize newAdult
col1 = list(adult_Data.columns) #to assign the row of variables to col1
newAdult.append(col1) #append the header to newAdult


for k in np.arange(0, len1, 1000):
 newAdult.append(list(adult_Data.iloc[k, :])) #to append the k-th observation to newAdult
resulting_df=pd.DataFrame(newAdult) #the result you needed


"""
Q4 Use the stratified random sampling method to sample every 40% of the observations from Adult.csv from income=>=50K and <50K, respectively
"""
import numpy as np

len1=len(adult_Data) #to assign the sample size of adult_Data to len1

newAdult_under=[] #initialize: this is for all observations with income "<=50"
newAdult_above=[] #initialize: this is for all observations with income ">50"
col1=list(adult_Data.columns) #to assign the row of variables to col1
newAdult_under.append(col1) #append the header to newAdult
newAdult_above.append(col1) #append the header to newAdult
#newAdult.append(col1) #append the header to newAdult

for k in np.arange(0, len1): #read each observation
 if adult_Data.loc[k,'income']==" <=50K": #if the income variable is <=50K, noting that there is a space before <=50K 
     newAdult_under.append(list(adult_Data.iloc[k, :])) #to append the k-th observation to newAdult_under
 else: #otherwise, if the income variable is >50K
  newAdult_above.append(list(adult_Data.iloc[k, :])) #to append the k-th observation to newAdult_above
newAdult_under_df=pd.DataFrame(newAdult_under) #to convert newAdult_under to a dataframe

newAdult_above_df=pd.DataFrame(newAdult_above) #to convert newAdult_above to a dataframe
newAdult_under_sample=newAdult_under_df.sample(frac=0.4,replace=False)#to sample 40% observations from newAdult_under and assign them to newAdult_under_sample
newAdult_above_sample=newAdult_above_df.sample(frac=0.4,replace=False)#to sample 40% observations from newAdult_above and assign them to newAdult_above_sample
