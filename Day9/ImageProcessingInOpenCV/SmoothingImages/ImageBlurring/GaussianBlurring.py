import cv2 as cv
from matplotlib import pyplot as plt

#2. Gaussian Blurring
#In this method, instead of a box filter, a Gaussian kernel is used. It is done with the function, cv.GaussianBlur().
#We should specify the width and height of the kernel which should be positive and odd.


img = cv.imread('/opencv/doc/images/opticalfb.jpg')
blur = cv.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
