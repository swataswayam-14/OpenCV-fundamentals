'''
laplacian pyramids are created from gaussian pyramids
there is no specific function to create laplacian pyramids

A level in Laplacian Pyramid is formed by the difference 
between that level in Gaussian Pyramid and expanded version 
of its upper level in Gaussian Pyramid.

laplacian and gaussian pyramids help us to blend and recontruct the images
'''

import numpy as np
import cv2 as cv

img = cv.imread('lena_color.tiff')
layer = img.copy()
#creating gaussian pyramid
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)

layer = gp[5]
cv.imshow('upper level gaussian pyramid',layer)

#creating laplacian pyramid:
lp = [layer]
for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1],gaussian_extended)
    cv.imshow(str(i),laplacian)

cv.imshow('original image', img)
cv.waitKey(0)
cv.destroyAllWindows()
     
