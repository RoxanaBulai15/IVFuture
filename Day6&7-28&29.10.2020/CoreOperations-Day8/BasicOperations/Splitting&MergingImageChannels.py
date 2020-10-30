import cv2 as cv
img = cv.imread('D:\IVFuture\opencv\doc\images\camshift_result.jpg')

# !!! Warning
# cv.split() is a costly operation (in terms of time). So use it only if necessary. Otherwise go for Numpy indexing.

#b,g,r = cv.split(img)
#img = cv.merge((b, g, r))
# or b = img[:,:,0]

img[:,:,2] = 0

#cv.imshow("Display window", b)
#cv.imshow("Display window", g)
#cv.imshow("Display window", r)
cv.imshow("Display window", img)
k = cv.waitKey(0)