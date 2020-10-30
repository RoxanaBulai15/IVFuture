import cv2 as cv
img = cv.imread('D:\IVFuture\opencv\doc\images\camshift_result.jpg')

#It returns a tuple of the number of rows, columns, and channels (if the image is color):
print(img.shape)

print( img.size )

#img.dtype is very important while debugging because a large number of errors in OpenCV-Python code are caused by invalid datatype.
print(img.dtype)