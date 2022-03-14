# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:56:09 2022

@author: note
"""

from PIL import Image

def grayscale(colored_img):
    w, h = colored_img.size
    
    img = Image.new("RGB", (w, h))
    
    """
    weights: 
        red: 0.2989
        green: 0.5870
        blue: 0.1140
    """
    
    for x in range(w):
        for y in range(h):
            pixel = colored_img.getpixel((x, y))
            lum = int(0.2989*pixel[0] + 0.5870*pixel[1] + 0.1140*pixel[2])
            
            img.putpixel((x, y), (lum, lum, lum))
            
    img.show()
    
    

img = Image.open("data/moon.jpg")

grayscale(img)
            
    
    