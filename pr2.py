import cv2 
img = cv2.imread('lena_color.tiff',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):#ord is a built in function that takes one argument-->press a key
    cv2.imwrite('lena_copy2.jpg',img)
    cv2.destroyAllWindows()