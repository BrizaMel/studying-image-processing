import cv2
import random


img = cv2.imread('data/flower.jpg', -1)

# height, width, channels
# channel : blue, green, red
print(img.shape)

width = img.shape[1]

for i in range(100):
    for j in range(width):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img2 = cv2.imread('data/flower.jpg', -1)

tag = img2[400:600, 800:1000]
img2[600:800, 1000:1200] = tag
img2 = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
