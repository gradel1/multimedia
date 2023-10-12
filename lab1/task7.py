import cv2 as cv

cap = cv.VideoCapture(0)

w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fourcc = cv.VideoWriter_fourcc(*'MJPG')
video_writer = cv.VideoWriter('web_out.avi', fourcc, 60, (w, h))

while(True):
    ret, frame = cap.read()

    if not(ret):
        break

    cv.imshow('frame', frame)
    video_writer.write(frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
video_writer.release()
