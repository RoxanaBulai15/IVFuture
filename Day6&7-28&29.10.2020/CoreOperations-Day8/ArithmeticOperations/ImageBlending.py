import cv2 as cv

img1 = cv.imread('D:\IVFuture\opencv\doc\images\meanshift_basics.jpg')
img2 = cv.imread('D:\IVFuture\opencv\doc\images\meanshift_basics.jpg')
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()