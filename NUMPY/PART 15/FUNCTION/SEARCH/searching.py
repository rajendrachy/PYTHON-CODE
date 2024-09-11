import numpy as np

var = np.array([1,2,3,4,2,5,2,5,6,7])
#               0,1,2,3,4,5,6,7,8,9 --> indexing
x = np.where(var == 2) # where is used to search the element in the array
y = np.where((var % 2) == 0)
                       # written the index
print(x)
print()
print(y)