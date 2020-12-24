import cv2 as cv
# 
catImg = cv.imread('Photos/cat.svg')

cv.imshow('Cat',catImg)

cv.waitKey(0)
print('CAT')

## Reading Videos

# capture = cv.VideoCapture('Videos/Dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     print(frame)
#     if isTrue:
#         pass
#     else:
#         break
#     cv.imshow('DOG',frame)

#     cv.waitKey(25)  #frame to wait specified milliseconds

# capture.release()
# cv.destroyAllWindows()