#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
from env import user, password, host
import env
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import wrangle_zillow



def bedroom_w_county(zillow_train):
    fig, ax = plt.subplots(figsize = (7,5))
    sns.scatterplot(data=zillow_train,x=zillow_train['longitude'],
                y=zillow_train['latitude'], zorder=1,hue='bedroom')


# In[15]:


def l_county(zillow_train):
    fig, ax = plt.subplots(figsize = (7,5))
    sns.scatterplot(data=zillow_train,x=zillow_train['longitude'],
                y=zillow_train['latitude'], zorder=1,hue='county')



def plot_categorical_and_continuous_vars():
    columns = zillow_train.select_dtypes('object')
    for col in columns:
        sns.set(rc={'figure.figsize':(20,10)})
        fig, axes = plt.subplots(2,2)
        sns.boxplot(x= col, y="taxvalue", data=zillow_train, hue = 'county', ax = axes[0,0])
        sns.barplot(x= col, y="taxvalue", data=zillow_train, hue = 'county', ax = axes[0,1])
        sns.violinplot(x= col, y="taxvalue", data=zillow_train, hue = 'county', ax = axes[1,0])
        sns.scatterplot(x= col, y="taxvalue", data=zillow_train, hue = 'county', ax = axes[1,1])


# In[7]:


def plot_variable_pairs():
    columns = zillow_train.select_dtypes('float')
    for col in columns:
        sns.lmplot(x= col, y="taxvalue", data=zillow_train, col = 'county', hue = 'county', line_kws={'color': 'red'})



# In[8]:
def differentrate(zillow_train):
   ax=sns.displot(
    data=zillow_train,
    x="month", hue="county",
    kind="kde", height=6,
    multiple="fill", clip=(0, None),
    palette="ch:rot=-.25,hue=1,light=.75",
).set(title='County transaction rate',ylabel='transaction')
# In[9]:


def tax_per_month(zillow_train):
    sns.kdeplot(zillow_train.month[(zillow_train["taxvalue"]<1000000)],
                color="#0072BD", shade = True)





