#!/usr/bin/python2.7
import cv2
import numpy as np

# Read image
img = cv2.imread('lena.jpg')

# Crop takes [y1:y2,x1:x2]

y1 = 200
y2 = 300

x1 = 100
x2 = 300

crop_img = img[y1:y2,x1:x2]


# Display images
cv2.imshow("Output",img)
cv2.imshow("Cropped",crop_img)
cv2.waitKey(0)
