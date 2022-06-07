from contextlib import redirect_stderr
import cv2 as cv
import numpy as np


img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)


blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)



merge=cv.merge([b,g,r])

cv.imshow('merge',merge)


blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('red',red)
cv.imshow('blue',blue)

cv.imshow('green',green)
cv.waitKey(0)