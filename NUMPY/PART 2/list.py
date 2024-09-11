import numpy as np
import time

start_time = time.time()
result = np.arange(1, 9)**4
end_time = time.time()

print(f"Execution time: {end_time - start_time:.6f} seconds")
print(result)