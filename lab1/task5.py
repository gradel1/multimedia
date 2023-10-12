import cv2 as cv

img = cv.imread(r'media/47428-7-smiley-picture-free-photo-png.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('frame', img)
cv.imshow('hsv frame', hsv)

cv.waitKey(0)
