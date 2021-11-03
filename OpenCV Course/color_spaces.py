import cv2 as cv

image = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Image', image)

# BGR to Gray Scale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(image, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)