'''
Script to combine all csv of facial features into one csv file
'''


import pandas as pd
df_name = pd.DataFrame()
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
    if (f.find('csv') != -1): 
        df = pd.read_csv(f,sep = ", ", engine = "python")
        df_name = df_name.append(df,ignore_index=True)