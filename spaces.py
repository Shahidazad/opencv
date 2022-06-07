import cv2  as cv
import matplotlib.pyplot as plt  # BGR TO RGB  ()plt. is default RGB
img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)

# plt.imshow(img)
# plt.show()


# convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# bgr to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
# BGR to lab

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


# BGR TO RGB
RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',RGB)
plt.imshow(RGB)
plt.show()
cv.waitKey(0)