'''
this program prompts the user
to enter a point on the image and
gives the colour of the point
as BGR channels in a second window
and fills the new image with the same BGR colour
'''

import numpy as np
import cv2
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        mycolorImage = np.zeros((512,512,3),np.uint8)
        mycolorImage[:]=[blue , green , red]
        cv2.imshow('color',mycolorImage)
img = cv2.imread('lena_color.tiff')
cv2.imshow('image',img)
points =[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()