import numpy as np
import cv2 as cv
img = cv.imread('D:\IVFuture\opencv\doc\images\camshift_result.jpg')

#Putem accesa un Pixel, indicand randul si coloana
px = img[100,100]
print( px )

# accessing only blue pixel
blue = img[100,100,0]
print( blue )

#You can modify the pixel values the same way.
img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)
59
# modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2))
100

cv.imshow("Display window", img)
k = cv.waitKey(0)