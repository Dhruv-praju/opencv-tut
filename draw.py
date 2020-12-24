import cv2 as cv
import numpy as np

## color = (R, G, B)

# make a blank img
blank = np.zeros((500,500,3), dtype='uint8') #u need to give height, width and color channels of that frame
# cv.imshow('Blank', blank)   # This will show complete blank image of black color
cv.waitKey(0)

img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)


# 1.Paint image a certain color
blank[:] = 70,100,200
## u could also give certain range of pixel blank[pixel range]=color
# blank[200:300, 100:200] = 0,255,255
cv.imshow('color', blank)

# 2.Draw a rectangle
cv.rectangle(blank, (10,10), (200,200), (230,180,90), thickness=cv.FILLED)
cv.imshow('rectangle', blank)

# 3.circle
cv.circle(blank, (250,250),30, (200,100,40),thickness=-2)
cv.imshow('circle',blank)

# 4.Draw a line
cv.line(blank, (200,0), (blank.shape[1]//2 , blank.shape[0]//2), (250,250,250),thickness=3)
cv.imshow('line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Dhruv!!!', (10,125), cv.FONT_HERSHEY_TRIPLEX, 1.0, (130,10,100), 2)
cv.imshow('text', blank)
cv.waitKey(0)

# cv.destroyAllWindows()