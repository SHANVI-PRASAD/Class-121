import cv2
import numpy as np
video = cv2.VideoCapture(0)
image = cv2.imread("download.jpg")
while True:
    ret,frame = video.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    upper_black = np.array([105,160,200])
    lower_black = np.array([30,30,30])
    mask = cv2.inRange(frame,lower_black,upper_black)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    f = np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()