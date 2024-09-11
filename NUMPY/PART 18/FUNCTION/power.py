import numpy as np

var4  = np.matrix([[1,2], [3,4]])
print(var4)
print()

print(np.linalg.matrix_power(var4, 2)) # 2 time multiplr & put 0 and get identity matrix
