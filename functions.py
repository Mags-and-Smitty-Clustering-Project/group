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
from sklearn.cluster import KMeans
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

seed = 23

def density_quality(train):
    p = sns.stripplot(y = train.density, x = train.quality, data = train, size = 2, jitter = .4, palette = 'magma')
    sns.boxplot(showmeans=True,
                meanline=True,
                meanprops={'color': 'k', 'ls': '-', 'lw': 2},
                medianprops={'visible': False},
                whiskerprops={'visible': False},
                zorder=10,
                x="quality",
                y="density",
                data=train,
                showfliers=False,
                showbox=False,
                showcaps=False,
                ax=p)
    plt.ylabel('Density Level', fontdict = { 'fontsize': 15})
    plt.xlabel('Wine Quality', fontdict = { 'fontsize': 15})
    plt.title('Does Density Affect Wine Quality', fontdict = { 'fontsize': 20})
    plt.show()

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
        


def cluster_sugar_acid(sugar_acid_df):
    df = sugar_acid_df[['rs', 'citric_acid']]
    
    kmeans = KMeans(n_clusters= 3, random_state = seed)

    kmeans.fit(df)

    kmeans.predict(df)
    
    sugar_acid_df['sugar_acid'] = kmeans.predict(df)
    
    sns.relplot(y = 'rs', x = 'citric_acid', hue = 'sugar_acid', palette = 'Accent', data = sugar_acid_df)
    
    plt.show()   
        
def sugar_acid_compare(train_scaled):        
    sns.countplot(train_scaled['sugar_acid'], hue = train_scaled.quality, palette = 'Accent')
    plt.ylabel('Number of Wines')
    plt.xlabel('Sugar and Citric Acid Group')
    plt.title('Are Residual Sugar and\n Citric Acid Related to Quality')
    labels = ['High Acid\nLow Sugar', 'Medium Acid\nHigh Sugar', 'Low Acid\nLow Sugar']
    plt.xticks(ticks = (0, 1, 2), labels = labels)
    plt.show()
        
def cluster_sulphites(sulphites_df):
    df = sulphites_df[['free_s02', 'total_s02']]
    
    kmeans = KMeans(n_clusters= 3, random_state = seed)

    kmeans.fit(df)

    kmeans.predict(df)
    
    sulphites_df['sulphites'] = kmeans.predict(df)
    
    sns.relplot(y = 'free_s02', x = 'total_s02', hue = 'sulphites', palette='Accent', data=sulphites_df)
    
    plt.show()   

    
def sulphites_compare(train_scaled):
    c = sns.diverging_palette(300, 10, s = 90)
    sns.countplot(train_scaled['sulphites'], hue = train_scaled.quality, palette = c, orient = "h")
    plt.ylabel('Number of Wines')
    plt.xlabel('Free and Total S02 Groupings')
    plt.title('Are Free and Total S02 Levels\nGood Indicators of Quality?')
    labels = ['Low Free\nLow Total S02', 'High Free\nHigh Total S02', 'Low Free\nHigh Total S02']
    plt.xticks(ticks = (0, 1, 2), labels = labels)
    plt.show()
     
        
def cluster_sug_dens(sug_dens_df):
    
    df = sug_dens_df[['rs', 'density']]

    kmeans = KMeans(n_clusters= 3, random_state = seed)

    kmeans.fit(df)

    kmeans.predict(df)

    sug_dens_df['sugar_dens'] = kmeans.predict(df)
    
    sns.relplot(y = 'rs', x = 'density', hue='sugar_dens', palette = 'Set1', data = sug_dens_df)
    
    plt.show()
        
    
def sugar_dens_compare(train_scaled):

    sns.countplot(train_scaled['sugar_dens'], hue = train_scaled.quality, palette = "Set1")
    plt.ylabel('Number of Wines')
    plt.xlabel('Sugar and Density Group')
    plt.title('Are Residual Sugar and\n Density Related to Quality')
    labels = ['High Density\nLow Sugar', 'Low Density\nLow Sugar', 'High Density\nHigh Sugar']
    plt.xticks(ticks = (0, 1, 2), labels = labels)
    plt.show()    
    
    
def model_report():
    data = {'Model': ['Linear Regression', 'Lasso + Lars', 'Polynomial Regression'],
            'Train Predictions': [221977.25, 221977.25, 220570.62],
            'Validate Predictions': [222972.52, 222972.52, 220216.19]}
    return pd.DataFrame(data)




def density_ols(df):

    # getting mean of target variable

    df['quality'].mean()

    # rounding and setting target variable name

    baseline_preds = round(df['quality'].mean(), 3)

    # create a dataframe

    predictions_df = df[['density', 'quality']]

    # MAKE NEW COLUMN ON DF FOR BASELINE PREDICTIONS

    predictions_df['baseline_preds'] = baseline_preds

    # our linear regression model

    ols_model = LinearRegression()

    ols_model.fit(df[['density']], df[['quality']])

    # predicting on density after it's been fit

    ols_model.predict(df[['density']])

    # model predictions from above line of codes with 'yhat' as variable name and append it on to df
    predictions_df['yhat'] = ols_model.predict(df[['density']])


    # computing residual of baseline predictions

    predictions_df['baseline_residual'] = predictions_df['quality'] - predictions_df['baseline_preds']


    # looking at difference between yhat predictions and actual preds ['quality']

    predictions_df['yhat_res'] = predictions_df['yhat'] - predictions_df['quality']


    # finding the RMSE in one step (x = original, y = prediction)

    dens_qual_rmse = sqrt(mean_squared_error(predictions_df['quality'], predictions_df['baseline_preds']))

    print(f'The RMSE on the baseline of density against wine quality is {round(dens_qual_rmse,4)}.')


    # RMSE of linear regression model

    OLS_rmse = mean_squared_error(predictions_df['yhat'], predictions_df['quality'], squared = False)

    print(f'The RMSE for the OLS Linear Regression model was {round(OLS_rmse, 4)}.')


