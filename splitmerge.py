import cv2 as cv
import numpy as np

### A colored image is made up of multiple channels
# BGR and RBG image are consist of 3 channels(Red, blue and green) merged together
# In opencv u can split the images in respective color channels

img = cv.imread('Photos/delhi.jpg')
cv.imshow('delhi', img) 

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
# This images are mapped to Grayscale. more white the region is , it has more amount of that component and more darker the region less concentration of that color is present

print(img.shape)    # shape variable returns tuple of number of rows, columns and channels(if present)
print(img.size)     # displays no. of pixels in the image
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)