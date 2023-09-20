import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('lena_color.tiff',1)
#img = np.zeros((200,200),np.uint8)
#cv.rectangle(img,(0,100),(200,200),(255),-1)
#20k pixels have the pixel value 0 and 20k pixels have the pixel value 1(white)
#cv.rectangle(img,(0,50),(100,100),(127),-1)
b, g, r = cv.split(img)

cv.imshow('img',img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

#plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()