import numpy as np

var1 = np.array([1,2,3,4,6,7,8,9,10])
#                0,1,2,3,4,5,6,7,8,9 --> indexing

var1 = np.array([1,2,3,4,8,9,10])
#                0,1,2,3,4,5,6,7--> indexing




#x1 = np.searchsorted(var1, 5, side="right") # 5 element should be placed inthe index 4 in shorted order 
x1 = np.searchsorted(var1, [5,6,7], side="right") # 5 element should be placed inthe index 4 in shorted order 

print(x1) # return the index