'''
hough transform is a popular technique to detect 
any shape, if you can represent that shape in a 
mathematical form. It can detect that shape even if 
it is broken or distorted a little bit.

HOUGH TRANSFORMATION ALGORITHM:-->
1.Edge detection, e.g. using the canny edge detector.
2.Mapping of edge points to the Hough space and storage
in an accumulator.
3.Interpretation of the accumulator to yield lines of
infinite length. The interpretation is done by thresholding
and possibly other constraints.
4.Conversion of infinite lines to finite lines.
'''
#OpenCV implements two kind of hough line transforms:
'''
-The standard Hough Transform (hough lines method)
-The probabilistic Hough line Transform (Hough Lines P Method)
'''
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150,apertureSize=3)
cv.imshow('canny_edge_image',edges)
lines = cv.HoughLines(edges , 1, np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a*rho
    y0 = b*rho
    
    x1= int(x0 + 1000 *(-b))
    y1 = int(y0 +1000 *(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0-1000*(a))
    
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
#this method gives lines of infinite length 
#starting from one end of the image to the other end of the image
#To fix this problem we have to use Probabilistic Hough Line tranform(HoughLinePmethod)