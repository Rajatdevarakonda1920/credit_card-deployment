#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import warnings 
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


# In[2]:


df =  pd.read_csv(r'C:\Users\RAJAT DEVARAKONDA\Desktop\Data_Science\PROJECTS DEPLOYMENTS\credit_card\data.csv')
Y=df['default.payment.next.month']
X=df.drop(['default.payment.next.month'],axis=1)
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest=train_test_split(X, Y, test_size=0.2, random_state=42)
#scaling
scl = StandardScaler() 
#scl the feature based on mean and std ...i have preferd standrisation coz features can take form of normal distribution
#this will make models to learn weights easily and also will make less sentive to outliers 
scl.fit(xtrain)
xtrain_scl = pd.DataFrame(scl.transform(xtrain))
xtest_scl = pd.DataFrame(scl.fit_transform(xtest))
xtest_scl.columns = xtest.columns 
xtrain_scl.columns = xtrain.columns 
rf_hp = RandomForestClassifier(bootstrap = False, criterion = 'gini', max_depth = 9,
        max_features = 'auto', min_samples_split= 7, n_estimators = 100)
rf_hp.fit(xtrain_scl,ytrain)




import joblib
joblib.dump(rf_hp,'credit_crd.pkl')



# %%
