import numpy as np

var_3 = np.array(["a", "s", "d", "f"])
f = [True, False, True, False]
new_a = var_3[f]
print(new_a) # only true value written
print(type(new_a))