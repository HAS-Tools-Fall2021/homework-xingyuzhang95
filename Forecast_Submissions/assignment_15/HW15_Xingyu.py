#%%
pip install pandas
pip install numpy
pip install matplotlib
pip install sklearn
### For Window's Users
#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


from sklearn.linear_model import LinearRegression

## Insert flow data
flow_url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb" \
           "&site_no=09506000&referred_module=sw" \
           "&period=&begin_date=2020-01-01&end_date=2021-12-05"
flow_data = pd.read_table(flow_url, sep='\t', skiprows=30,
                          names=['agency_cd', 'site_no', 'datetime', 'flow',
                                 'code'], parse_dates=['datetime'],
                          index_col=['datetime'])
flow_data['month'] = pd.DatetimeIndex(flow_data.index).month
flow_data['day'] = pd.DatetimeIndex(flow_data.index).day
flow_data['year'] = pd.DatetimeIndex(flow_data.index).year
# %%
flow_mean = flow_data.resample('W').mean()
flow_mean['flow_tm1'] = flow_mean['flow'].shift(1)
flow_mean['flow_tm2'] = flow_mean['flow'].shift(2)

# Using the entire flow data
train = flow_mean[2:][['flow', 'flow_tm1', 'flow_tm2']]



# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1',  'flow_tm2']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# Print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction
prediction = model.predict(train[['flow_tm1', 'flow_tm2']])
print(" This week mean flow is ", round(prediction[0], 1))
print(" This week mean flow is ", round(prediction[1], 1))