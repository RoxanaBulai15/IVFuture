#It gives us the coordinates (x,y) for every mouse event.
# #With this event and location, we can do whatever we like.
# To list all available events available, run the following code in Python terminal:
#import cv2 as cv
#events = [i for i in dir(cv) if 'EVENT' in i]
#print( events )
import numpy as np
import cv2 as cv


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        #
        cv.circle(img, (x, y), 60, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8) #np.zeros seteaza imaginea sa fie neagra
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()