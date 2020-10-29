import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# !!! Ce sunt parametrii de la cv.rectangle(...) ???
#(0,255,0) este culoarea(verde)
#(384,0) este coltul din stanga sus
#(510,128) este coltul din dreapta jos
#ultimul numar este grosimea liniei
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.rectangle(img,(0,0),(50,50),(0,255,0),3)
cv.imshow("Display window", img)
k = cv.waitKey(0)