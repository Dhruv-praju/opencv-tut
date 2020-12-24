import cv2 as cv
# their are various types of images (reference :https://www.javatpoint.com/dip-types-of-images)
img = cv.imread('Photos/mumbai.jpg')

cv.imshow('Mumbai', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('Grayscale', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny =  cv.Canny(blur, 125, 175)    # canny function detects edges in the given input image
cv.imshow('Canny Image', canny)

# Dilating the image
## Dilating means adding extra pixels to the boundary of objects in a image
## while erosion means removing pixels from boundaries
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated',dilated)

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (900,600), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:500, 100:450]
cv.imshow('Croped', cropped)

cv.waitKey(0)   # wait infinitly