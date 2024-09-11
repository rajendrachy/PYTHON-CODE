import numpy as np

var1 = np.array([[1,2,3], [1,2,3]])
# v = np.insert(var1, 2, 6, axis = 0) 
# v = np.insert(var1, 2, 6, axis = 1) 
v = np.append(var1, 6, 5) # used in the 1D array

print(v)