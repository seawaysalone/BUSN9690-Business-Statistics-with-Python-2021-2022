#A#
import pandas as pd

AE_df = pd.read_csv(r'D:\Document\UKC\BUSN9690\Python\adult.csv')

print(AE_df)

#B#
head = AE_df.head()


print(head)

#C#
 
a = AE_df.info()
 
dataStructure = pd.DataFrame(a)

print(dataStructure)

#D#

b = AE_df.describe()
 
print(b)

#E#

##cannot use "hours-per-week"## 

hours_per_week = AE_df.describe()

#F#
