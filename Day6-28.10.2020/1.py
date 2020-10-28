import cv2 as cv
import sys


img = cv.imread(cv.samples.findFile("D:\IVFuture\opencv\doc\images\opticalfb.jpg"))
img1 = cv.imread(r"C:\Users\ROXANA\Desktop\1200px-An_up-close_picture_of_a_curious_male_domestic_shorthair_tabby_cat.jpg")


#daca imaginea1 nu exista
if img1 is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img1)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("D:\IVFuture\opencv\doc\images\opticalfb.jpg", img2)

