#STEP 1: Perform face detection
#STEP 2: Extract face ROI
#STEP 3: Stored blurred face in original image
#STEP 4: Blur/Anonymize face

#STEP 1&2&3: Face detection & exctract face ROI
import cv2
import cv2 as cv
from matplotlib import pyplot as plt

face_cascade=cv.CascadeClassifier('D:\IVFuture\opencv\data\haarcascades\haarcascade_frontalface_alt.xml')
img = cv2.imread('trump.jpg')
#frame_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#frame_gray = cv.equalizeHist(frame_gray)
faces = face_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=6) #!!
for face in faces:
    x, y, w, h = face
    #!!! plt
    #plt.subplot(121), plt.imshow(img), plt.title('Original')
    #plt.xticks([]), plt.yticks([])
    img[y:y+h,x:x+w]=cv2.GaussianBlur(img[y:y+h,x:x+w],(15,15),cv2.BORDER_DEFAULT)

    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #center = (x + w // 2, y + h // 2)
    #img = cv.ellipse(img, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
    #faceROI = frame_gray[y:y + h, x:x + w]
    #blur = cv.GaussianBlur(faceROI, (5, 5), 0)

    #!!! plt
    #plt.subplot(122), plt.imshow(img), plt.title('Blurred')
    #plt.xticks([]), plt.yticks([])
    #plt.show()
cv2.imshow('img', img)
cv2.waitKey(0)

#STEP 4: BLUR
