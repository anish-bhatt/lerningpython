# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:08:17 2023

@author: Bhatt
"""

''' PANDAS - for any data files   '''


""" DATAFRAME """

import pandas as pd

df_datacsv = pd.read_csv('Data.csv')

# df_data1xlsx = pd.read_csv('data1.csv')

""" Methods of Dataframe """
""" Head = top / tail = Bttom of data - default 5 """

df_datacsv.head(1)   ## Top lines 
df_datacsv.tail(2)   ## End lines 

""" Dataframe one column can b made an index"""
df_datacsv = df_datacsv.set_index("origin") 

df_datacsv.loc["Texas"] 

""" Slicinng datafram """

df_Slice1 =df_datacsv["size"]
print(df_Slice1)

df_Slice2 =df_datacsv[["size","battles","regiment"]]
print(df_Slice2)

"""" index operators 
same as list slicing and indexing of data 0 is first - from bottom first is -1"""
df_datacsv.index[4]
df_datacsv.index[0:4]
df_datacsv.index[4:]
df_datacsv.index[4:-1]


""" 
Slicing - Label basd of Index based 
iloc is better 
"""
df_datacsv.iloc[:] ## Everything ROWS : COl
df_datacsv.iloc[0:3,0:3]
df_datacsv.iloc[0:3,2]
df_datacsv.iloc[0:-1,-1:]
df_datacsv.iloc[0:5, 0]
df_datacsv.iloc[7:, -2]
df_datacsv.iloc[1:3]
df_datacsv.iloc[2:]
df_datacsv.iloc[:,:2]
df_datacsv.iloc[:,:-1]
df_datacsv.iloc[0:3,3:2]

x = df_datacsv.iloc[7:, -2]

"""
Boolean Masking
just like filter in Excel
"""

df_datacsv["deaths"]>50  ## gives output on screen

df_datacsv[df_datacsv["deaths"]>50]  ## gives output on screen 

"""Gives output of the dataframe in to another dataframe """
df_datacsv_filtered = df_datacsv[df_datacsv["deaths"]>50] 

df_datacsv [df_datacsv("deaths")<50] | [df_datacsv("deaths")>500]

""""get from percy """"
x = df_datacsv[(df_datacsv("deaths")>=50)] & [(df_datacsv("regiment")!= "Dragoons")]

c = df_datacsv

head tail 
"""""""""""""""""""""""""""""""
""""""""""""""""""""""""
df_datacsv.dtypes

df_datacsv['regiment'].nunique()   ## no of unique vallues 

df_datacsv['company'].unique()  ## List of unique vallues 

"""

"""


import pandas as pd

dfGame = pd.read_csv('Data.csv')
dfGame=dfGame.assign(survived=2000-dfGame['deaths'])

dfGame['left']=2000-dfGame['deaths']

""" Adds a column n DF """
dfGame['status']=''

""" Adds a column and populates Male in it """
dfGame['Gender']='Male'

dfGame.dtypes

""" get from Percy """
dfGame[['battles','size']]=dfGame(['battles','size']).astype(str)
""" """


""" dropping column """
dfGame=dfGame.drop('Gender', axis=1)

dfGame=dfGame.drop(['Gender', 'status'], axis=1)

dfGame=dfGame.rename(columns={'comapany':'abc', 'regiment':'batallion'})

print(dfGame)


dfGame.to_csv('game.csv', index=False)

dfGame.to_csv('game.xlsx', index=False)
""" use sep =|
"""

for index,row in dfGame.itrrows():
    print(index,row)
    
for row in dfdatacsv.itrtuples():
    print(row)
    
"""ravel vs flatten / iterrows or itrtuples """

df1=pd.read_csv('Data.csv')
    
df1['avg_daath'] = df1.apply(lambda row : row ['deaths']/row ['battles'] ,axis=1)
