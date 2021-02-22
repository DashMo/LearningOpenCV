import numpy as np
import cv2

cap = cv2.VideoCapture(0) #input number accesses that number webcam

while True:
    ret, frame = cap.read() #ret tells if pic captured properly, frame holds np array with picture
    #cv2.imshow('Frame',frame)
    width = int(cap.get(3)) #int parameter is property identifier
    height = int(cap.get(4))
    image = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
    image = cv2.line(frame,(0,height),(width,0),(0,255,0),10)
    image = cv2.rectangle(image,(100,100),(500,150),(128,128,128),5) #thickness of -1 would fill rectangle
    image = cv2.circle(image,(width//2,height//2), 60, (0,0,255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image,'Learning OpenCV',(180,height-10),font,1,(255,255,255),3,cv2.LINE_AA)
    cv2.imshow('Frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'): #waits one millisecond for input 'q', if detected we will stop capturing frames
        break



    

cap.release() #releases camera
cv2.destroyAllWindows() #closes picture