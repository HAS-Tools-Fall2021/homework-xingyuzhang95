
# %%
# Import the modules we will use

import numpy as np

# %%
##create
matrix=np.random.randn(6,12)
# %%
print(np.mean(matrix),np.std(matrix))
# %%
print(np.mean(matrix[:,2]),np.std(matrix[:,2]))

# %%
for i in range(matrix.shape[0]):
    print((i+1),'raw',np.mean(matrix[i,:]))
for j in range(matrix.shape[1]):
    print((j+1),'colomn',np.mean(matrix[:,j]))
# %%
