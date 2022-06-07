
import cv2 as cv

# img=cv2.imread("images\sim.png")

# print(img)
# print(2)
# cv2.imshow("original", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # dir(cv2)

# read video

capture=cv.VideoCapture('videos/sample_1280x720_surfing_with_audio.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'): # close video by d
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)