from pickletools import uint8
import cv2
import numpy as np 

img = cv2.imread('data/woman.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
print(img.shape)

mask = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
cv2.rectangle(mask, (300, 100), (800, 500), 255, -1)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('masked', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
cv2.circle(mask, (500, 250), 200, 255, -1)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('masked', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
