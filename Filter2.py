import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# smoothing is the most common operation in image processing
# it is used to remove noise from the images
'''
various filters available in OpenCV are:
- homogeneous filter
- Gaussian filter
- Median filter
- Bilateral filter
HOMOGENEOUS FILTER: it is the most simple filter,
    each output pixel is the mean of its kernel neighbors
--> In image processing, a kernel, convolution matrix, or mask is a small
matrix. It is used for blurring, sharpening, embossing, edge detection
and more....
'''

img = cv.imread('Fig1038(a)(noisy_fingerprint).tif')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (6, 6))
gblur = cv.GaussianBlur(img, (5, 5), 0)
titles = ['image', '2D Convolution', 'blur', 'Gaussian Blur']
images = [img, dst, blur, gblur]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()