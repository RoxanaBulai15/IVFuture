#OpenCV also provides cv.drawKeyPoints() function
# which draws the small circles on the locations of keypoints.

import numpy as np
import cv2 as cv
img = cv.imread('house.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img)
cv.imwrite('sift_keypoints.jpg',img)