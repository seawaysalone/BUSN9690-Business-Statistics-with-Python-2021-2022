##Q4
wh = pd.read_csv('weight-height.csv')

#####CONVERT UNITS#############
##define functions
def convert_weight(w):
    return w*0.453592
def convert_height(h):
    return h*0.0254
##apply conversion
wh.Weight = wh.Weight.apply(convert_weight)
wh.Height = wh.Height.apply(convert_height)

##insert BMI col
wh['BMI'] = wh['Weight']/wh['Height']**2

##determaine Health condition
def health_condi(a):
    if a < 18.5:
        b = "you're in the underweight range."
    elif a >= 18.5 and a < 25:
        b = "you're in the healthy weight range."
    elif a >= 25 and a < 30:
        b = "you're in the overweight range."
    elif a >= 30 and a < 40:
        b = "you're in the obese range."
    elif a >= 40:
        b = "you're in the over obese range."
    return b
##insert Health condition col
wh['Health Condition'] = wh['BMI'].apply(health_condi)

##export to csv
wh.to_csv("Weight-height-BMI.csv")