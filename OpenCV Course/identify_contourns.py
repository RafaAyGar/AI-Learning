import cv2 as cv
import numpy as np

image = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Image', image)

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', image_gray)

image_canny = cv.Canny(image, 125, 175)
cv.imshow('Canny', image_canny)

# Actually Finding Contours with cv.findContours method...

contours, hierachies = cv.findContours(image_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found! (no blur)')

# Obtenemos un número demasiado grande de contornos, por lo que vamos a probar a hacerlo con una imagen difuminada...
image_blurred = cv.blur(image, (5,5), cv.BORDER_DEFAULT)
image_canny = cv.Canny(image_blurred, 125, 175)
contours_blurred, hierarchies_blurred = cv.findContours(image_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours_blurred)} contours found! (with blur)')

# Vamos a probar otra función del estilo de cv.Canny para quedarnos con los bordes de la imagen...
ret, thresh = cv.threshold(image_gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold Image', thresh)
contours_threshold, hierarchies_threshold = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours_threshold)} contours found! (using threshold function)')

# We are going to draw our contours in a blank image...
blank = np.zeros(image.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours_threshold, -1, (0,0,255), 1)
cv.imshow('Drew Contours (using threshold function)', blank)
blank = np.zeros(image.shape, dtype='uint8')
cv.drawContours(blank, contours_blurred, -1, (0,0,255), 1)
cv.imshow('Drew Contours (with blur)', blank)

cv.waitKey(0)