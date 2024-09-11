# Heading -->> array 

# import numpy as np
# x = [1, 2, 3, 4]
# y = np.array(x)
# print(y) #[1 2 3 4]

# import numpy as np
# x = np.array([1, 2, 3, 4])
# print(x) # [1 2 3 4]
# print(type(x)) # nuppy.ndaray




# -----------user impt-------------
import numpy as np
l = []
for i in range(1,5):
    int_1 = int(input("Enter a value : ")) # using int -->> give an integer value
                                            # without using int -->> string value written
    l.append(int_1)

print(np.array(l))
print(type(np.array(l)))    


