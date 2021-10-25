# Starter code illustrating how to make a regression model 

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
# Note you will need to open a terminal window and type: 'pip install for sklearn' to install the package 
# The first time you use it

# %%
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )


# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# %%
# Building an autoregressive model
# You can learn more about the approach I'm following by walking
# Through this tutorial
# https://realpython.com/linear-regression-in-python/

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

# Step 2 - pick what portion of the time series you want to use as training data
# here I'm grabbing the first 800 weeks
# Note1 - dropping the first two weeks since they wont have lagged data
# to go with them
train = flow_weekly[2:800][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[800:][['flow', 'flow_tm1', 'flow_tm2']]

# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
# See the tutorial to understand the reshape step here
x = train['flow_tm1'].values.reshape(-1, 1)
y = train['flow'].values
model.fit(x, y)

#Look at the results
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

#print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Step 4 Make a prediction with your model
# Predict the model response for a  given flow value
q_pred_train = model.predict(train['flow_tm1'].values.reshape(-1, 1))
q_pred_test = model.predict(test['flow_tm1'].values.reshape(-1, 1))

#alternatievely you can calcualte this yourself like this:
q_pred = model.intercept_ + model.coef_ * train['flow_tm1']

# you could also predict the q for just a single value like this
last_week_flow = 500
prediction = model.intercept_ + model.coef_ * last_week_flow


# %%
# Another example but this time using two time lags as inputs to the model
model2 = LinearRegression()
x2 = train[['flow_tm1', 'flow_tm2']]
model2.fit(x2, y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

# generate preditions with the funciton
q_pred2_train = model2.predict(train[['flow_tm1', 'flow_tm2']])

# or by hand
q_pred2 = model2.intercept_   \
    + model2.coef_[0] * train['flow_tm1'] \
    + model2.coef_[1] * train['flow_tm2']


# %%
# Plot up the models

# 3. Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred_train, color='green', linestyle='--',
        label='simulated 1 lag')
ax.plot(train.index, q_pred2_train, color='blue', linestyle='--',
        label='simulated 2 lag')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.legend()
