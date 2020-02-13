# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:10:09 2020

@author: Vishal
"""

import pandas as pd
import numpy as np
import os

# file path
CSV_PATH = os.path.join('..','collection_master','data_frame.pickle')

df = pd.read_pickle(CSV_PATH)

small_df = df.iloc[49980:50019, :].copy()
grouped = small_df.groupby('artist')
type(grouped)

for name,group_df in grouped:
    print(name)
    print(group_df)
    break

def fill_values(series):
    values_counted= series.value_counts()
    if values_counted.empty:
        return series
    most_frequent = values_counted.index[0]
    new_medium = series.fillna(most_frequent)
    return new_medium

def tranform_df(source_df):
    group_dfs=[]
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
        group_dfs.append(filled_df)

    new_df = pd.concat(group_dfs)
    return new_df


# result
filled_df = tranform_df(small_df)




# Simple methods
grouped_mediums = small_df.groupby('artist')['medium']
small_df.loc[:,'medium'] =  grouped_mediums.transform(fill_values)


# min
df.groupby('artist').agg(np.min)
df.groupby('artist').min()

# filter 
grouped_title = df.groupby('title')
title_counts =  grouped_title.size().sort_values(ascending=False)

