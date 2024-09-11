import numpy as np

var = np.array([1, 2, 3, 4])
var1 = np.array([9, 8, 7, 6])

ar_new = np.stack((var, var1), axis = 1) #  When you set axis=1, it means that the input arrays will be stacked column-wise, or vertically.
ar_new1 = np.hstack((var, var1)) # row wise merged
ar_new2 = np.vstack((var, var1)) # cols wise merged
ar_new3 = np.dstack((var, var1)) # height wise merged

       # vstack -->> column wise merged
       # hstack -->> row wise merged
       # dstack -->> according to height merged
print(ar_new)
print()
print(ar_new1)
print()
print(ar_new2)
print()
print(ar_new3)