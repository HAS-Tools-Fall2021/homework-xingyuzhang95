header:
name: Xingyu Zhang
date: Sep 27th
assignment number: 5th

##Don't forget to grade my hw4 and cheatsheet2.



1. Provide a summary of the data frames properties.
What are the column names?

Index(['agency_cd', 'site_no', 'datetime', 'flow', 'code', 'year', 'month',
       'day'],
      dtype='object')

What is its index?


RangeIndex(start=0, stop=11944, step=1)

What data types do each of the columns have?

agency_cd     object
site_no        int64
datetime      object
flow         float64
code          object
year           int32
month          int32
day            int32
dtype: object

2. Provide a summary of the flow column including the min, mean, 
max, standard deviation and quartiles.

count    11944.000000
mean       341.126482
std       1391.845646
min         19.000000
25%         93.500000
50%        157.000000
75%        214.000000
max      63400.000000
Name: flow, dtype: float64

3. Provide the same information but on a monthly basis.
(Note: you should be able to do this with one or two lines of code)

	    flow
        count mean	    std	        min	     25%	50%	     75%	max
month								
1	1023.0	691.002933	2708.527013	158.0	201.000	218.0	285.00	63400.0
2	932.0	903.156652	3300.470852	136.0	200.000	238.0	615.75	61000.0
3	1023.0	919.477028	1625.606804	97.0	178.000	368.0	1045.00	30500.0
4	990.0	295.596970	540.712365	64.9	111.250	140.0	210.00	4690.0
5	1023.0	104.410850	50.394386	46.0	77.050	92.0	117.50	546.0
6	990.0	65.534949	28.660493	22.1	48.925	60.0	76.55	481.0
7	1023.0	108.447312	219.942070	19.0	53.500	71.0	112.50	5270.0
8	1023.0	171.500782	295.999467	29.6	77.950	116.0	178.00	5360.0
9	982.0	171.050815	283.185580	37.5	88.525	119.0	169.75	5590.0
10	992.0	144.094556	110.663378	59.8	104.750	124.0	152.25	1910.0
11	960.0	203.198958	232.211365	117.0	154.000	174.0	198.00	4600.0
12	992.0	331.986895	1080.358791	155.0	190.000	203.0	226.00	28700.0

4. Provide a table with the 5 highest and 5 lowest flow values for 
the period of record. Include the date, month and flow values in 
your summary.

agency_cd	    site_no	datetime	flow    code year month	day
1468	USGS	9506000	1993-01-08	63400.0	A:e	1993	1	8
1511	USGS	9506000	1993-02-20	61000.0	A	1993	2	20
2236	USGS	9506000	1995-02-15	45500.0	A	1995	2	15
5886	USGS	9506000	2005-02-12	35600.0	A	2005	2	12
2255	USGS	9506000	1995-03-06	30500.0	A	1995	3	6

agency_cd	    site_no	datetime	flow   code	year  month	day
8584	USGS	9506000	2012-07-03	23.4	A	2012	7	3
8580	USGS	9506000	2012-06-29	22.5	A	2012	6	29
8581	USGS	9506000	2012-06-30	22.1	A	2012	6	30
8583	USGS	9506000	2012-07-02	20.1	A	2012	7	2
8582	USGS	9506000	2012-07-01	19.0	A	2012	7	1

5. Find the highest and lowest flow values for every month of the 
year (i.e. you will find 12 maxes and 12 mins) and report back 
what year these occurred in.

minyears [2003. 1991. 1989. 2018. 2004. 2012. 2012. 2019. 2020. 2020. 2016. 2012.]
maxyears [1993. 1993. 1995. 1991. 1992. 1992. 2021. 1992. 2004. 2010. 2004. 2004.]

6. Provide a list of historical dates with flows that are within 
10% of your week 1 forecast value. If there are none than increase 
the %10 window until you have at least one other value and report 
the date and the new window you used

There has a total of 2198 historical dates with flows that are within 10% of my week 1 forecast value (200cfs). See more details in the python script.


####Forecasting numbers

I made my forecast predictions based off the averages throughout the
end of September. Over the weekend it was around 100 and there will 
be more rain throughout the week to keep the flow around that average.
Weeks 5 forecast guess was 100 cfs and the second weeks forecast was
80 cfs. 