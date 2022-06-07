from turtle import color
import cv2 as cv

import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)   

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',mask)



# gray histogram
# gr_ht=cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('gray hist')
# plt.xlabel('bins')
# plt.ylabel('pixel')
# plt.plot(gr_ht)
# plt.xlim([0,256])
# plt.show()


# color hist
col=('b','g','r')

for i,c in enumerate(col):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=c)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)