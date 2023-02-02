import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LassoLars
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import TweedieRegressor
from math import sqrt
from scipy.stats import pearsonr, spearmanr
from scipy import stats

from env import get_connection
import prepare


# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


def t_test(a, b):
    '''
    This function will take in two arguments in the form of a continuous and discrete variable and runs
    an independent t-test and prints whether or not to print whether or not to rejec the Null Hypothesis
    based on those results
    '''
    alpha = 0.05
    t, p = stats.ttest_ind(a, b, equal_var=False)
    print(t, p / 2)
    print("")
    if p / 2 > alpha:
        print("We fail to reject $H_{0}$")
    elif t < 0:
        print("We fail to reject $H_{0}$")
    else:
        print("We reject the null hypothesis as there is a\nsignificant relationship between density and quality of wine.")

        
def chi_sq(a, b):
    '''
    This function will take in two arguments in the for of two discrete variables and runs a chi^2 test
    to determine if the the two variables are independent of each other and prints the results based on the findings
    '''
    result = pd.crosstab(a, b)

    chi2, p, degf, expected = stats.chi2_contingency(result)

    print(f'chi^2  = {chi2:.4f}') 

    print(f'p-value = {p:.4f}')
        
    
    
def model_report():
    data = {'Model': ['Linear Regression', 'Lasso + Lars', 'Polynomial Regression'],
            'Train Predictions': [221977.25, 221977.25, 220570.62],
            'Validate Predictions': [222972.52, 222972.52, 220216.19]}
    return pd.DataFrame(data)