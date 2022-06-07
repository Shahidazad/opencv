import cv2 as cv


img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# simple thresh
threshold,thresh=cv.threshold(img,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold,thresh_inv=cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh',thresh_inv)

# adaptive
adaptive_t=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive',adaptive_t)

cv.waitKey(0)