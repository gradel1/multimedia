import cv2 as cv

cap = cv.VideoCapture(1)

while(True):
    ret, frame = cap.read()

    if not(ret):
        break

    cv.imshow('mob frame', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
