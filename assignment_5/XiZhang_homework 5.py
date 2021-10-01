# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week2.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :)
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# %%
#question 2
#use .describe
data.columns
flow=data["flow"]
np.mean(flow)
flow.mean()
flow.describe()
# %%

data_group=data.groupby(["month"])
groupflow=data_group["flow"]
groupflow.mean()
data.head(5)
data.tail(10)

datasort=data.sort_values(by="flow", ascending = True)
datasort.head(5)

#question 5
#Create space for min/max each month
maxyears=np.zeros(12)
minyears=np.zeros(12)

#month+1=Jan
for month in range(12):
        print(month) 
        monthdata=data[data["month"]==(month+1)]
        datasort=monthdata.sort_values(by="flow", ascending = True)
        minyears[month]=datasort["year"].head(1)
        maxyears[month]=datasort["year"].tail(1)
# %%