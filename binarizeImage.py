import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/woman2.jpg')

threshold = 128
maxValue = 255
im_bool = img < threshold

print(im_bool)

newImage = im_bool * maxValue

plt.imshow(newImage)
plt.show()