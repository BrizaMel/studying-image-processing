import cv2

# loading an image
img = cv2.imread('data/flower.jpg', -1)
# img = cv2.resize(img, (700, 500))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('data/new_img.jpg', img)