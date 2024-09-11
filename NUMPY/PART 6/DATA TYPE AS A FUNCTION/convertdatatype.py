# import numpy as np
# x = np.array([1, 2, 3, 4])
# print("Data type : ", x.dtype) # int



# # Convert 
# import numpy as np
# x = np.array([1, 2, 3, 4], dtype = np.int8)
# print("Data type : ", x.dtype) # int
# print(x)


# Convert  this int into a float data type
# import numpy as np
# x1 = np.array([1, 2, 3, 4], dtype = "f") # dtype = "f" => convert into a float
# print("Data type : ", x1.dtype) # int
# print(x1)




# import numpy as np

# x2 = np.array([1, 2, 3, 4]) 
# new = np.float32(x2)
# print("Data type : ", x2.dtype) # int
# print("Data type: ", new.dtype)
# print(x2)
# print(new)












import numpy as np

x2 = np.array([1, 2, 3, 4]) 
new = np.float32(x2) # change into a float
new_one = np.int_(new) # agian change into a integer
print("Data type : ", x2.dtype) # int
print("Data type: ", new.dtype)
print("Data type: ", new_one.dtype)

print(x2)
print(new)
print(new_one)
