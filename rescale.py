import cv2 as cv

def changeRes(width, height):
    """  Only live Videos  """
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame,scale=0.20):
    """Images, videos & live video"""
    ## rescaled frame = original frame * scale

    width = int(frame.shape[1] * scale)
    height = int( frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

## resizing images
CatImg = cv.imread('Photos/cat.jpg')

cv.imshow('Image',CatImg)
resized_img = rescaleFrame(CatImg)
cv.imshow('Image Resized', resized_img)

## resizing videos
capture = cv.VideoCapture('Videos/Dog.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:
        pass
    else:
        break
    
    frame_resized = rescaleFrame(frame)    

    cv.imshow('Video original',frame)    
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(30) & 0xFF==ord('q'):  #frame to wait specified milliseconds
        break

capture.release()
cv.destroyAllWindows()