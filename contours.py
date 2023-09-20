'''
curve joining all the continuous points on the boundary
which have the same color intensity is a contour
very useful in shape anaylysis , object detection or object recognition
'''
#for better accuracy we generally use binary images to find the contour
'''
contours is a python list of all the contours in the image.
Each individual contour is a Numpy array of (x,y) coordinates
of boundary points of the object.
'''
import cv2 as cv
import numpy as np

img = cv.imread('mandril_color.tif')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray,127,255,0)
contours , hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print("number of contours = "+str(len(contours)))
print(contours[1])

cv.drawContours(img,contours,-1,(0,255,0),3)#-1  to drwa all the contours
# it can give 1 to 5323 as the total contours present is 5323

cv.imshow('image',img)
cv.imshow('gray image',imgray)
cv.waitKey(0)
cv.destroyAllWindows()
