# -*- coding: utf-8 -*-
"""Data Preparation na Prática

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eLj3g59HWbLO5DWXf_NK5SXj6O8JxENN
"""

from google.colab import files
upload = files.upload()

import pandas as pd
import numpy as np

df = pd.read_csv('DataPrepFinal.csv')

df.head()

df = df.drop(columns = ['Unnamed: 0', 'name', 'category', 'goal', 'pledged', 'usd pledged'])

df.head()

df['usd_goal_real'] = df['usd_goal_real'].str.strip('USD')

df.head()

# RegEx

df['launched'] = df['launched'].str.replace(' \d\d:\d\d','', regex=True)

df.head()

df['usd_goal_real'] = df['usd_goal_real'].astype('int64')

df['launched'] = pd.to_datetime(df['launched'], format='%d/%m/%y')
df['deadline'] = pd.to_datetime(df['deadline'], format='%d/%m/%y')

df.dtypes

# Criação variável tempo ao vivo

df['time_range'] = (df['deadline'] - df['launched']).dt.days

df.head()

dfc = pd.read_csv('campaign.csv')

dfc.head()

df.head()

dfc['Text Description'].unique()

dfc = dfc.drop(['Text Description'], axis=1)

dfc.head()

# Fazendo merge

df = df.merge(dfc, how='right', on=['ID'])

df.head()

dfi = pd.read_csv('invested.csv')

dfi.head()

dfi = pd.get_dummies(dfi, columns = ['backedLocation'], dtype=int)

dfi.head()

dfi.sort_values(by=['ID'])

dfi = dfi.groupby(by=['ID']).agg({'age': 'mean', 'backedLocation_BR': 'sum', 'backedLocation_GBK': 'sum', 'backedLocation_US': 'sum'})

dfi.head()

df = df.merge(dfi, how='right', on=['ID'])

df.head()

