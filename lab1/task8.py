import cv2 as cv

cap = cv.VideoCapture(0)

w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
center = (int(w/2), int(h/2))


def find_max(color):
    color = list(color)
    val = max(color)
    ind = color.index(val)
    new_color = [0,0,0]
    new_color[ind] = 255

    return new_color


while(True):
    ret, frame = cap.read()

    if not(ret):
        break

    color = frame[center]

    cv.rectangle(frame, (center[0] - 90, center[1] - 10), (center[0] + 90, center[1] + 10), find_max(color), -1)
    cv.rectangle(frame, (center[0] - 10, center[1] + 90), (center[0] + 10, center[1] + 10), find_max(color), -1)
    cv.rectangle(frame, (center[0] + 10, center[1] - 90), (center[0] - 10, center[1] - 10), find_max(color), -1)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
