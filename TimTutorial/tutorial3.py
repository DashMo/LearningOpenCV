import numpy as np
import cv2

cap = cv2.VideoCapture(0) #input number accesses that number webcam

while True:
    ret, frame = cap.read() #ret tells if pic captured properly, frame holds np array with picture
    #cv2.imshow('Frame',frame)
    width = int(cap.get(3)) #int parameter is property identifier
    height = int(cap.get(4))
    image = np.zeros(frame.shape,dtype=np.uint8)
    smallerFrame = cv2.resize(frame,(0,0),fx=.5,fy=.5)
    image[:height//2, :width//2] = cv2.rotate(smallerFrame,cv2.cv2.ROTATE_180)
    image[height//2:,:width//2] = cv2.rotate(smallerFrame,cv2.cv2.ROTATE_180)
    image[height//2:,width//2:] = smallerFrame
    image[:height//2,width//2:] = smallerFrame
    cv2.imshow('Frame',image)

    if cv2.waitKey(1) & 0xFF == ord('q'): #waits one millisecond for input 'q', if detected we will stop capturing frames
        break



    

cap.release() #releases camera
cv2.destroyAllWindows() #closes picture