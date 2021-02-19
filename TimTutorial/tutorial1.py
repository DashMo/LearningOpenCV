import cv2
img = cv2.imread('assets/logo.jpg', 1) #-1 is color, 0 is grayscale, 1 is alphaIncluded(unchanged)
#img = cv2.resize(img,(1200,1200)) #resize to tuple size
img = cv2.resize(img,(0,0),fx=.5,fy=.5) #Scale by fx and fy
img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE) #rotate image
cv2.imshow('Image',img)
cv2.imwrite('output.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows

