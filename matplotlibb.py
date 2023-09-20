from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread('lena_color.tiff')
cv.imshow('lena',img)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)# this code converts the BGR form of image to RGB 
#as matplotlib reads the image in the RGB format
#now both the image looks the same

plt.imshow(img)
#plt.xticks([]),plt.yticks([])#this line of code hides the x and y coordinates or ticks in the image
plt.show()
'''
open cv reads the image in the BGR format
whereas matplotlib reads the image in the RBG format 
'''
