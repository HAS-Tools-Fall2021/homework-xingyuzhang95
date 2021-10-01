# %%
# Pandas Indexing Exercise 1
# start with the following dataframe of all 1's
import numpy as np
import pandas as pd
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. Change the values for all of the vowel rows to 3
# 2. Multiply the first 4 rows by 7
# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc
# 4. Same question as 3 but without using loc

# %%
# 1. Change the values for all of the vowel rows to 3
data_frame.loc[['a','e']]=3
data_frame
# %%
# 2. Multiply the first 4 rows by 7
data_frame.iloc[:4,]=data_frame.iloc[:4,]*7
#data_frame.iloc[:4,]*=7
data_frame
# %%
# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc
