import cv2
import numpy as np
import time
import sys
import os
from PIL import Image as im

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

path_name = "image.jpg"
image = cv2.imread(path_name)
file_name = os.path.basename(path_name)
filename, ext = file_name.split(".")

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
for i in range(len(boxes)):
    # extract the bounding box coordinates
    x, y = boxes[i][0], boxes[i][1]
    w, h = boxes[i][2], boxes[i][3]
    # draw a bounding box rectangle and label on the image
    color = [int(c) for c in colors[class_ids[i]]]

    rectangle=cv2.rectangle(image, (x, y), (x + w, y + h), color=color, thickness=thickness)
    #text = f"{labels[class_ids[i]]}: {confidences[i]:.2f}"
    print(type(rectangle))


    # Convert to Grayscale Image
    array = np.reshape(rectangle, (1024, 720))
    data = im.fromarray(array)
    img_rectangle=data.save('img_rectangle.png')
    gray_image = cv2.cvtColor(img_rectangle, cv2.COLOR_BGR2GRAY)


    # Canny Edge Detection
    canny_edge = cv2.Canny(gray_image, 170, 200)

    # Find contours based on Edges
    contours, new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

    # Initialize license Plate contour and x,y coordinates
    contour_with_license_plate = None
    license_plate = None
    x = None
    y = None
    w = None
    h = None

    # Find the contour with 4 potential corners and creat ROI around it
    for contour in contours:
        # Find Perimeter of contour and it should be a closed contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
        if len(approx) == 4:  # see whether it is a Rect
            contour_with_license_plate = approx
            x, y, w, h = cv2.boundingRect(contour)
            license_plate = gray_image[y:y + h, x:x + w]
            break

    # Removing Noise from the detected image
    license_plate = cv2.bilateralFilter(license_plate, 11, 17, 17)

    cv2.imshow('a', license_plate)
    cv2.waitKey(0)

cv2.imwrite(filename + "_yolo3." + ext, image)