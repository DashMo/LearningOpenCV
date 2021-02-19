import cv2
import random
img = cv2.imread('assets/logo-2.png', 1) #-1 is color, 0 is grayscale, 1 is alphaIncluded(unchanged)
print(img.shape) #uses BGR instead of RGB  for order (0-255 range)
#print(img[0])
print(img[1000][500:520])
for i in range(900,1001):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
head = img[300:1000,50:1000]
img[300:1000,1050:2000 ] = head
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()