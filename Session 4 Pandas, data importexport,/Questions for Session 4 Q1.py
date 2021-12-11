###Q1###

import pandas as pd
#A#
a = pd.DataFrame({'Name':['John','Anna','Emma'],'Business statistic':[65,72,56],'Simulation':[60,65,64]})

#B#
a2 = pd.DataFrame(a)

#C#
#print(a.loc[0])

#D#
del a2

#E#
a.drop([2],axis=0) #axis=0 denotes row, and axis=1 denotes column

#F#
a['Grade'] =  ['Merit', 'Merit','Merit']

print(a)



