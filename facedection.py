import cv2 as cv


img=cv.imread('images/3.jpg')
cv.imshow('men',img)   

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade=cv.CascadeClassifier('har_face.xml')
face_r=haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=2)


print(len(face_r))
for (x,y,w,h) in face_r:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('detected',img)



cv.waitKey(0)
# print(dir(har_cascade))