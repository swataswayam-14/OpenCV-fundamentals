'''
this program masks all the color and shows only the desired color portion on the image as we want
we just need to pass the lower boundation and upper boundation variable(l_b and u_b) for the color that we want to mask
'''
import numpy as np
import cv2 as cv
def nothing(x):
    pass
while True:
    frame = cv.imread('mandril_color.tif')
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_b= np.array([0,50,50])
    u_b = np.array([10,255,255])
    mask = cv.inRange(hsv,l_b,u_b)
    res = cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()
    