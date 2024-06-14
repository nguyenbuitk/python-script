import numpy as np

arr = np.array([1, 2, 3, 4, 5])
np.savetxt('output.txt', arr, fmt='%d')
print(arr)

print(type(arr))