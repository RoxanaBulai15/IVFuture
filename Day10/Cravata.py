import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('trump.jpg', cv.IMREAD_UNCHANGED)
template = cv.imread('tie.jpg', cv.IMREAD_UNCHANGED)

result=cv.matchTemplate(img,template,cv.TM_CCOEFF_NORMED)

#1. Detectarea cravatei
#get the best match position
min_val, max_val, min_loc, max_loc=cv.minMaxLoc(result)
top_left=max_loc
tie_w=template.shape[1]
tie_h=template.shape[0]
bottom_right=(top_left[0]+tie_w,top_left[1]+tie_h)

cv.rectangle(img,top_left, bottom_right, color=(0,255, 0), thickness=2, lineType=cv.LINE_4)
screen = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv.imshow('asd',screen)
#2. Schimbarea culorii




hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower_range = np.array([0,100,100])
upper_range = np.array([5,255,255])

mask = cv.inRange(hsv, lower_range, upper_range)
res = cv.bitwise_and(img,img, mask= mask)
#cv.imshow('frame',img)
cv.imshow('mask',mask)
cv.imshow('res',res)



cv.waitKey(0)