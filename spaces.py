import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/delhi.jpg')
cv.imshow('Delhi', img)

## Color-spaces are different color modes or format 

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV(Hue Saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

## Open cv reads an image in BGR format. But outside opencv we use RGB format which is inverse of BGR format
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_bgr=cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

### HSV image format is widely used for tracking, human detection because unlike RGB format, HSV seperates out intensity form the image
# reference :https://dsp.stackexchange.com/questions/2687/why-do-we-use-the-hsv-colour-space-so-often-in-vision-and-image-processing#:~:text=HSV%20stands%20for%20Hue%2DSaturation,skin%20color%2C%20fire%20color%20etc.

cv.waitKey(0)