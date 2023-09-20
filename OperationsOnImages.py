'''
this program deals with some basic 
arithematic operations on images
'''
import numpy as np
import cv2

img = cv2.imread('lena_color.tiff')
print(img.shape)#returns a tuple of number of rows, columns , and channels
print(img.size)#returns total number of pixels that is accessed
print(img.dtype)#returns Image datatype 
print(img.itemsize)
print(img.ndim)
b,g,r= cv2.split(img)
img = cv2.merge((b,g,r))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 