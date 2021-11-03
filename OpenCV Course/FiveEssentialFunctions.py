import cv2 as cv


# Transform image to Gray Scale
image = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Image', image)
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Image Gray', image_gray)

# Blur an Image
image_blur = cv.GaussianBlur(image, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blurred Image', image_blur)

# Edge Detector
edges = cv.Canny(image, 125, 175)
cv.imshow('Canny Edge', edges)

# Combine Edge Detector With Blurring
edges_with_blur = cv.Canny(image_blur, 125, 175)
cv.imshow('Canny Edges With Blur', edges_with_blur)

# Dilating The Image
dilated = cv.dilate(image, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroded Image (Erosionar)
eroded = cv.erode(image, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize 
resized = cv.resize(image, (1000, 1000)) # Cambia el tamaño a 500x500
cv.imshow('Resized', resized)
# ** You can interpolate the image if you are making a big change in the size...
resized_interpolated = cv.resize(image, (1000, 1000), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Interpolated', resized_interpolated)

# Crop (Toma la porcio que se indica de una imagen)
cropped = image[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)   