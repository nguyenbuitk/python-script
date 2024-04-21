import cv2
import numpy as np
array = cv2.imread("capture_image.png")
flattened_array = array.reshape(-1, array.shape[-1])
np.savetxt('output.txt', flattened_array, fmt='%d')
print(flattened_array)