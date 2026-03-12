import pandas as pd

DATA1 = pd.DataFrame( {'Name':['Shalu','Gudddu','Simmi','Nitu','kittu'],
                       'AGE':[15,16,17,16,None],
                       'Subject':['pcm','pcb','pcm','arts','commerse'],
                       'AVG_Marks':[68,70,75,80,76]} )
print(DATA1)
print(DATA1.head())