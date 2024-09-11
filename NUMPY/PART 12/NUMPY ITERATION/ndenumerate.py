
# index also written 
# ndenumerate
import numpy as np 

var3 = np.array([[[1,2,3,4], [1,2,3,4]]])
print(var3)
print(var3.ndim)
print()

for i,d in np.ndenumerate(var3):
    print(i, d)