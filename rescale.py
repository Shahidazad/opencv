import cv2 as cv

img=cv.imread('images/thor.jpg')
cv.imshow('thor',img)


# to resize image

def rescaleFrame(frame,scale=0.75): # this method work for all
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions= (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


def changeRes(width,height):  # this work only for live videos
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture('videos/sample_1280x720_surfing_with_audio.mp4')
resized_image=rescaleFrame(img)
cv.imshow('Iamge',resized_image)
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('video resize',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): # close video by d
        break

capture.release()
cv.destroyAllWindows()