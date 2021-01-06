import PIL
import cv2
import numpy as np
import pytesseract
from pytesseract import image_to_string

# Read image
img = cv2.imread("image.jpg", 1)
gray = cv2.cvtColor(img, 0)
cv2.imshow('img', gray)
cv2.waitKey(0)

#read haarcascade
#plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml') #does not give me error, but result is not correct
#plates_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')
plates_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
plates = plates_cascade.detectMultiScale(gray, 1.2, 4)


for (x,y,w,h) in plates:
    #detect plate with rectangle
    #rec. start point (x,y), rec. end point (x+w, y+h), blue color(255,0,0), line width 1

    plates_rec = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
    #Text= pytesseract.image_to_string(plates_rec)
    print(type(plates_rec))

    #pytesseract.tesseract_cmd = 'C:\Users\ROXANA\Desktop\IVFuture\venv\Lib\site-packages'

    output = pytesseract.image_to_string(PIL.Image.open('Output Image.PNG').convert("RGB"), lang='eng')
    cv2.putText(plates_rec, output, (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    gray_plates = gray[y:y+h, x:x+w]
    color_plates = img[y:y+h, x:x+w]

    #cv2.imshow('img', gray_plates)
    #cv2.waitKey(0)

    height, width, chanel = gray_plates.shape
    print(height, width)


cv2.imshow('img', img)
cv2.waitKey(0)
print('Number of detected licence plates:', len(plates))