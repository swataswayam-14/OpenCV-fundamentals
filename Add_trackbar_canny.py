import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def nothing(x):
    pass


while True:
    v=cv.namedWindow('tracking')
    cv.createTrackbar('index1', 'tracking', 0, 255, nothing)
    cv.createTrackbar('index2', 'tracking', 0, 255, nothing)

    img = cv.imread('lena_color.tiff', cv.IMREAD_GRAYSCALE)
    index1 = cv.getTrackbarPos('index1', 'tracking')
    index2 = cv.getTrackbarPos('index2', 'tracking')
    canny = cv.Canny(img, index1, index2)
    titles = ['image', 'canny','trackin']
    images = [img, canny,v]


    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

    plt.show()

cv.destroyAllWindows()
    
