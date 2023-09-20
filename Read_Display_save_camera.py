import cv2
cap = cv2.VideoCapture(0);
#while loop  to cpature the frame continuously
while(True):
    ret , frame = cap.read()
    #if you want converting coloured footage to grayscale footage
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
# to display footage from a  video file the syntax is 
#cap = cv2.VideoCapture('name.mp4') name.extension
#then write:--
#while(cap.isOpened()):#if the video file name is correct then isOpened function will return true else false
#cap = cv2.VideoCapture(8);
#print(cap.isOpened())# output is false