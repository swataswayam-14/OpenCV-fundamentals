'''
this program merge two images
using cv2.add method'''
import numpy as np
import cv2
img = cv2.imread('lena_color.tiff')
cv2.imshow('one',img)
cv2.waitKey(2000)
img2 = cv2.imread('heart.png')
cv2.imshow('two',img2)
cv2.waitKey(2000)
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
dst = cv2.add(img,img2);
#there is another method to add for ex: 90%of 1st image and 30% of 2nd image weightage
dst2 = cv2.addWeighted(img,.5,img2,.5,0);
dst3 = cv2.addWeighted(img,.6,img2,.4,0);
dst4 = cv2.addWeighted(img,.7,img2,.3,0);
dst5 = cv2.addWeighted(img,.9,img2,.1,0);
cv2.imshow('image',dst)
cv2.waitKey(2000)
cv2.imshow('image2',dst2)
cv2.waitKey(2000)
cv2.imshow('image3',dst3)
cv2.waitKey(2000)
cv2.imshow('image4',dst4)
cv2.waitKey(2000)
cv2.imshow('image5',dst5)
cv2.waitKey(2000)
cv2.destroyAllWindows()
