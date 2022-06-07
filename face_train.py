import os
import numpy as np
import cv2 as cv


people=['elon','rajat']

# p=[]

# for i in os.listdir(r'C:\opencv\photo'):
#     p.append(i)
#     print(i)
# print(p)
DIR=r'C:\opencv\photo'


features=[]
labels=[]
haar_cascade = cv.CascadeClassifier('har_face.xml')
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for  img  in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            if img_array is None:
                continue    
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('train done')
print('features',len(features))
print('labels',len(labels))

features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')  # do not repeate the process again
np.save('feature.npy',features)

np.save('labels.npy',labels)