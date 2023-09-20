import cv2
#DIP3E_CH03_Original_Images
img=cv2.imread('lena_color.tiff',0)#0 for grayscale , 1 for coloured, -1 for unchanged
'''
if we give wrong file name
in the imread function we get 
a none...
so first check like if it is none
then you will get to know that you have 
given some wrong file name'''
print(img)
cv2.imshow('image',img) 
#the image is showned for milliseconds.
#to show it properly we will add--
cv2.waitKey(5000) #it takes the milliseconds for which it will show the image
cv2.destroyAllWindows()#destroys or terminates the window that we have created
'''if we give the command cv2.waitKey(0)
then our window will not close until we close it'''
# function to write a image to a file:-
cv2.imwrite('lena_colour.jpg',img)