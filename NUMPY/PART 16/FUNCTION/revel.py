import numpy as np

var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2, (2,3)) # (rows , cols)
print(y) # 2 D array

print("Flatten : ",y.flatten(order="F")) # again 1D array
print("Revel: ", np.ravel(y, order="K"))