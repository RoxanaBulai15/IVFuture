import numpy as np
import cv2 as cv


def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
# CE SUNT PARAMETRII DE LA cv.createTrackbar
# 1. 'R', 'G', 'B' - trackbar names
# 2. second one is the window name
# 3. the default value
# 4. the maximum value
# 5. the callback function which is executed every time trackbar value changes
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'  # In our application, we have created one switch in which application works only if switch is ON, otherwise screen is always black.

cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    # CE SUNT PARAMETRII DE LA cv.getTrackbarPos?
    #1. trackbarnam
    #2. Name of the window that is the parent of the trackbar.

    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()