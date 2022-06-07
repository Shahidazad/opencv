import cv2 as cv

import numpy as np
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


ca=cv.Canny(img,125,175)
cv.imshow('ca',ca)


ret,thresh=cv.threshold(gray,125,125,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
contours,hierarchies=cv.findContours(ca,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contour draw',blank)


cv.waitKey(0)