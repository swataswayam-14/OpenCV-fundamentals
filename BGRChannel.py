'''
this programs prints the BGR channel on the screen
wherever in the image the user clicks Right Mouse Buttor'''
import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_RBUTTON:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strBGR = str(blue)+', '+str(green)+', '+str(red)
        cv2.putText(img,strBGR,(x,y),font,.5,(0,255,255),2)
        cv2.imshow('image',img)
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena_color.tiff')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
    