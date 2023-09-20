import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lena_color.tiff',0)
hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()