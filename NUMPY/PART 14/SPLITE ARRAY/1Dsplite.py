import numpy as np 

var = np.array([1,2,3,4,5,6])
print(var)
print()

ar = np.array_split(var, 3) # (var, 3 (-->> part splite))
print()
print(ar)
print(type(ar))
print()

print(ar[0])