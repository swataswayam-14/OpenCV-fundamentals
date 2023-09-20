import numpy as np
import cv2

# Load image
img = cv2.imread('lena_color.tiff',1)
#creating an image using numpy zeroes method
#img = np.zeros([512,512,3], np.uint8)#-->this method gives a black image of height 512 and width 512
#drawing a line --> the function take two arguments--> the starting point and the ending point
img = cv2.line(img,(0,0),(255,255),(147,96,44),10)# to draw a line
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10)
img = cv2.rectangle(img,(384,0),(510,128),(255,0,0),-1)#if in place of thickness you give -1 then the rectangle would be filled with the color given
img = cv2.circle(img,(47,56),63,(0,255,0),-1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'hello !',(10,50),font,2,(255,255,255),5,cv2.LINE_AA)
# Check if image was loaded correctly
if img is None:
    print("Error: Could not read image file")
else:
    # Display image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()