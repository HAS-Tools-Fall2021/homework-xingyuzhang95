# Part 1 of data loading notes: 
# Options for loading streamflow data

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis
#%%
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# %%
# There are 3 ways to read data: 
# 1) Load a file that you have locally using read_table
# 2) Read a file using a URL for a Rest API using read_table 
# 3) Useing packages for specific APIs

# %%
# So far we have been using the function pd.read_table to load data
# Checkout this link to see all the options https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# We can read csv and excel files directly 

filename = 'streamflow_week1.txt'
filepath = os.path.join('../../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime'
                     )


# %%
# Option two - We can actually just read dirctly from the URL that this is comming from
# NOTE: this only works when its formatted as something readable. 
# See what happens if you click table rather than tab separated. 

# Start from the USGS website for this gauge: 
#https://waterdata.usgs.gov/nwis/dv?referred_module=sw&site_no=09506000

#After we do the selections we want and say go we would get taken to the following URL
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-16"
# We should break the URL up onto multiple lines so it will be easier to read
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000" \
       "&referred_module=sw&period=&begin_date=1989-01-01&end_date=2020-10-16"

# Now we can read it with read_table command the same as we did before  
# (note run this without the skiprows and names to show what those are doing)
data2 = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],)


#Note that we can also use this to make our URL within our code
site = '09506000'
start = '1989-01-01'
end = '2020-10-16'
url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
      "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
data3 = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],)

# What we are doing here is actually just interacting with the USGS's
# Rest API:
# Application Programming Interface: Application Programming Interface
# RESTful API is composed of a URL and the associated parameters
# We were just building the call to that API ourselves. 

# %%
# Option 3: Use a package to interact with the API for us
# Here we are using the NWIS package
station_id = "09506000"
start_date = '1989-01-01'
stop_date = '2020-10-16'
# Note that this actually gets it in a slightly better format for us
# we don't have to specify the column names it already knows
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date, parameterCd='00060')

#Lest see what the NWIS package is doing!
# From terminal type the following to see where your evn lives
# conda env list 
# your packages will be within this folder in /lib/python/sitepackages
# add the folder for this package to your vs code env and you can see 
# what the package is doing
