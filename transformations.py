import cv2 as cv
import numpy as np
## Image transformations are translation , rotation , resizing, clipping and cropping
img = cv.imread('Photos/delhi.jpg')

cv.imshow('Delhi',img)

# you can get the dimension of frame(image) f as f.shape[1] which is width and f.shape[0] is height

# Translation
def translate(img, x, y):
    """shifts the given image by x pixels along X-axis and y pixels along Y-axis"""
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimemsion = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimemsion)

# -x --> left
# -y --> Up
# y --> Down
# x --> Right

translated = translate(img, 100, -100)   # shifts image right by 100 pixels and down by 100 pixels
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None :
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle , 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 270)
cv.imshow('Rotated rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (900,500), interpolation=cv.INTER_CUBIC)   #while enlarging use interpolation as INTER_LINEAR or INTER_CUBIC
# while shrinking image use default that is INTER_AREA
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)
cv.imshow('Flipped', flip)

cv.waitKey(0)

########### Scaling Vs Resizing #######
## reference : https://guides.lib.umich.edu/c.php?g=282942&p=1885347

# Scaling an image means stretching every pixel in image . It does not add any new pixels to the image.
# Due to this, scaling images larger than its original dimensions, results it to appear very fuzzy or blur.
# Hence image is not clear when it is enlarged(i.e image quality degrades)
# Scaling to small size doesn't affect the quality.
# E.g. Suppose ur image has width of 300px and u scale image to a factor of 1.5 .After rescaling still width is same (same no. of pixels 300), just the difference is that, now each pixel's width is 1.5 times its original pixel width 
# Think of scaling an image as magnify or zooming. You are not changing its actual size

# Resizing actually means changing size(no. of pixels) of an image. Resizing is an intristic change in the size of an image 
# E.g. Changing an image size from 1000px to 500 px is resizing

######## Cropping ########
# Cropping removing certain part of an image. Cropping means discarding the pixels that u don't want from an image . After cropping actual size of an image is changed  