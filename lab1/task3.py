import cv2 as cv
from time import monotonic as timer
import time

interval = 1/10
cap = cv.VideoCapture(r'media/videoplayback.mp4', cv.CAP_ANY)

while(True):
    ret, frame = cap.read()

    if not(ret):
        break

    frame2 = cv.resize(frame, (500, 800))
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('gray frame', frame)
    cv.imshow('big frame', frame2)
    cv.moveWindow("gray frame", 150, 150)

    if cv.waitKey(1) & 0xFF == 27:
        break

    time.sleep(interval - timer() % interval)
