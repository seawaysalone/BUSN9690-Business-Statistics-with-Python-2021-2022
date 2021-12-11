import pandas as pd 
import math 

Weight_Height = pd.read_csv('weight-height.csv')

########################
def BMI_calculator(Height,Weight):
    
    ConvertedHeight = Height*0.0254
    ConvertedWeight = Weight*0.453592

    Math = ConvertedWeight/ConvertedHeight**2
    
    return Math
########################

NumRows = Weight_Height.shape[0]

BMI=[] 
BMI = [0 for i in range(NumRows)]

########################

yourHealthCondition = [] 
yourHealthCondition = [0 for i in range(NumRows)] 

########################

for i in range(0,NumRows): #in i start count 0 to 999
    
 W1 = Weight_Height.loc[i,"Weight"]  #to assign the i-th Weight to W1, where W1 is a middle variable 

 H1 = Weight_Height.loc[i,"Height"] 
   
 า่่าBMI[i] = BMI_calculator(H1,W1) #to call the BMI function
   
 if BMI[i]<18.5: 
  yourHealthCondition[i]="you're in the underweight range." #when the condition is met, 
 
 elif BMI[i]>=18.5 and BMI[i]<25: 
  yourHealthCondition[i]="you're in the healthy weight range."
 
 elif BMI[i]>=25 and BMI[i]<30:
  yourHealthCondition[i]="you're in the overweight range."
 
 elif BMI[i]>=30 and BMI[i]<40: 
  yourHealthCondition[i]="you're in the obese range."
 
 else:
  yourHealthCondition[i]="you're in the over-obese range."
 
########################

Weight_Height['BMI'] = BMI #to add the BMI array to the file
Weight_Height['yourHealthCondition'] = yourHealthCondition #to add the yourHealthCondition array to the file
Weight_Height.to_csv("Weight-height-BMI1.csv.csv") #to write the data to a csv fil





