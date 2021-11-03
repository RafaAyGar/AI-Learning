import cv2 as cv

image = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Image', image)

# BLURRING METHODS:

# 1. Averaging Method
average = cv.blur(image, (3,3))
cv.imshow('Average Blur', average)
# Averaging divides image in groups of  9 pixels where there is one in the middle, then computes the average color
# intesity of the surrounding pixels to give value to the central one.

# 2. Gaussian Blur
gaussian = cv.GaussianBlur(image, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)
# Gaussian divides the image in the same way that averaging but it assign a weight to each surrounding pixel and computes
# a weighted operation to get the intensity of the center | Gaussian seems more organic and natural than the averaging.

# 3. Median Blur
median = cv.medianBlur(image, 3)
cv.imshow('Median Blur', median)
# Works the same way as averaging but this computes the median instead of the average, this tends to reduce the noise 
# in the blurring.

# 4. Bilateral Blurring
bilateral = cv.bilateralFilter(image, 5, 100, 100)
cv.imshow('Bilateral', bilateral)
# This is one of the most effective and used methods, in it you specify a range of pixels that will be computed to draw 
# the central one, larger values implies that farther pixels will be computed so blur will ge increased.


cv.waitKey(0)