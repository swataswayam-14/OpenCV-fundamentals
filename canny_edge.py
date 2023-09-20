'''
the canny edge detector is an edge detection operator 
that uses a multi-stage algorithm to detect a wide range
of edges in images. It was developed by John F. Canny in 1986.

THE CANNY EDGE DETECTION ALGORITHM IS COMPOSED OF 5 STEPS:
1.noise reduction
2.gradient calculation
3.non-maximum suppression
4.double threshold
5.edge tracking by hysteresis
'''
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('lena_color.tiff',0)
canny = cv.Canny(img,100,200)
titles = ['image','canny']
images = [img,canny]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
#canny edge detection is better as it provides less noise and better edge detection
    
