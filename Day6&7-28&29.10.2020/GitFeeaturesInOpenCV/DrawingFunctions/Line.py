import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# !!! Ce sunt parametrii de la cv.line(...) ???
#(255,0,0) este culoarea(albastru)
#(0,0) este punctul de unde incepe linia
#(511,511) este punctul unde se termina linia
#ultimul numar este grosimea liniei
cv.line(img, (0,0), (511,511), (255,0,0), 5)
cv.line(img, (0,0), (0,511), (255,0,0), 5) #latura verticala din stanga
cv.line(img, (0,0), (511,0), (255,0,0), 5) #latura orizontala de sus
cv.line(img, (0,511), (511,511), (255,0,0), 5) #latura orizontala de jos
cv.line(img, (511,0), (511,511), (255,0,0), 5) #latura verticala din dreapta
cv.line(img, (0,511), (511,0), (255,0,0), 10) #cealalta diagonala
cv.imshow("Display window", img)
k = cv.waitKey(0)