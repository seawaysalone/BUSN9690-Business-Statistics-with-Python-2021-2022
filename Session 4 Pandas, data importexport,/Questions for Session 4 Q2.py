##Q2##

import numpy as np

#A#

a = np.matrix([[1,2,6,2],
              [0,7,1,3],
              [4,0,2,1]])

b = np.matrix([[5,2,3,2],
              [2,1,4,4],
              [2,5,7,1],])


plus = a + b

minus = a - b

multiply = np.multiply(a,b)

divinding = a/b

#B#
  
b_t = np.transpose(b)

print(a*b_t)



