import numpy as np

arr = np.array([1, 2 , 3, 4, 2, 5, 2, 6, 2, 7])
u_e, indices = np.unique(arr, return_index=True)

print("Unique elements:", u_e)
print("Indices:", indices)