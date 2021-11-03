import cv2 as cv
from UtilFunctions import reescaleFrame

# Reading Images
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Reescaling Images
img_resized = reescaleFrame(img, 1.25)
cv.imshow('Cat Resized', img_resized)

cv.waitKey(0)



