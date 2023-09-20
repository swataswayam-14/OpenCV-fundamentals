'''
this program gives the coordinate at any point 
on the image when the user clicks on the image
by the mouse's left click button'''
import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x,' ,',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+', '+str(y)
        cv2.putText(img, strXY,(x,y),font,.5,(255,255,0),2)#(x,y)is the location where we want to print the text
        cv2.imshow('image',img)
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('peppers_color.tif')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows