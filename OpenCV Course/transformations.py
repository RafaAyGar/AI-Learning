import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

image = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Image', image)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> Left
# -y --> Up
# x -- Right
# y --> Down
translated = translate(image, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(image, 45)
cv.imshow('Rotated', rotated)

# Resize 
resized = cv.resize(image, (1000, 1000)) # Cambia el tamaño a 500x500
cv.imshow('Resized', resized)
# ** You can interpolate the image if you are making a big change in the size...
resized_interpolated = cv.resize(image, (1000, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Interpolated', resized_interpolated)

# Flipping
hor_flipped = cv.flip(image, 0)
cv.imshow('Horizontal Flipped Image', hor_flipped)
ver_flipped = cv.flip(image, 1)
cv.imshow('Vertically Flipped Image', hor_flipped)
both_flipped = cv.flip(image, -1)
cv.imshow('Horizontal And Vertically Flipped Image', hor_flipped)

# Crop (Toma la porcio que se indica de una imagen)
cropped = image[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

