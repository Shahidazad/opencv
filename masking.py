import cv2 as cv

import numpy as np

img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cir=cv.circle(blank.copy(),(200,200),200,255,-1)
rec=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
weird=cv.bitwise_and(rec,cir)
cv.imshow('weird',weird)

# cv.imshow('mask',mask)
# masked=cv.bitwise_and(img,img,mask=mask)
# cv.imshow('mask',masked)

cv.waitKey(0)