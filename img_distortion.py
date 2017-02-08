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

# Add borders
width,height = img.shape[:2]

BLACK = [0,0,0]

padded_img = cv2.copyMakeBorder(crop_img,y1,height-y2,x1,width-x2,cv2.BORDER_CONSTANT,value=BLACK)

# Display images
cv2.imshow("Output",img)
cv2.imshow("Cropped",crop_img)
cv2.imshow("Padded",padded_img)
#cv2.waitKey(0)

# Save the images
cv2.imwrite("cropped.jpg",crop_img)
cv2.imwrite("padded.jpg",padded_img)
