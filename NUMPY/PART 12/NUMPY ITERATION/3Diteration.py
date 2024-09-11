import numpy as np 

var3 = np.array([[[1,2,3,4], [1,2,3,4]]])
print(var3)
print(var3.ndim)
print()

for i in var3:
    for j in i:
        for k in j:
            print(k)