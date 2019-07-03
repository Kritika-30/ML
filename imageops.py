#!/usr/bin/python

import cv2
import sys

# version
print(cv2.__version__)

# image name as first arg given by user

data = sys.argv[1]


# image read
img=cv2.imread(data,1)   # loading image in a colored format --original image 

print(img)

#shape
print(img.shape)

#height width color channel
# to show image
cv2.imshow('windowname1',img)
cv2.imshow('windowname2',img-50)

# saving image
cv2.imwrite('newimage.jpg',img)


cv2.waitKey(0)  #holding image for infinite time
