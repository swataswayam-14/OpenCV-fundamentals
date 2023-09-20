'''
this programs promts the user to click the left
button of the mouse. if the user clicks on the 
right button 2 or more times on the image then 
it will draw a line joining the two points given by the user'''
import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
        cv2.imshow('image',img)
        
img = cv2.imread('lena_color.tiff')
cv2.imshow('image',img)
points = [] 
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()