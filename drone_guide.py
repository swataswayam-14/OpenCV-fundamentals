import cv2 as cv
import numpy as np
import time

map_img = cv.imread('paplu.jpg')
grey_map = cv.cvtColor(map_img, cv.COLOR_BGR2GRAY)
template = cv.imread('template_paplu.jpg', 0)
w, h = template.shape[::-1]

cap = cv.VideoCapture(0)  # Use 0 if the drone camera is connected to the computer

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame from camera")
        break

    grey_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    res = cv.matchTemplate(grey_frame, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.2)

    if len(loc[0]) > 0:
        pt = (loc[1][0], loc[0][0])  # First match
        cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        # Calculate drone's position on the map
        map_pt_x = int(pt[0] * map_img.shape[1] / frame.shape[1])
        map_pt_y = int(pt[1] * map_img.shape[0] / frame.shape[0])
        drone_pos = (map_pt_x, map_pt_y)
        print("Drone position:", drone_pos)

    cv.imshow('frame', frame)
    # cv.imshow('template',template)
    # cv.imshow('original',map_img)
    key = cv.waitKey(1)  # Wait for 5 seconds before capturing the next frame
    if key == 27:  
        break

cap.release()
cv.destroyAllWindows()