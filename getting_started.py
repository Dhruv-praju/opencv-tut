"""READ, WRITE, DISPLAY AND SAVE IMAGE"""
import cv2 as cv
# First read the image
# reading means converting it into matrix
## if flag is : 1 reads in color mode
#               0 reads in grayscale mode
#              -1 reads in alpha mode if present
img=cv.imread('lena.jpg',1)    #reads the given image file with specified mode
print(img)
# imshow() method will display the image in the window
cv.imshow('image',img)
# waitkey() delays the no. of ms specified and ends delay if key is pressed
k=cv.waitKey(0)

if k==27:       # we want window to be displayed until user presses 'esc' key
    cv.destroyAllWindows()
elif k==ord('s'):   # we want image to be save if user presses 's' key
    cv.imwrite('lena_copy.png',img)    # with given matrix it saves image with given name and file format(.png, .jpg)
