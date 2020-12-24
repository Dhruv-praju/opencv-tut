"""PLAYING VIDEO FROM A FILE"""
## Playing video from a file is same as capturing it from the camera
import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
cap.open('vtest.avi')
# Play if cap is initialized
# cap object will not initialize if wrong file name or camera index is given
while cap.isOpened():
    # cap.read() returns true if frame is read correctly
    ret, frame = cap.read()

    # u can print height and width of the frame
    # by default it is 640 x 480
    print(f'width: {cap.get(cv.CAP_PROP_FRAME_WIDTH)}  height: {cap.get(cv.CAP_PROP_FRAME_HEIGHT)}')

    if not ret:
        print("Can't receive frame (stream?) Exiting...")
        break

    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # display the frame
    cv.imshow('video file', gray)
    # Wait for 25ms to display the frame
    # u must atleast wait for 25ms so that video speed is normal
    # if u set wait time too less, then video will be very fast

    if cv.waitKey(150)==ord('q'):   # after frame is displayed program stops here for 150ms and if key is pressed, it becomes true and below statement is executed
        break
    # cv.waitKey(50)

cap.release()   # release all the resources
cv.destroyAllWindows()