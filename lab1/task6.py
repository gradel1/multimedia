import cv2 as cv

cap = cv.VideoCapture(0)

w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
center = (int(w/2), int(h/2))

while(True):
    ret, frame = cap.read()

    if not(ret):
        break

    cv.rectangle(frame, (center[0]-90, center[1]-10), (center[0]+90, center[1]+10), (0, 0, 255), 2)
    cv.rectangle(frame, (center[0] - 10, center[1] + 90), (center[0] + 10, center[1] + 10), (0, 0, 255), 2)
    cv.rectangle(frame, (center[0] + 10, center[1] - 90), (center[0] - 10, center[1] - 10), (0, 0, 255), 2)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break
