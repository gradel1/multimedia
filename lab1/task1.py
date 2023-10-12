import cv2 as cv

img = cv.imread(r'media/pict.jpg')
cv.namedWindow('Display window', cv.WINDOW_FULLSCREEN)
cv.imshow('picture', img)
cv.waitKey(0)
