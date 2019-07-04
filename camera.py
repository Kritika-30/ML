#!/usr/bin/python

import cv2

#starting camera
cap=cv2.VideoCapture(0)
#                   First camera

#to check  camera started or not
if cap.isOpened():
    print("camera is ready to take picture")
else:
    print('check your camera driver')

# now we can read input from camera
#print(cap.read())  # it will take first picture

status,img=cap.read()
status1,img1=cap.read()
# now showing

cv2.imshow('liveimg',img)
cv2.imshow('liveim2',img1)
cv2.waitKey(0)

# to close camera
cap.release()
