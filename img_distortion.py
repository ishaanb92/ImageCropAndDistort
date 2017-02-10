#!/usr/bin/python2.7
import cv2
import numpy as np
import ConfigParser
import sys

# Read image
img = cv2.imread('lena.jpg')

# Parse the config file
parser = ConfigParser.ConfigParser()
parser.read('config.ini')

src_width,src_height,src_channels = img.shape

# Crop takes [y_min:y_max,x_min:x_max]

y_min = parser.getint('Bounding Box Size','y_min')
y_max = parser.getint('Bounding Box Size','y_max')

x_min = parser.getint('Bounding Box Size','x_min')
x_max = parser.getint('Bounding Box Size','x_max')

# Check bounding box limits
if x_max > src_width or y_max > src_height or x_min < 0 or y_min < 0 :
    print 'Invalid bounds on the crop'
    sys.exit()

crop_img = img[y_min:y_max,x_min:x_max]

# Get output type
output_type = parser.get('Output Type','type')

# Get output image dimensions
width = parser.getint('Target Image Size','width')
height = parser.getint('Target Image Size','height')

if output_type == 'crop':
    output = crop_img
elif output_type == 'padded':
    BLACK = [0,0,0]
    output = cv2.copyMakeBorder(crop_img,y_min,height-y_max,x_min,width-x_max,cv2.BORDER_CONSTANT,value=BLACK)
elif output_type == 'resize':
    output = cv2.resize(crop_img,(width,height), interpolation = cv2.INTER_CUBIC)
else:
    print "Type : %s is not recognized"%output_type
    sys.exit()

cv2.imwrite('output.jpg',output)





