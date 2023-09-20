import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#smoothing is the most common operation in image processing
#it is used to remove noise from the images
'''
various fliters available in open cv are:
-homogeneous filter
-gaussian filter
-Median filter
-Bilateral filter
HOMOGENEOUS FILTER: it is the most simple filter ,
    each output pixel is the mean of its kernel neighbors
-->In image processing , a kernel, convolution matrix , or mask is a small
matrix. It is used for blurring, sharpening , embossing , edge detection
and more....
'''
img = cv.imread('Fig1001(e)(edge_noisy_image).tif')
img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)# bilateral filter is used in images where we want to preserve the borders
#bilateral filter is highly effective in noise removing while keeping the edge sharp
blur = cv.blur(img,(6,6))
gblur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5)
bilateralFilter = cv.bilateralFilter(img,9,75,75)

titles= ['image','2D Convolution','blur','Gaussian Blur','median Blur','Bilateral Filter']
images = [img,dst,blur,gblur,median,bilateralFilter]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()    
#in the output we see that the corner borders are smoothened or the image is blurred
'''
as in one-dimensional signals, images also can be filteres with
various low-pass filters(LPF), high-pass filters(HPF) etc.
-->LPF helps in removing noises, blurring the images.
-->HPF helps in finding edges in the images.

Gaussian filter is a different-weight-kernel, in both x and y direction
Median filter is something that replaces each pixel's value with the 
median of its neighboring pixels. This method is great when dealing with 
"salt and pepper noise".
'''