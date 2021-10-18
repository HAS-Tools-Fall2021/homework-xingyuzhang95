# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter

# %%

filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# Read in our data as a dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     )

# Read in our data as a dataframe - making the dates into a dattime object
data2 = pd.read_table(filepath, sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],
                              parse_dates =['datetime']
                      )


#note that in data2 the column called 'datetime' is a datetime
print(data.info())
print(data2.info())

# Also could have done this like this
print(data.dtypes)
print(data2.dtypes)

# %%
# In your previous starter codes I used date time properties to 
# Parse out the year-month-day info from the dates like this:
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
# Datetimes plot much more nicely!
plot_data= data.iloc[0:365]
plot_data2  = data2.iloc[0:365]

# See that the x axis does not look good for this plot because
# the dates aren't datetimes
fig, ax = plt.subplots()
ax.plot(plot_data['datetime'], plot_data['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')

# Here they look much  better
fig, ax = plt.subplots()
ax.plot(plot_data2['datetime'], plot_data2['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')


# and  we can plot the entire timeseries and it will adjust accordingly
fig, ax = plt.subplots()
ax.plot(data2['datetime'], data2['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')


# %% 
# Setting your date as the index of the dataframe
datai = data2.copy()
datai = datai.set_index('datetime')
datai.head()
data2.head()

# Now I can plot this even more easily
# it will assume my x axis is the index
fig, ax = plt.subplots()
ax.plot(datai['flow'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')


# %%
# Setting a column as datatime after the fact
data3 = data.copy()
print(data3.dtypes)
data3['datatime'] = pd.to_datetime(data3['datetime'])
print(data3.dtypes)

# %%
# With datetimes we can easily subset our values using the date info
#Grab out just a year or a month 
datai["2013"].head()
datai[datai.index.month == 5]
datai['2013-01-01':'2020-08-31'].head()

#See only the year component of the date
datai.index.year
datai.index.month
datai.index.day
datai.index.dayofweek

#If its not the index you can  still do this for any column
# its just a little more  complicated
pd.DatetimeIndex(data2['datetime']).year

# or grab out any date you want
datai.loc["1989-01-01"]

# or for a range of dates
datai.loc["1989-01-01":"1989-01-07"]


# %%
# the best part is resampling though!!
data_w = datai.resample("w").mean()
data_wmax = datai.resample("w").max()

print(data_w.head())
print(data_wmax.head())


# If your datetime is not the index thats okay you can still 
# point it to a column like this
data_w2 = data2.resample("W", on='datetime').mean()

# or we could do it annually
data_y2 = data2.resample("Y", on='datetime').mean()


#%%
# You can also control the formatting that is used

#Selecting the date format I would like here
date_form = DateFormatter("%Y/%d")

fig, ax = plt.subplots()
ax.plot(datai.flow['2001'])
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]",
       yscale='log')
ax.xaxis.set_major_formatter(date_form)


# %%

#data_flow=datai[datai.index.month==10]
Oct_mean=datai.groupby(datai.index.day).median
Oct_max=datai.groupby(datai.index.day).max
# %%
