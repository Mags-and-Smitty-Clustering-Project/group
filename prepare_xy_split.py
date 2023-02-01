## IMPORTS

import os

import pandas as pd

from pydataset import data

from sklearn.model_selection import train_test_split

from env import host, username, password, get_connection




# train, validate, test are retrieved from the 'tts_zillow(zil)' function.
# the target needs to be entered in quotes, i.e, 'target_variable'.

def tts_xy(train, val, test, target):
    
    '''
    This function splits train, val, test into X_train, X_val, X_test
    (the dataframe of features, exludes the target variable) 
    and y-train (target variable), etc
    '''

    X_train = train.drop(columns = [target])
    y_train = train[target]


    X_val = val.drop(columns = [target])
    y_val = val[target]


    X_test = test.drop(columns = [target])
    y_test = test[target]

    return X_train, y_train, X_val, y_val, X_test, y_test
