# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:17:11 2020

@author: vlahane
"""

import pandas as pd
import os

# file path
CSV_PATH = os.path.join('..','collection_master','data_frame.pickle')

df = pd.read_pickle(CSV_PATH)

#df.artist  # don't use this in code

artists = df['artist']
pd.unique(artists)
len(pd.unique(artists))


s = df['artist'] == 'Blake, Robert'
s.value_counts()

# Other way
artist_counts = df['artist'].value_counts()
artist_counts['Blake, Robert']

# Demo 3
df.loc[1035,'artist']  # single value
df.iloc[0,0] # 1st row and column
df.iloc[0,:]  #1st full row
df.iloc[0:2,0:2] # 2 rows and two coulmn (1st)


df.loc[df['artist'] == 'Blake, Robert' ,:]  # get all rows and column for Robert

# Row index    Column indexer
#df.loc[100:103,[0,1,4]]

# try mutiplication

#df['height'] * df['width']  # error Object so need to convert
#df['height'].sort_values().head()
#df['width'].sort_values().tail()


# Try to convert 
#pd.to_numeric(df['width'], errors='coerce')
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

#pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')


df['height'] * df['width']  # converted values 

df['units'].value_counts()

# Assign - create new column with size

area = df['height'] * df['width']


df = df.assign(area=area)

df['area'].max()
df['area'].idxmax()
df.loc[df['area'].idxmax(),:]
