import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/woman.jpg')

img_R, img_G, img_B = img.copy(), img.copy(), img.copy()

img_R[:, :, (0, 1)] = 0
img_G[:, :, (0, 2)] = 0
img_B[:, :, (1, 2)] = 0

img_rgb = np.concatenate((img_R, img_G, img_B), axis=1)
img_rgb = cv2.resize(img_rgb, (0, 0), fx=0.5, fy=0.5)

plt.imshow(img_rgb)
plt.show()