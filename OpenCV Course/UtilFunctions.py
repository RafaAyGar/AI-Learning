import cv2 as cv

# Work on Images, Videos and Live Videos
def reescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Work on Live Videos
def changeResolution(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)
    return capture
