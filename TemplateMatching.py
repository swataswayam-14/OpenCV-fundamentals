'''
template matching is a method of searching and finding
the location of a template image inside a larger image
in open cv there is a method matchTemplate to achieve this purpose
'''
import cv2 as cv
import numpy as np

img = cv.imread('map.png')
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#grey_img = cv.resize(grey_img,(512,512))
template = cv.imread('template2.png',0)
#template = cv.resize(template,(230,230))
w,h = template.shape[::-1]

res = cv.matchTemplate(grey_img,template,cv.TM_CCOEFF_NORMED)
print(res)
threshold = 0.95
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img,pt,(pt[0] + w, pt[1] + h),(0,187,255),2)
    
cv.imshow('img',img)
cv.imshow('template',template)
cv.waitKey(0)
cv.destroyAllWindows()