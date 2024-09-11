# reshape
# import numpy as np
# var2 = np.array([1,2,3,4,5,6])
# print(var2)
# print(var2.ndim) # 1

# print()

# x = var2.reshape(3, 2) # ( rows, cols)
# print(x)
# print(x.ndim) # 2  # blank row is not made in the numpy


# to make three dimensional 3 * 3 
# x1 = var2.reshape(2,3,2) 






# move on from n-dimension array to 1- D array in the pyhon

import numpy as np
var3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)


print()

x1 = var3.reshape(2, 3, 2) # ( rows, cols)
print(x1)
print()

one = x1.reshape(-1) # using -1 it should convert into a 1-D array
print(one)
print(one.ndim)
