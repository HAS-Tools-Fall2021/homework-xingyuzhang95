# Instructions for how to search for gridded climate data
# at NOAA: Physical Sciences Lab
# https://psl.noaa.gov/data/gridded_help/howtosub.html 
# 
# Search page (highlight multiple variables: Air Temperuature, 
# Precipitation, Precipitation Amount, Precipitation Rate)
# https://psl.noaa.gov/cgi-bin/db_search/SearchMenus.pl
#
# Select NCEP Reanalysis (chosen for the long & most recent records) 
# 
# Click "Make a plot or subset"
# Subset to a time & lat/lon range, data is 1deg x 1deg
# 1990-01-01-00Z : 2020-10-20-00Z
# 34-36N, 247-249E 
# 
# Output options: create a plot first, this will ensure that 
# you've selected a small enough subset that is downloadable 
# in your browser. 
#
# Then click, "FTP the data used to generate this plot", and 
# "FTP a copy of the file" (file size: ~ 2Mb)

# My example: 
# https://psl.noaa.gov/cgi-bin/GrADS.pl?dataset=NCEP%20Reanalysis%20Daily%20Averages;DB_did=195;file=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface_gauss%2Fpevpr.sfc.gauss.1948.nc%20pevpr.sfc.gauss.y4.nc%20105513;variable=pevpr;DB_vid=3174;DB_tid=89283;units=W%2Fm2;longstat=Mean;DB_statistic=Mean;stat=;lat-begin=88.54S;lat-end=88.54N;lon-begin=0.00E;lon-end=358.13E;dim0=time;year_begin=1948;mon_begin=Jan;day_begin=1;year_end=1948;mon_end=Jan;day_end=1;X=lon;Y=lat;output=file;bckgrnd=black;use_color=on;fill=lines;cint=;range1=;range2=;scale=100;maskf=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface%2Fland.nc;maskv=Land-sea%20mask;submit=Create%20Plot%20or%20Subset%20of%20Data;time-begin=1%20Jan%201%201948;time-end=1%20Jan%201%201948
#
# Repeat for other variables          

precip_reanal_file = 'data/NCEP_reanalysis_prrate_19900101_20200930.nc'
temp_reanal_file   = 'data/NCEP_reanalysis_temp_19900101_20200930.nc''

# use netCDF4.Dataset to read in .nc file
precip_reanal_data = Dataset(precip_reanal_file)
temp_reanal_data = Dataset(temp_reanal_file)
# find varibale names and dimesions
print(precip_reanal_data.variables)
print(temp_reanal_data.variables)
# extract specific variables: lats, lons and precip
precip_reanalysis = precip_reanal_data.variables['prate'][:, 0, 0]*86400
temp_reanalysis = (temp_reanal_data.variables['air'][:, 0, 0]-273.15)*(9./5.)+32

# %%
precip_reanalysis_s = pd.Series(precip_reanalysis,index=pd.date_range(start='1/1/1990', end='30/09/2020',tz='UTC'))
temp_reanalysis_s = pd.Series(temp_reanalysis,index=pd.date_range(start='1/1/1990', end='30/09/2020',tz='UTC'))

df_reanalysis = pd.DataFrame({"Reanalysis Temp":temp_reanalysis_s, "Reanalysis Precip":precip_reanalysis_s}, index=precip_reanalysis_s.index)
#%%

fig, ax1 = plt.subplots(1,1,figsize=(6,4),sharex=True)
df_reanalysis["Reanalysis Temp"].plot(ax=ax1, color='r', label='Temperature')
ax2 = ax1.twinx() 
df_reanalysis["Reanalysis Precip"].plot(ax=ax2, color='b', label='Precipitation')
ax1.set_ylabel('Temp [$\\mathrm{^\circ F}]$')
ax2.set_ylabel('Precip [$\\mathrm{mm}]$')
ax1.legend(loc=2)
ax2.legend(loc=1)
plt.show()
