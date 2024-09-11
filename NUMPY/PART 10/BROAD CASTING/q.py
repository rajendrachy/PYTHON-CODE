import numpy as np

var1 = np.array([1,2,3]) # (1 * 3) => matrix
print(var1.shape)
print()
print(var1)
print()

var2 = np.array([[1], [2], [3]]) # (3 * 1) => matrix
print(var2.shape)
print()
print(var2)
print()
print(var1 + var2) # 3  * 3 new array made while print the array
