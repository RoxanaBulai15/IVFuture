import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#OpenCV provides four main types of blurring techniques:

#1. AVERAGING
#It simply takes the average of all the pixels under the kernel area and replaces the central element.
# This is done by the function cv.blur() or cv.boxFilter()


#img = cv.imread('/opencv/doc/images/opticalfb.jpg')
img= cv2.imread('dog.jpg')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

