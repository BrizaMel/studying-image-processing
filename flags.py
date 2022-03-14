# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:09:40 2022

@author: Briza Mel
"""
from PIL import Image

def triangle(size):
    WHITE = (255, 255, 255)
    
    image = Image.new("RGB", (size, size)) 
    
    for i in range(size):
        for j in range(size):
            if (i > j):
                image.putpixel((i, j), WHITE)
                
    image.show()
    
    
def Germany_flag(height):
    # ratio = 3:5
    RED = (255, 0, 0)
    YELLOW = (255, 204, 0)
    
    width = (5*height)//3
    
    flag = Image.new("RGB", (width, height))
    offset = height//3
    
    for i in range(width):
        for j in range(offset+1):
            # black is standard
            # image.putpixel((i, j), BLACK)
            flag.putpixel((i, j + offset), RED) 
            flag.putpixel((i, j + 2*offset), YELLOW)
    
    flag.show()
            
    
def Japan_flag(height):
    # ratio = 2:3
    WHITE = (255, 255, 255)
    RED = (188, 0, 45)
    
    width = (3*height)//2
    
    flag = Image.new("RGB", (width, height), WHITE)
    
    # diameter/height = 3/5 
    radius = (3*height)//10
    center = (width//2, height//2)
    
    for i in range (center[0] - radius, center[0] + radius + 1):
        for j in range (center[1] - radius, center[1] + radius + 1):
            if ((i - center[0])**2 + (j - center[1])**2 <= radius**2):
                flag.putpixel((i, j), RED)
    
    flag.show()
    
    
    
# triangle(500)
Germany_flag(700)
# Japan_flag(700)