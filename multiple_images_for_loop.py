import numpy as np
import cv2 as cv

img = cv.imread('lena_color.tiff')
layer = img.copy()
gp = [layer]
#using pyrdown method multiple times using for loops
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i),layer)

cv.imshow('original image',img)
cv.waitKey(0)
cv.destroyAllWindows()