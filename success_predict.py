# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:30:27 2018

@author: pmannuel
"""
import pandas as pd
import numpy as np

data = pd.read_csv('Kickstarter_2018-01.csv', error_bad_lines=False)

selected_cols = ['backers_count',
                     'blurb',
                     'category.id',
                     'category.name',
                     'category.parent_id',
                     'category.slug',
                     'country',
                     'created_at',
                     'deadline',
                     'goal',
                     'launched_at',
                     'name',
                     'spotlight',
                     'staff_pick',
                     'state',
                     'usd_pledged',
                     'usd_type']
    
data = data[selected_cols]

#because there are some "bad lines" a.k.a lines that are shifted to the right due to bad parsing
#subset rows that are correctly parsed
# correctly parsed rows should have a legit entry in the domestic col
#domestic = data['usd_type'] == "domestic"
#intl = data['usd_type'] == "international"
#blank = data['usd_type'].isnull().any()
#drop data with empty blurb or empty name entries
#given more time, webscrapped missing entries
data = data.dropna() 
    
#select only data with known status
successful = data['state'] == "successful"
failed = data['state'] == "failed"
cancelled = data['state'] == "cancelled"
suspended = data['state'] == "suspended"

data = data.loc[failed | successful | cancelled | suspended]

#correct class of columns
categorical_cols = ['category.id',
                    'category.parent_id',
                    'country',
                    'spotlight',
                    'staff_pick',
                    'state',
                    'usd_type']

data[categorical_cols] = pd.Categorical

num_cols = ['usd_pledged',
            'deadline',
            'created_at',
            'launched_at']

data[num_cols] = data[num_cols].apply(pd.to_numeric, errors='coerce')

#because there are some "bad lines" a.k.a lines that are shifted to the right due to bad parsing
#subset rows that are correctly parsed
# correctly parsed rows should have a legit entry in the domestic col
#domestic = data['usd_type'] == "domestic"
#intl = data['usd_type'] == "international"
#blank = data['usd_type'].isnull().any()
#drop data with empty blurb or empty name entries
#given more time, webscrapped missing entries
data = data.dropna()

data['created_at'] = pd.to_datetime(data['created_at'],unit='s')
data['launched_at'] = pd.to_datetime(data['launched_at'],unit='s')
data['deadline'] = pd.to_datetime(data['launched_at'],unit='s')

#Check data
data.info()
data.describe()
data.columns[data.isnull().any()]
