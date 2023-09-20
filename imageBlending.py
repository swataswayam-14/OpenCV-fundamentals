import cv2 as cv
import numpy as np

apple = cv.imread('apple.png')
orange = cv.imread('orange.png')
print(apple.shape)
print(orange.shape)

apple = cv.resize(apple,(512,512))
orange = cv.resize(orange, (512,512))
print(apple.shape)
print(orange.shape)
'''
creating half of both apple and orange images
and blending them directly
'''
apple_orange = np.hstack((apple[:, :256],orange[:, 256:]))
# but after doing this the line is clearly visible
# in image blending the orange and apple image should be blended or merged
#there must not be any distinction b/w the images. 
'''
TO BLEND TWO IMAGES USING IMAGE PYRAMIDS TECHNIQUES:
1.load the two images of apple and orange
2. find the gaussian pyramids for apple and orange
3. from gaussian pyramids, find their laplacian pyramids.
4.now join the left half of apple and right half of orange in 
    each levels of laplacian pyramids.
5.finally from this joint image pyramids, reconstruct the original image
'''
# generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
    
# generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)
    
# generate laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)
    
#now add left and right halves of images in each level
apple_orange_pyramid = []
n=0
for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
# now reconstruction
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i],apple_orange_reconstruct)
    

cv.imshow('apple',apple)
cv.waitKey(2500)
cv.imshow('orange',orange)
cv.waitKey(2500)
cv.imshow('apple_orange',apple_orange)
cv.waitKey(2500)
cv.imshow('apple_orange_reconstruct',apple_orange_reconstruct)
cv.waitKey(2500)

cv.destroyAllWindows()