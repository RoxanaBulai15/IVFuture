import time

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
cv2.imwrite(filename + "_1111." + ext, mask)
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


CONFIDENCE = 0.5
SCORE_THRESHOLD = 0.5
IOU_THRESHOLD = 0.5

# the neural network configuration
config_path = "yolov3.cfg"
# the YOLO net weights file
weights_path = "D:\IVFuture\yolov3.weights"

# loading all the class labels (objects)
labels = open("coco.names").read().strip().split("\n")
# generating colors for each object for later plotting
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

#config_path = open("yolov3.cfg").read().strip().split("\n")
#weights_path = open("D:\IVFuture\yolov3.weights").read().strip().split("\n")

# load the YOLO network
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

path_name = "car.jpg"
image = cv2.imread(path_name)


h, w = image.shape[:2]
# create 4D blob
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

print("image.shape:", image.shape)
print("blob.shape:", blob.shape)

# sets the blob as the input of the network
net.setInput(blob)
# get all the layer names
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# feed forward (inference) and get the network output
# measure how much it took in seconds
start = time.perf_counter()
layer_outputs = net.forward(ln)
time_took = time.perf_counter() - start
print(f"Time took: {time_took:.2f}s")

font_scale = 1
thickness = 1
boxes, confidences, class_ids = [], [], []
# loop over each of the layer outputs
for output in layer_outputs:
    # loop over each of the object detections
    for detection in output:
        # extract the class id (label) and confidence (as a probability) of
        # the current object detection
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        # discard out weak predictions by ensuring the detected
        # probability is greater than the minimum probability
        if confidence > CONFIDENCE:
            # scale the bounding box coordinates back relative to the
            # size of the image, keeping in mind that YOLO actually
            # returns the center (x, y)-coordinates of the bounding
            # box followed by the boxes' width and height
            box = detection[:4] * np.array([w, h, w, h])
            (centerX, centerY, width, height) = box.astype("int")
            # use the center (x, y)-coordinates to derive the top and
            # and left corner of the bounding box
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            # update our list of bounding box coordinates, confidences,
            # and class IDs
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            class_ids.append(class_id)

print(detection.shape)

# loop over the indexes we are keeping
n=len(boxes)-1
    # extract the bounding box coordinates
x, y = boxes[n][0], boxes[n][1]
w, h = boxes[n][2], boxes[n][3]
# draw a bounding box rectangle and label on the image
color = [int(c) for c in colors[class_ids[n]]]

rectangle=cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)
#text = f"{labels[class_ids[i]]}: {confidences[i]:.2f}"

    # calculate text width & height to draw the transparent boxes as background of the text
    #(text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)[0]
text_offset_x = x
text_offset_y = y - 5

    #box_coords = ((text_offset_x, text_offset_y+h/2-text_height), (text_offset_x + text_width, text_offset_y + text_height))
    #overlay = image.copy()
    #cv2.rectangle(overlay, box_coords[0], box_coords[1], color=color, thickness=thickness)
    # add opacity (transparency to the box)
    #image = cv2.addWeighted(overlay, 0.6, image, 0.4, 0)
    # now put the text (label: confidence %)

cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    #cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
       # fontScale=font_scale, color=(0, 0, 0), thickness=thickness)

cv2.imwrite(filename + "_yolo3." + ext, image)
cv2.waitKey(0)