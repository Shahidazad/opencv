import cv2 as cv
from cv2 import CV_64F

import numpy as np
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)   



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap)) # pixel not be -VE
cv.imshow('Lapcian',lap)


# sobel
sobx=cv.Sobel(gray,cv.CV_64F,1,0)
soby=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('sobx',sobx)

cv.imshow('soby',soby)

c=cv.Canny(gray,150,175)
cv.imshow('Canny',c)


cv.waitKey(0)