#We will learn to create a depth map from stereo images.
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
imgL = cv.imread('library.jpg',0)
imgR = cv.imread('library.jpg',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()