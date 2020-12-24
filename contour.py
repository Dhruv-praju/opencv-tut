import cv2 as cv
import numpy as np
## Contours are boundaries of objects (outline of objects) so that we can identify them
# reference : https://medium.com/@evergreenllc2020/fundamentals-of-image-contours-3598a9bcc595
# Contours are little different from edge detection.
# Contours are used in object/face detection and recognition

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175) # canny images are binary images that detect edges
# cv.imshow('Canny Edges', canny)

# This function can also used to create binary images
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)  # if the pixel(of grayscale) is below threshold(i.e 125) ,it will set to black and if above sets to white 
cv.imshow('Thresh', thresh)

# Mode in which contours are returned
# cv.RETR_LIST will give list of all contours
# cv.RETR_TREE returns all heirarchial contours
# cv.RETR_EXTERNAL returns only external contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found !')

# we can draw contours on blank image
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)