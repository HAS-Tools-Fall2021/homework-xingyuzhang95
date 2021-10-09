# %%

import numpy as np
import pandas as pd
#From Laura Condon to Everyone:  08:15 AM
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
###write a for loop to calculate the average flow for everyday in Oct
day_average=np.zeros(31)
for i in range(31):
    grab_data=data[(data['month']==10)&(data['day']==i+1)]
    day_average[i]=round(np.mean(grab_data['flow']),2)
# %%
Oct=data[data['month']==10]
oct_mean=Oct.groupby['day'].mean()['flow']

# %%
def  day_average(data, month):
    day_average=np.zeros(31)
    for i in range(31):
        grab_data=data[(data['month']==month)&(data['day']==i+1)]
        day_average[i]=round(np.mean(grab_data['flow']),2)
# %%