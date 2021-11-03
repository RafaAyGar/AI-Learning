import cv2 as cv
import numpy as np

image = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Image', image)

blank = np.zeros(image.shape[:2], dtype='uint8')

# We will split the image in 3 main colo channels
b,g,r = cv.split(image)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print('Shapes: ')
print(f'Image: {image.shape} the last 3 represent we have 3 color channels :)')
print(f'Blue: {b.shape}')
print(f'Green: {g.shape}')
print(f'Red: {r.shape}')

# Merging 3 color chanels
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)



cv.waitKey(0)