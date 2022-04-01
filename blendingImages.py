import cv2
import numpy as np 
import matplotlib.pyplot as plt

first = cv2.imread('data/woman.jpg')

print(first.shape)
h, w = first.shape[0], first.shape[1]

second = cv2.imread('data/flower.jpg')
second = cv2.resize(second, (w, h))

blended = (first*0.6 + second*0.4).astype(np.uint8)

plt.figure(figsize=(10, 10))
plt.imshow(blended)
plt.show()