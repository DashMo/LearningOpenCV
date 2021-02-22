import numpy as np
import cv2

colorimg = cv2.imread('assets/chessboard.jpg', 1) #-1 is color, 0 is grayscale, 1 is alphaIncluded(unchanged)
colorimg = cv2.resize(colorimg,(0,0),fx=.3,fy=.3)
img = cv2.cvtColor(colorimg,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img,200,.05,50) #(image, numCorners, minimumQuality, euclideanDistanceBetweenCorners to prevent rounded corners from getting multiple corners)
corners = np.int0(corners) #convert to integers instead of floats
print(corners)
for corner in corners:
    x,y = corner.ravel() #will flatten something from [[1,2,3]] to [1,2,3]
    colorimg = cv2.circle(colorimg,(x,y),5,[255,0,0],-1)
for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        c1 = tuple(corners[i][0])
        c2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255,size=3)))
        cv2.line(colorimg,c1,c2,color,1)
frame = cv2.imshow('Frame', colorimg )
cv2.waitKey(0)
cv2.destroyAllWindows