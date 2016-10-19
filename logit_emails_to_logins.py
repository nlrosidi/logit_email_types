import pandas as pd 
import statsmodels.api as sm 
import pylab as pl 
import numpy as np


'''Cleaning and preparing the data

'''
# load the data into a DataFrame
df =pd.read_csv('emails.csv')

# ensure that the dataset loaded successfully
print df.head()

# remove the user_id column since it's not needed for our regression
del df['user_id']

# print out some descriptive statistics to get a sense of the data
print df.describe()

# since we're using statsmodels, we need to manually add the intercept
df['intercept'] = 1.0


'''Performing the regression

'''
# identify the independent variables
ind_vars = df.columns[1:]

#train on dependent variables
logit = sm.Logit(df['login'], df[ind_vars])

# fit the model and print out the output summary
result = logit.fit()
print result.summary()

# output the odds ratios and 95% CI
conf = result.conf_int()
conf['odds_ratio'] = result.params
conf.columns = ['2.5%', '97.5%', 'odds_ratio']
print np.exp(conf)