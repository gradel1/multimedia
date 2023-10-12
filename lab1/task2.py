import cv2 as cv

img1 = cv.imread(r'media/images.jpg',
                 cv.IMREAD_GRAYSCALE) #convert image to the single channel grayscale image
img2 = cv.imread(r'media/47428-7-smiley-picture-free-photo-png.png',
                 cv.IMREAD_REDUCED_COLOR_2) #convert image to the 3 channel BGR color image and the image size reduced 1/2
img3 = cv.imread(r'media/unknown.png',
                 cv.IMREAD_ANYCOLOR) #the image is read in any possible color format

cv.namedWindow('window 1',
               cv.WINDOW_NORMAL) #the user can resize the window
cv.namedWindow('window 2',
               cv.WINDOW_AUTOSIZE) #the user cannot resize the window, the size is constrainted by the image displayed.
cv.namedWindow('window 3',
               cv.WINDOW_GUI_EXPANDED) #status bar and tool bar

cv.imshow('picture 1', img1)
cv.imshow('picture 2', img2)
cv.imshow('picture 3', img3)

cv.waitKey(0)

cv.destroyAllWindows()
