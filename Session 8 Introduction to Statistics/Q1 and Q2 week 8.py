# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:49:13 2021

Q1 
"""
import pandas as pd


adult_Data = pd.read_csv("D:\Document\UKC\BUSN9690\Python\adult.csv",head = 0)

sampleData=Adult_Data.sample(n=4000,replace=False)


"""
Q2
 Mean sampleData.age.mean()
 Median sampleData.age.median()
 Min sampleData.age.min()
 Max sampleData.age.max()
 Standard deviation sampleData.age.std()
 The 1st quartile sampleData.age.quantile(0.25)
 The 3rd quartile sampleData.age.quantile(0.75)
"""


"""
Q3
"""

import numpy as np

len1=len(Adult_df) #to assign the sample size of Adult_df to len1
newAdult=[] #initialize newAdult
col1=list(Adult_df.columns) #to assign the row of variables to col1
newAdult.append(col1) #append the header to newAdult


for k in np.arange(0, len1, 1000):
 newAdult.append(list(Adult_df.iloc[k, :])) #to append the k-th observation to newAdult
resulting_df=pd.DataFrame(newAdult) #the result you needed