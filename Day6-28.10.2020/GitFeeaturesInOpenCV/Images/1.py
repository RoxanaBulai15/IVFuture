import cv2 as cv
import sys

#citeste imaginea din cv.samples
img1 = cv.imread(cv.samples.findFile("starry_night.jpg"))
img2 = cv.imread(cv.samples.findFile("starry_night.jpg"), flags="IMREAD_COLOR") #loads the image in the BGR 8-bit format
img3 = cv.imread(cv.samples.findFile("starry_night.jpg"), flags="IMREAD_UNCHANGED") #loads the image as is
img4 = cv.imread(cv.samples.findFile("starry_night.jpg"), flags="IMREAD_GRAYSCALE") #loads the image as an intensity one
#daca imaginea1 nu exista
if img1 is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img1)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img1)

