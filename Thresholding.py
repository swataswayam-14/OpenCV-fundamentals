'''
thresh-holding is a popular segmentation 
technique used for separating an object from its background
The process of thresh-holding involves comparing each pixel of an image
with a predefined threshold values.
This type of comparision of each pixel of an image
to a threshold value divides all the pixels of the input image into two groups
first group involves pixels having intensity values lower than the threshold values
second group involves pixels having intensity values greater than the threshold value.
'''
import numpy as np
import cv2 as cv
img = cv.imread('gradient.jpg',0)
_,thl = cv.threshold(img,127,255,cv.THRESH_BINARY)# it is binary thresholding and as the name suggest it is either 0 or 1
_,thl2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,thl3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,thl4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,thl5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
img = cv.resize(img,(512,512))
thl = cv.resize(thl,(512,512))
thl2 = cv.resize(thl2,(512,512))
thl3 = cv.resize(thl3,(512,512))
thl4 = cv.resize(thl4,(512,512))
thl5 = cv.resize(thl5,(512,512))
cv.imshow('image',img)
cv.imshow('threshold',thl)
cv.imshow('threshold_inv',thl2)
cv.imshow('threshold_trunc',thl3)
cv.imshow('threshold_to_zero',thl4)#pixel values below 127 will be 0 and above it will remain the same
cv.imshow('threshold_to_zero_inv',thl5)#just the inverse of ThresToZero.
cv.waitKey(0)
cv.destroyAllWindows()
'''
in this binary thresholding we are comparing each and every
pixel of the original image with 127 and if the value of the 
pixel is less than 127 , the value is assigned to 0 that is black and if 
the value of the pixel is greater than 127 the pixel value is 
assigned 1 that is white. The inverse simply inverses everything
'''

