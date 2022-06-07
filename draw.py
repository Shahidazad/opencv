# draw on image

import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')

cv.imshow('Blank',blank)
# img=cv.imread('images/thor.jpg')
# cv.imshow('origin',img)
# cv.waitKey(0)

# paint image with color
# blank[200:300,300:400]=0,0,255
# cv.imshow('red',blank)
# cv.waitKey(0)

# draw rectangle
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
cv.imshow('rectangle',blank)
# cv.waitKey(0)
# draw circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('blank',blank)
# cv.waitKey(0)

# line method
cv.line(blank,(100,200),(300,400),(255,255,255),thickness=3)
cv.imshow('line',blank)
cv.waitKey(0)

# write text 
cv.putText(blank,'hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)