import math

def Math(x,a,beta):

    Math = 1 - math.exp(-(x/a)**beta) 

    return Math

Math(10,10,1.2)

