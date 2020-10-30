import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x, y) ) # 250+10 = 260 => 255

print( x + y )   # 250+10 = 260 % 256 = 4
