'''
An image gradient is a directional change 
in the intensity or color in an image.
it can be used to find edges in the image.
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('sudoku.png',cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img,cv.CV_64F,ksize=1)#kernel size must be odd
lap = np.uint8(np.absolute(lap))# this method detects all the edges
sobelX = cv.Sobel(img,cv.CV_64F,1,0)
SobelY = cv.Sobel(img,cv.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))#change in direction of intensity is in x direction
SobelY = np.uint8(np.absolute(SobelY))#change in direction of intensity is in y direction

#combining these results:
sobelCombined = cv.bitwise_or(sobelX,SobelY)

titles = ['image','laplacian','SobelX','SobelY','sobelCombined']
images = [img,lap,sobelX,SobelY,sobelCombined]
for i in range(5):
    plt.subplot(2,3,i+1)
    
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
    