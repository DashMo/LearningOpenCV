import numpy as np
import cv2

img = cv2.imread('assets/logo.jpg', 1) #-1 is color, 0 is grayscale, 1 is alphaIncluded(unchanged)

frame = cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows