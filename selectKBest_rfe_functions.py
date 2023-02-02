# imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, f_regression, RFE

from env import host, username, password, get_connection
import env




# SelectKBest function

# df = dataframe,
# scaled_cols = columns to scale, entered as a list, i.e, ['variable_name'],
# target_var = target variable, entered as a string, i.e, 'variable_name'
# kk = the k number of features to select / return

def select_best(df, scaled_cols, target_var, kk):
 
    '''
    This function takes in the predictors (X), the target (y) and 
    the number of features to select (k) and returns the names of
    the top k selected features based on the SelectKBest class. 
    '''
    
    # creating a copy of original df in order to avoid messes and permanently scaled data later
    df_copy = df.copy()
    
    # scaling the data in specific columns, reassigning the scaled numbers to the column names
    mms = MinMaxScaler()
    df_copy[scaled_cols] = mms.fit_transform(df_copy[scaled_cols])

    # feature array / df with continuous features (X, ...) and target (y)
    X_train_scaled = df_copy[scaled_cols]
    y_train = df_copy[target_var]

    # create an instance of the SelectKBest object
    selector = SelectKBest(f_regression, k = kk)

    # fit the object to data : .fit(features, target variable)
    selector.fit(X_train_scaled, y_train)
    
    # masking the values by assigning a variable to the T/F in order to apply it to the columns
    selector_rankings = selector.get_support()

    # see only the column names relevant to our analysis
    best = X_train_scaled.columns[selector_rankings]
    
    return best




# RFE function

# df = dataframe,
# target_var = target variable (y-value), the column to drop, entered as a string, i.e, 'variable_name'
# fts = n_features_to_select
# dummy_columns = columns of which to make dummies, entered as a list, i.e ['variable_name']

def rfe_function(df, fts, target_var, dummy_columns):
    
    '''This function takes in the predictors, the target and the 
    number of features to select and returns the top k-features 
    based on the RFE class.
    '''
    
    # dropping 'tip' to allow for fair evaluation of data
    X_train = df.drop(columns = target_var)

    # make dummies of categorical columns, then reassign to variable X_train
    X_train = pd.get_dummies(X_train, columns = dummy_columns)
    y_train = df[target_var]

    # RFE uses a machine learning model (here, linear regression) 
    #   to determine the 2 features with the most predictive capability
    rfe = RFE(LinearRegression(), n_features_to_select = fts)

    # fitting 
    rfe.fit(X_train, y_train)

    # ranking of the categorical columns and aligning them with their column names
    ranking = rfe.ranking_
    features = X_train.columns.tolist()

    # turning ranks & columns into a df
    df = pd.DataFrame({'ranking' : ranking,
                       'feature' : features})

    df = df.sort_values('ranking')
    
    return df