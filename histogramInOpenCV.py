'''
histogram as a graph or a plot which gives
a overall idea about the intensity distribution 
of the image.
'''
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = np.zeros((200,200),np.uint8)
cv.imshow('img',img)
#finding histogram of this image using matplotlib plt.hist
plt.hist(img.ravel(),256,[0,256])
plt.show()
'''
in the y axis we will see the total number of pixels
here it is 200*200=40000 and in the x axis we will see 
the intensity of each pixel.
this graph shows how many number of pixels inside an image
which have pixel value ranging from 0 to 256

in our example all the 40000 pixels value have the pixel value 0 (black)

histogram is a graph which give you an overall idea of the intensity
ditribution of an image
'''




cv.waitKey(0)
cv.destroyAllWindows()