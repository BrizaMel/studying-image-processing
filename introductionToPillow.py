# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:53:26 2022

@author: Briza Mel
"""

from PIL import Image, ImageFilter
import numpy as np
from matplotlib import pyplot as plt


def vertical_images(img1, img2):
    img1 = np.array(img1)
    img2 = np.array(img2)
    vertical = Image.fromarray(np.vstack((img1, img2)))
    vertical.show()

def details(img):
    img = np.array(img)
    print("The dimension of the image is: ", img.ndim)
    print("The height of the image is: ", img.shape[0])
    print("The width of the image is: ", img.shape[1])
    print("The channels of the image is: ", img.shape[2])
    print("The data type of the image is: ", img.dtype)
    
def details_pixel(img, pixel):
    img = np.array(img)
    print("The pixel value is: ", img[pixel[0]][pixel[1]]) # [R, G, B]
    print("Min pixel value at channel R: ", img[:,:,0].min())
    print("Min pixel value at channel G: ", img[:,:,1].min())
    print("Min pixel value at channel B: ", img[:,:,2].min())
    
    
def save_ndarray_as_image(img_array, path):
    img = Image.fromarray(img_array)
    img.save(path)
    
img = Image.open("data/moon.jpg")

# details(img)
# details_pixel(img, (20,100))

filtered = img.filter(ImageFilter.EDGE_ENHANCE)

img_array = np.array(filtered)
save_ndarray_as_image(img_array, "data/filtered.jpg")

# vertical_images(img, filtered)

"""
List of predefined image enhencement filters:
BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SHARPEN
SMOOTH
SMOOTH_MORE
"""



