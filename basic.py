import cv2 as cv
from cv2 import blur
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)

# convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blurr
blurr=cv.GaussianBlur(img,(13,13),cv.BORDER_DEFAULT)
cv.imshow('blurr',blurr)


# find edges
can=cv.Canny(blurr,125,185)
cv.imshow('canny',can)
# cv.waitKey(0)
  # dilating the image
dilated=cv.dilate(can,(3,3),iterations=1)
cv.imshow('dilating',dilated)
# eroding
erod=cv.erode(dilated,(7,7),iterations=1)
cv.imshow('EROD',erod)
# resize
resized=cv.resize(img,(500,500))
# cv.imshow('resize',resized)

# crop 
croping=img[10:30,30:50]
cv.imshow('crop',croping)
cv.waitKey(0)   