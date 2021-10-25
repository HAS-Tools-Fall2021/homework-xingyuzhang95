# Part 1 of data loading notes: 
# Options for loading streamflow data

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
import datetime
import os
import json 
import urllib.request as req
import urllib
import dataretrieval.nwis as nwis
from matplotlib.gridspec import GridSpec
# %%
# There are 3 ways to read data: 
# 1) Load a file that you have locally using read_table
# 2) Read a file using a URL for a Rest API using read_table 
# 3) Useing packages for specific APIs


#%%
#Note that we can also use this to make our URL within our code
station_id = "09506000"
start='1989-01-01'
end='2021-10-23'
strfdata = nwis.get_record(sites=station_id, service='dv', start=start, end=end, parameterCd='00060')
strfdata.columns = ['flow','agency_cd','site_no']

# What we are doing here is actually just interacting with the USGS's
# Rest API:
# Application Programming Interface: Application Programming Interface
# RESTful API is composed of a URL and the associated parameters
# We were just building the call to that API ourselves. 
#%%
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.448&lon=-111.789" \
       "&vars=prcp&years=&format=csv"
data = pd.read_table(url, delimiter=',', skiprows=6)

# Drop data before 1989 so we can match the time with USGS streamflow data
data.drop(data[data['year']<1989].index,inplace=True)

# Generate datetime and set it as data.index
data['datetime'] = data['year'].astype(str)+data['yday'].astype(str)
data.set_index(data.index-3285, inplace=True)

# %%
for ii in np.arange(0,11680):
     temp = datetime.datetime.strptime(data['datetime'][ii], '%Y%j').strftime('%Y-%m-%d')
     data['datetime'][ii] = datetime.datetime.strptime(temp, '%Y-%m-%d')

data['datetime']
data.set_index(data['datetime'], inplace=True)
data.drop(columns=['datetime', 'year', 'yday'], inplace=True)
data.columns = ['prcp']
# %%
W_prcp     = data.resample('W').mean()
W_strfdata = strfdata.resample('W').mean()
W_prcp     = W_prcp[W_prcp.index.year < 2021]
W_strfdata = W_strfdata[W_strfdata.index.year < 2021]

# Generate two y axis plot
# %%

#%%
fig=plt.figure(figsize=(30,12))

gspec = GridSpec(ncols=1, nrows=2, figure=fig)#, width_ratios=[2, 3])
#=-=-=-=-=-=-=-=-=-=-=-=    
ax=fig.add_subplot(gspec[0])
ax.plot(W_strfdata.index, W_strfdata['flow'], color='red')
ax.set(ylabel = 'Streamflow (m^3/s)', yscale = 'log',title = 'Weekly mean streamflow and precipitation')

ax.tick_params(labelsize=30,length=10,width=5,direction='in',which='major',right=True,top=True,labelcolor='red')
ax.tick_params(length=7,width=3,direction='in',which='minor',right=True,top=True)

ax1.set_ylabel('precipitation (mm)',fontsize=30,fontweight='bold',color='red')

ax2=fig.add_subplot(gspec[1])
ax2.plot(W_prcp.index, W_prcp['prcp'])
ax2.set(ylabel = 'Precipitation (mm/day)', xlabel = 'Year', ylim=(0, 20.0))
ax2.tick_params(labelsize=30,length=10,width=5,direction='in',which='major',right=True,top=True)
ax2.tick_params(length=7,width=3,direction='in',which='minor',right=True,top=True)


fig.savefig('two_yaxis_prcp_flow.jpg', dpi=300, bbox_inches='tight')
# %%
# Build an autoregressive model 
W_strfdata = strfdata.resample('W').mean()
W_strfdata['flow_tm1'] = W_strfdata['flow'].shift(1)
W_strfdata['flow_tm2'] = W_strfdata['flow'].shift(2)
W_strfdata['flow_tm3'] = W_strfdata['flow'].shift(3)

# Using the entire flow data  
train = W_strfdata[3:][['flow', 'flow_tm1', 'flow_tm2','flow_tm3']]

# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1', 'flow_tm2','flow_tm3']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

#print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction
prediction = model.predict(train[['flow_tm1', 'flow_tm2','flow_tm3']])
print(" This week mean flow is ", round(prediction[0], 1))
print(" This week mean flow is ", round(prediction[1], 1))
#
# %%
# Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots()
ax.scatter(W_strfdata['flow'][3:], prediction, marker='o', alpha=0.05,
            color='blue', label='simulated 3 lag')
ax.set(title="Linear regression flow results", xlabel="Observation (cfs)", ylabel="Simulation with 3 lag (cfs)",
       yscale='log', xscale='log', xlim=(0,15000), ylim=(0,15000))
ax.set_aspect('equal', adjustable='box')
ax.legend()
plt.show()

fig.savefig('lm.jpg', dpi=300)

# %%
