import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# !!! Ce sunt parametrii de la cv.circle(...) ???
#(0,0,255) este culoarea(roz)
#63 este raza cercului
#(447,63) este centrul cercului
#ultimul numar este grosimea liniei
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.circle(img,(50,50), 10, (0,0,255), -1)
cv.imshow("Display window", img)
k = cv.waitKey(0)