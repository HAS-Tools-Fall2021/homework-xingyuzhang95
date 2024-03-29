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
#note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
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
fig, ax = plt.subplots()
ax = sns.boxplot(y="month", x="flow",  data=data,orient='h',
                 linewidth=0.3)
ax.set(xscale='log')
# Here i'm separating out the x lable and ylable setting just as an illustration
# They also could have been included in the ax.set command above
ax.set_xlabel('Flow (cfs)')
ax.set_ylabel('month')
plt.show()
fig.savefig("p3_boxplot_monthly_diff.png")
# %% 
# 4. Plot the september flows for the last 10 years
mypal = sns.color_palette('rainbow', 12)
fig, ax = plt.subplots()
colpick = 0
for i in range(2010, 2021):
        plot_data=data[(data['year']==i) &( data['month']==9)]
        ax.plot(plot_data['day'], plot_data['flow'], color=mypal[colpick],
                linestyle='dashed', label=str(i)+' Oct')
        colpick += 1
ax.set(yscale='log')
ax.set_xlabel('date')
ax.legend(fontsize=6)
fig.savefig("p4_time_series_daily.png")
# %% 
#5. scatterplot this years flow vs last years flow for september
fig, ax = plt.subplots()

ax.scatter(data[(data['year'] == 2019) & (data['month'] == 10)].flow,  data[(data['year'] == 2020) & (data['month'] == 10)].flow, marker='p',
           color='blueviolet')
ax.set(xlabel='2019 flow', ylabel='2020 flow',title="2019 Oct flow vs 2020")
ax.set_xlim(30,150)
ax.set_ylim(30,150)
ax.legend(fontsize=6)
fig.savefig("p5_scatter_Oct_flow.png")

# %%
#6. multiple hist using for loop
fig, ax = plt.subplots(1, 2)
ax= ax.flatten()  #so that we can refer to plots as ax[0]...ax[3] rather than ax[0,0]..ax[1,1]
axi = 0
month_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct",
                "Nov","Dec"]
for m in range(9,11):
        month_data = data[data['month'] == m]
        plot_title = month_list[m]
        ax[axi].hist(np.log10(month_data['flow']), bins=40,
           edgecolor='grey', color='purple')
        ax[axi].set(title=plot_title)
        #ax[axi].set(xlabel='Log(Flow) cfs', ylabel='count', title=plot_title)
        axi=axi+1

ax[0].set(xlabel='Log(flow) (cfs)',ylabel="Count")
ax[1].set(xlabel='Log(flow) (cfs)')
plt.show()

fig.set_size_inches(6,4)
fig.savefig("p6_OctvsNov_PDF.png",dpi=300)


#Figure out how to do multi conditionals

# %%
