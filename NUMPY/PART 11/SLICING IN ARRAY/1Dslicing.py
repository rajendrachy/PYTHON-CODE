import numpy as np

var = np.array([1,2,3,4,5,6,7])
#               0,1,2,3,4,5,6 => indexing
print(var)

print()

print("2 to 5 array is : ", var[1:5]) #(start, end)
print("2 to End : ", var[1:]) #( start, end -> blank)

print("start to 5 : ", var[:5])
print("stop point : ", var[::2]) # ( start, end, stop)
print("stop: ", var[1:5:2])  # ( start, end, stop)


