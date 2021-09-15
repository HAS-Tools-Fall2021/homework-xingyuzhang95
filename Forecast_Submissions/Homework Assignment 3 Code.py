# Homework Assignment 3 Code
# Includes part of starter code from Laura Condon, HWRS 501, Fall 2021

# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections.

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%

# Forecast 3 Code

print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))


# 1 week prediction: 96 
# 2 week prediction: 84


if type(flow[27]) is int:
        print("is an integer")
elif type(flow[27]) is str:
        print("is a string")
elif type(flow[27]) is float:
        print("is a float")

len(flow)

if type(year[27]) is int:
        print("is an integer")
elif type(year[27]) is str:
        print("is a string")
elif type(year[27]) is float:
        print("is a float") 

len(year)

if type(month[27]) is int:
        print("is an integer")
elif type(month[27]) is str:
        print("is a string")
elif type(month[27]) is float:
        print("is a float")

len(month)

if type(day[27]) is int:
        print("is an integer")
elif type(day[27]) is str:
        print("is a string")
elif type(day[27]) is float:
        print("is a float") 

len(day)


#####################################

ilist = []      

for i in range(len(flow)):
        if flow [i] > 96 and month[i] == 8:
                ilist.append(i)

print(len(ilist))

jlist = []

for i in range(len(flow)):
        if flow [i] > 84 and month[i] == 8:
                jlist.append(i)

print(len(jlist))


######################################

klist = []

for i in range(len(flow)):
        if flow[i] > 96 and month[i] == 8 and year[i] <= 2000:
                klist.append(i)

print(len(klist))

mlist = []

for i in range(len(flow)):
        if flow[i] > 84 and month[i] == 8 and year[i] <= 2000:
                mlist.append(i)

print(len(mlist))


# The number of flow values between January 1st, 1989 and December 31st, 2000
# is 4382, but I could not figure out how to write a code to find this number.
# I just calculated it from the text file instead.

nlist = []

for i in range(len(flow)):
        if flow[i] > 96 and month[i] == 8 and year[i] >= 2010:
                nlist.append(i)

print(len(nlist))

olist = []

for i in range(len(flow)):
        if flow[i] > 84 and month[i] == 8 and year[i] >= 2000:
                olist.append(i)

print(len(olist))

# The number of flow values between January 1st, 2010 and September 13th, 2021
# is 4270, but I couldn't figure out how to write a code to find this number.
# I just calculated it from the text file instead.

ilist2 = [i for i in range(len(flow)) if month[i]==8 and day[i] <= 14]

subset = [flow[j] for j in ilist2]

print(np.mean(subset))



ilist3 = [i for i in range(len(flow)) if month[i]==8 and day[i] >= 15]

subset = [flow[j] for j in ilist3]

print(np.mean(subset))

# %%