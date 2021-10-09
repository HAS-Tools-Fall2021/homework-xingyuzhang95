# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import dataretrieval.nwis as nwis
#note you may need to do pip install for sklearn


# %%
# Set the file name and path to where you have stored the data

filename = 'streamflow_week7.txt'
filepath = os.path.join('..\Code_Review1', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek


# %% 
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed weekly flow values
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], color='blue',
        linestyle='dashed', label='daily')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Daily Avg Flow [cfs]",
        yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(5,3)
fig.savefig("p1_time_series_daily.png")

# %% 
#2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], label='weekly')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2014, 1, 26), datetime.date(2020, 10, 1)])
ax.legend()
plt.show()
fig.savefig("p2_time_series_2014.png")
# %% 
#3 Boxplot of flows by month 
def generate_boxplot(variable_x,variable_y):
    fig, ax = plt.subplots()
    ax = sns.boxplot(x=variable_x, y=variable_y,  data=data,orient='h',\
                    linewidth=0.3)
    ax.set(xscale='log')
    # Here i'm separating out the x lable and ylable setting just as an illustration
    # They also could have been included in the ax.set command above
    ax.set_xlabel(variable_x)
    ax.set_ylabel(variable_y)
    return fig
#%%
fig=generate_boxplot("flow","month")
plt.show()
fig.savefig("p3_boxplot_monthly_diff.png")

#Figure out how to do multi conditionals

# %%
