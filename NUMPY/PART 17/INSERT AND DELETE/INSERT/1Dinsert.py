import numpy as np

var = np.array([1,2,3,4])
print(var)

# v = np.insert(var, 2, 40) # (var, position or index, value to insert)
# v = np.insert(var, (2,4), 40) # (var, position or index, value to insert)
v = np.insert(var, (2,4), 6.5) # float value is not accepted , it should convert into a int value


print("INSERT : ", v)

print(type(var))
print(var.dtype)
