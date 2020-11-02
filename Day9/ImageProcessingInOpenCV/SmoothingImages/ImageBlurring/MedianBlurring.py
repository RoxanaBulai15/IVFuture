#3. Median Blurring
#Here, the function cv.medianBlur() takes the median of all the pixels under the kernel area
#and the central element is replaced with this median value.

import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('/opencv/doc/images/opticalfb.jpg')
median = cv.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
