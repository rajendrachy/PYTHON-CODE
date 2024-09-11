# without using a for loop in the 3 D array
# using a nditer function
import numpy as np 

var3 = np.array([[[1,2,3,4], [1,2,3,4]]])
print(var3)
print(var3.ndim)
print()

for i in np.nditer(var3):
    print(i)