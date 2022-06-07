
import cv2 as cv
import numpy as np
img=cv.imread('images/thor.jpg')

cv.imshow('thor',img)

# translation(shift the img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) # dimension of image width and height
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)
# x=right,y=dwn,-x=left,-y=up
t=translate(img,100,-100)
# cv.imshow('translate',t)
cv.waitKey(0)


# rotation (rotate img)

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint==None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)  # angle and scale value =1
    dimension=(width,height)
    return cv.warpAffine(img,rotMat,dimension)
r=rotate(img,45)

# cv.imshow('rotate',r)

# resize
res=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',res)
# flipping

flip=cv.flip(img,-1)  # 0 = inverted  1= horizontal
cv.imshow('flip',flip)


cv.waitKey(0)