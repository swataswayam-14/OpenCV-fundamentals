import cv2 as cv
import numpy as np
'''
adoptive thresholding calculates threshold for a 
smaller region of images. So we get different thresholding values
for the same image.
hence it gives us better results for images with varying illumination
'''
img = cv.imread('sudoku.png',0)
_,thl1 = cv.threshold(img,125,255,cv.THRESH_BINARY)
thl2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
thl3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
'''
here we don't see the clear image after thresholding
here we can only see that part of the image which is well
illuminated and the other parts are turned black in global thresholding
hence in this case it is better to use adaptive thresholding
'''
cv.imshow('image',img)
cv.imshow('binary',thl1)
cv.imshow('adaptive_mean_binary',thl2)
cv.imshow('adaptive_gaussian_binary',thl3)
cv.waitKey(0)
cv.destroyAllWindows()
