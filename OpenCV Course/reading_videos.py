import cv2 as cv
from UtilFunctions import reescaleFrame

# Reading Videos
video = cv.VideoCapture(0) # The integer passed refer to the camere used, if you have multiples try arguments like 1 or 2.
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = reescaleFrame(frame, 1.25)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
