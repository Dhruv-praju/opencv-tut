import cv2 as cv
import numpy as np

##   Various filtering techniques are used to smoothen the image to reduce noise in the image

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

# Averaging 
blur = cv.blur(img, (3,3))
cv.imshow('Blur', blur)

# Gaussian Blur
# Gaussian blur is more natural than normal averaging technique of blur
# In this blur while averging pixel which u are averaging will contribute more, and as we go far pixel contribution reduces(since farther pixels would not have much influence)
gauss_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gauss Blur', gauss_blur)

# Median Blur
# In this it takes median(middle) of all pixels in a kernel and sets the pixel to that value
# It does not create any new value of the pixel
# Egdes are preserved while bluring(i.e. Edges get eroded but not blured like gaussian, and averaging blur)
# Median blur is widely used to reduce noise 
# reference : https://docs.gimp.org/2.10/en/gimp-filter-median-blur.html
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 170, 175, 95)
cv.imshow('Bilateral', bilateral)

bilateral = cv.bilateralFilter(img, 170, 175, 195)
cv.imshow('Bilateral2', bilateral)

cv.waitKey(0)