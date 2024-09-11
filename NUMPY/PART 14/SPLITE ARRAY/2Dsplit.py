import numpy as np 

var1 = np.array([[1,2],[3,4],[5,6]])
print(var1)
print()

ar1 = np.array_split(var1, 3) # (var, 3 (-->> part splite))
ar2 = np.array_split(var1, 3, axis = 1) # (var, 3 (-->> part splite))

print()
print(ar1)
print(type(ar1))
print()
print(ar2)

