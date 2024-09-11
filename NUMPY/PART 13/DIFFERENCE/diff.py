# # -----------------COPY--------------------

# import numpy as np

# var = np.array([1,2,3,4])
# co = var.copy()

# var[1] = 40
# print("Var: ", var) # change in the original data
# print("Copy : " , co) # Not change in the copy data



# -------------------VIEW---------------

# COPY

import numpy as np

var = np.array([1,2,3,4])
vi = var.view()

var[1] = 40
print("Var: ", var) # change in the original data
print("Copy : " , vi) #  change in the view data



