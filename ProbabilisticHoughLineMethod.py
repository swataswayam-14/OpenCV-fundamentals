import numpy as np
import cv2 as cv
img = cv.imread('road.png')
imgr = img.copy()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize=3)
cv.imshow('edges',edges)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength= 50,maxLineGap=3)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    
cv.imshow('image',img)
cv.imshow('Original_image',imgr)
cv.waitKey(0)
cv.destroyAllWindows()