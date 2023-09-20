import cv2
import datetime
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret , frame=cap.read()
    if ret==True:
        font = cv2.FONT_HERSHEY_SIMPLEX
       
        datet = str(datetime.datetime.now())
        text = 'Width: '+str(cap.get(3))+' height: '+str(cap.get(4)) +' '+ datet
        frame = cv2.putText(frame,text,(10,50),font,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()      