# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:59:53 2020

@author: vlahane
"""

import pandas as pd
import os

# file path
CSV_PATH = os.path.join('..','collection_master','artwork_data.csv')

# read csv
df = pd.read_csv( CSV_PATH , nrows=5)

# read csv set index within file
df = pd.read_csv( CSV_PATH , nrows=5 ,index_col='id' )

# read csv file ,only with two columns
df = pd.read_csv( CSV_PATH , nrows=5 ,index_col='id' , usecols=['id',
                 'artist'])

# Use more columns
COLS_TO_USE = ['id','artist','title','medium','year','acquisitionYear',
               'height','width','units']
df =  pd.read_csv(CSV_PATH , usecols=COLS_TO_USE,index_col='id')

df.to_pickle(os.path.join('..','collection_master','data_frame.pickle'))
#
