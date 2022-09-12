
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


# In[4]:


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[5]:


def acquire_zillow():
    file='zillow_df.csv'
    if os.path.isfile(file):
        return pd.read_csv(file)
    else:
        zillow2017_df = pd.read_sql(('SELECT yearbuilt,lotsizesquarefeet,logerror,longitude,latitude,transactiondate,bathroomcnt,bedroomcnt,fips,calculatedfinishedsquarefeet,regionidzip,taxvaluedollarcnt FROM properties_2017 JOIN propertylandusetype USING (propertylandusetypeid) JOIN predictions_2017 USING (id) WHERE propertylandusedesc = "Single Family Residential" and predictions_2017.transactiondate like "2017%%"'), get_connection('zillow'))
        zillow2017_df.to_csv(file,index=False)
    return zillow2017_df


# In[8]:


def clean_column():
    zillow2017_df=acquire_zillow()
    zillow2017_df.rename(columns={'bedroomcnt':'bedroom','bathroomcnt':'bathroom','calculatedfinishedsquarefeet':'sqtft','taxvaluedollarcnt':'taxvalue','garagecarcnt':'garage','lotsizesquarefeet':'lots','poolcnt':'pool','regionidzip':'zipcode'},inplace=True)
    zillow2017_df['fips']= zillow2017_df['fips'].astype(object)
    value=[]
    for row in zillow2017_df['fips']:
        if row ==6037.0: value.append('Los Angeles County, CA')
        elif row == 6059.0: value.append("Orange County, CA")
        elif row == 6111.0: value.append('Ventura County, CA')
        else:
            value.append('Undetermined')
    zillow2017_df['county']=value
    zillow2017_df['zipcode']=zillow2017_df['zipcode'].astype(object)
    return zillow2017_df


# In[9]:


def remove_outlier(k):
    zillow2017_df=clean_column()
    col_list=zillow2017_df.select_dtypes(float)
    for col in col_list:
        q1, q3 = zillow2017_df[col].quantile([.25, .75]) 
        iqr = q3 - q1  
        upper_bound = q3 + k * iqr  
        lower_bound = q1 - k * iqr  
        zillow2017_df = zillow2017_df[(zillow2017_df[col] > lower_bound) & (zillow2017_df[col] < upper_bound)]
    return zillow2017_df.dropna()


# In[10]:


def get_hist(k):
    zillow2017_df=remove_outlier(k)
    plt.figure(figsize=(16, 3))
    cols = zillow2017_df.select_dtypes(float).columns
    for i, col in enumerate(cols):
        plot_num = i + 1 
        plt.subplot(1, len(cols), plot_num)
        plt.title(col)
        zillow2017_df[col].hist(bins=5)
        plt.grid(False)
        plt.ticklabel_format(useOffset=False)
        plt.tight_layout()
    plt.show()


# In[11]:


def wrangle_zillow(k):
    zillow2017_df=remove_outlier(k)
    get_hist(k)
    train_validate, zillow_test = train_test_split(zillow2017_df, test_size=.2, random_state=123)
    zillow_train, zillow_validate = train_test_split(train_validate, test_size=.3, random_state=123)
    zillow_train['month']=pd.DatetimeIndex(zillow_train['transactiondate']).month
    zillow_train=zillow_train.drop(columns=['transactiondate'])
    zillow_validate['month']=pd.DatetimeIndex(zillow_validate['transactiondate']).month
    zillow_validate=zillow_validate.drop(columns=['transactiondate'])
    zillow_test['month']=pd.DatetimeIndex(zillow_test['transactiondate']).month
    zillow_test=zillow_test.drop(columns=['transactiondate'])
    return zillow_train, zillow_validate, zillow_test


# In[ ]:
def scale(scaler,zillow_train,cols=['bedroom','bathroom','sqtft','lots'],return_scaler=True):
    zillow_train=zillow_train
    zillow_train_scaled=zillow_train.copy()
    scaler=scaler
    zillow_train_scaled[cols] = scaler.fit_transform(zillow_train[cols])
    return scaler, zillow_train_scaled



