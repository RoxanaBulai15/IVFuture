import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv.line(img, (0,0), (511,511), (255,0,0), 5)
cv.line(img, (0,0), (0,511), (255,0,0), 5) #latura verticala din stanga
cv.line(img, (0,0), (511,0), (255,0,0), 5) #latura orizontala de sus
cv.line(img, (0,511), (511,511), (255,0,0), 5) #latura orizontala de jos
cv.line(img, (511,0), (511,511), (255,0,0), 5) #latura verticala din dreapta
cv.line(img, (0,511), (511,0), (255,0,0), 10) #cealalta diagonala

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.rectangle(img,(0,0),(50,50),(0,255,0),3)

cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.circle(img,(0,0), 10, (0,0,255), -1)
cv.circle(img,(50,50), 10, (0,0,255), -1)
cv.circle(img,(100,100), 10, (0,0,255), -1)
cv.circle(img,(150,150), 10, (0,0,255), -1)
cv.circle(img,(200,200), 10, (0,0,255), -1)
cv.circle(img,(250,250), 10, (0,0,255), -1)
cv.circle(img,(300,300), 10, (0,0,255), -1)
cv.circle(img,(350,350), 10, (0,0,255), -1)
cv.circle(img,(400,400), 10, (0,0,255), -1)
cv.circle(img,(450,450), 10, (0,0,255), -1)
cv.circle(img,(500,500), 10, (0,0,255), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.ellipse(img,(256,256),(100,50),0,0,180,155,-1)

cv.imshow("Display window", img)
k = cv.waitKey(0)