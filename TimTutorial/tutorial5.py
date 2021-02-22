import numpy as np
import cv2

cap = cv2.VideoCapture(0) #input number accesses that number webcam

while True:
    ret, frame = cap.read() #ret tells if pic captured properly, frame holds np array with picture
    #cv2.imshow('Frame',frame)
    width = int(cap.get(3)) #int parameter is property identifier
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converts from BGR to HSV 
    lower_blue = np.array([90,50,50])
    # BGR_color = [[[255,0,0]]]    #THIS is how to manually convert from BGR to HSV
    # blue = cv2.cvtColor(BGR_color,cv2.COLOR_BGR2HSV)
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue) #will mask image to keep only pixels within this color range
    image = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('mask',mask)
    cv2.imshow('Frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'): #waits one millisecond for input 'q', if detected we will stop capturing frames
        break



    

cap.release() #releases camera
cv2.destroyAllWindows() #closes picture