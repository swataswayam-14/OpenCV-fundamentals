#morphological operations:
'''
morphological transformations are some simple 
operations based on the image shape
- normally performed on binary images.
A kernel tells you how to change the value of any
given pixel by combining it with different amounts 
of the neighbouring pixels
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('balls.png', 1)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)
#here a black dot is present in the mask
#to remove it: the below line of code--->
'''
the bigger the rectangle is the better the result would be
'''
kernal = np.ones((3,3),np.uint8)#kernel here is a 2/2 sqaure shape
#this kernel would be applied to our image wherever these black dots are there
#the size of the black dot get reduced
#but still we can see the black dots
#to remove it completely a third parameter is passed to the dilate method that  is i->the no. of iteration
dilation = cv.dilate(mask,kernal,iterations=5)
'''
but there is a problem
the size of the white area is increased and its merging
'''
titles = ['Image', 'Mask','dilation']
images = [img, mask,dilation]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()