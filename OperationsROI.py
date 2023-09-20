# ROI stands for Region Of Interest
# sometimes we need to work on some specific region of the image
# for ex: copy a specific part of the image and paste it elsewhere

import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)

img = cv2.imread('peppers_color.tif')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

x11 = int(input("enter x11: "))
y11 = int(input("enter y11: "))
x12 = int(input("enter x12: "))
y12 = int(input("enter y12: "))
ball = img[y11:y12, x11:x12]

x21 = int(input("enter x21: "))
y21 = int(input("enter y21: "))
x22 = int(input("enter x22: "))
y22 = int(input("enter y22: "))

img[y21:y22, x21:x22] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()