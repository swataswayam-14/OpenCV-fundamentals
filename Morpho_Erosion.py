import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('balls.png', 1)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)
kernal = np.ones((5,5),np.uint8)
erosion = cv.erode(mask,kernal,iterations=1)
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
mg = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernal)
th = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernal)
titles = ['Image', 'Mask','erosion','opening','closing','mg','th']
images = [img, mask,erosion,opening,closing,mg,th]

for i in range(7):
    plt.subplot(4, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
#in opening first erosion is applied then dilation is applied
#in closing first dilation is applied then erosion is applied
#mg is difference between dilation and erosion of the image
#th is the difference between the input image and the opening image