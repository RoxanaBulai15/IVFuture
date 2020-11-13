import cv2
import imutils
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread('car.jpg')
path_name='car.jpg'
file_name = np.os.path.basename(path_name)
filename, ext = file_name.split(".")
cv2.imwrite(filename + "_1." + ext, img)

img = cv2.resize(img, (620,480) )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 13, 15, 15)
cv2.imshow('a',gray)
cv2.imwrite(filename + "_2." + ext, gray)

edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
cv2.imshow('img',edged)
cv2.imwrite(filename + "_3." + ext, edged)

contours=cv2.findContours(edged.copy(),cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
#Now we can start looking for contours on our image
contours = imutils.grab_contours(contours)
contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break

# Masking the part other than the number plate
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt], 0, 255, -1,)
new_image = cv2.bitwise_and(img,img,mask=mask)
cv2.imwrite(filename + "_4." + ext, new_image)

#Character Segmentation
# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]

cv2.imwrite(filename + "_5." + ext, Cropped)
cv2.imshow('c',Cropped)
#Character Recognition
#Read the number plate

text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("Detected license plate Number is:", text)


cv2.imshow('b',new_image)
cv2.waitKey(0)