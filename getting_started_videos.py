"""CAPTURE A VIDEO FROM A CAMERA"""
## We will try to capture a video from webcam of laptop and convert it into grayscale and display it
import cv2 as cv
# To capture, u need to create VideoCapture object
# Argument can be device index(i.e a number to specify which camera) or the name of video file
cap = cv.VideoCapture(0)    #if you have second camera u can pass 1

while True :
    # read frame-by-frame
    ret, frame = cap.read() #ret will be true or false based on video frame is received or not

    # exit if frame is not reveiced
    if not ret:
        print("Can't receive frame (stream?) Exiting...")
        break

    # U can do operations on frame(convert into grayscale)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv.imshow('webcam frame',frame)
    # waitkey()  waits for specified ms util any key is pressed
    # waitkey(100000) - waits for 10 seconds and ends waiting if any key is pressed
    if cv.waitKey(1)&0xFF==ord('q'):  # waits for 1ms until key 'q' is pressed
        break

    print('frame displayed')

cap.release()
cv.destroyAllWindows()