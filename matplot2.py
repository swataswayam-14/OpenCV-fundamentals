from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('gradient.jpg',0)
_,thl = cv.threshold(img,127,255,cv.THRESH_BINARY)# it is binary thresholding and as the name suggest it is either 0 or 1
_,thl2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,thl3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,thl4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,thl5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
img = cv.resize(img,(512,512))
thl = cv.resize(thl,(512,512))
thl2 = cv.resize(thl2,(512,512))
thl3 = cv.resize(thl3,(512,512))
thl4 = cv.resize(thl4,(512,512))
thl5 = cv.resize(thl5,(512,512))
'''
by using matplotlib we can show all these 5 thresholding images
that we have created in a single window.
whereas in open cv we used 5 different window to show these images.
'''
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thl,thl2,thl3,thl4,thl5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    #if we don't want to show the ticks then we can use
    plt.xticks([]),plt.yticks([])
plt.show()