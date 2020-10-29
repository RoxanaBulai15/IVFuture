import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv.ellipse(img,(256,256),(100,50),0,0,180,155,-1)
# !!! Ce sunt parametrii de la cv.ellipse(...) ???
#(256,256) este centrul elipsei
#(100,50) este lungimea axelor
#0 startAngle ptr arcul elipsei
#0 endAngle ptr arcul elipsei

cv.imshow("Display window", img)
k = cv.waitKey(0)