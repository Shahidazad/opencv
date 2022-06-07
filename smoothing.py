
import cv2  as cv
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)

avg=cv.blur(img,(3,3))
cv.imshow('average blur',avg)


# gaussian blurr (less blur as compare average)
gaus=cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaus',gaus)

# median
m=cv.medianBlur(img,7)
cv.imshow('median',m)


# bilateral blur  (retain edges also)
bil=cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bil)

cv.waitKey(0)