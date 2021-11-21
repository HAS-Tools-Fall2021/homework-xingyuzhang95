# Part 1 of data loading notes: 
# Options for loading streamflow data

# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import netCDF4 as nc
import string
import time
from glob import glob

#%%
impath='C:\\ZXY\\course\\HWRS501\\Forecasting21\\weekly_results\\'
files=glob(impath+'forecast'+'*.csv')
temp = pd.read_csv(files[0])
# %%
for x in range(1,11):
    filename = '../../Forecast21/weely_result/forecast_week'+str(x)+'_results.csv'
    filepath = os.path.join('../../Forecast21/weely_result', filename)
    temp = pd.read_csv(filename)