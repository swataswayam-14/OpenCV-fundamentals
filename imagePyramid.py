'''
pyramid or pyramid representation is a type of 
multi-scale signal representation in which a signal or an
image is subject to repeated smoothing and subsampling

TWO TYPES OF IMAGE PYRAMIDS:
-->Gaussian pyramid
-->Laplacian pyramid
'''
import cv2 as cv
import numpy as np

img = cv.imread('lena_color.tiff')
lr1 = cv.pyrDown(img)# lr1 is 1/4th of the original image
lr2 = cv.pyrDown(lr1)# lr2 is 1/16th of the original image
hr2 = cv.pyrUp(lr2)

cv.imshow('original image',img)
cv.imshow('pyrdown image',lr1)
cv.imshow('2nd pyrdown',lr2)
cv.imshow('pyrUp of 2nd image',hr2)
 
cv.waitKey(0)
cv.destroyAllWindows()