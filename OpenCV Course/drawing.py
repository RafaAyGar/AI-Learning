import cv2 as cv
import numpy as np
from numpy.lib.function_base import bartlett

blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint Background Green
blank[:] = 0,255,0 

# Color red some pixels
blank[200:300, 300:400] = 0,0,255

# Drawing a Rectangle on an Image
cv.rectangle(blank, (0,0), (255,255), color=(255,0,0), thickness=4)
# cv.imshow('Img With Lined Rectangle', blank)
cv.rectangle(blank, (0,0), (255,255), color=(255,0,0), thickness=cv.FILLED)
# cv.imshow('Img With Filled Rectangle', blank)

# Drawing By Cuadrants
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), color=(255,0,0), thickness=cv.FILLED)
# cv.imshow('Drawed By Dividing Img Dimensions', blank)

# Drawing Circles
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(0,0,128), thickness=3)
cv.imshow('Same With Circle', blank)

# Drawing Lines
cv.line(blank, (0,0), (400, 100), color=(255, 255, 128), thickness=4)
cv.imshow('White Line Drawed', blank)

# Writing Text
cv.putText(blank,
            'Hello There is Some Text',
            (0,255),
            cv.FONT_HERSHEY_TRIPLEX,
            fontScale=0.7,
            color=(255,255,100),
            thickness=2)

cv.imshow('Image With Text', blank)
cv.waitKey(0)