import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rec=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)# starting and ending pts  color(255)white
cir=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rec)

cv.imshow('circle',cir)


# bitwise and
bit_and=cv.bitwise_and(cir,rec) # merging to images (intersection) common(rec,cir)
# cv.imshow('bit_and',bit_and)

# bit or

bit_or=cv.bitwise_or(cir,rec) # merging to images super impose(rec+cir)
cv.imshow('bit_or',bit_or)

# bit XOR
bit_xor=cv.bitwise_xor(rec,cir)# non intersecting (rec-cir)
cv.imshow('XOR',bit_xor)



# bitwise NOT (convert white to black vice verse) Opposite
bit_not=cv.bitwise_not(rec,cir)
cv.imshow('bit not',bit_not)
cv.waitKey(0)