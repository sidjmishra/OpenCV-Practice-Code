import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'D:\Learning Notes and code\Opencv\images\vtest.avi')

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
# method 1
# fgbg = cv.bgsegm.BackgroundSubtractorMOG()
# method 2
# fgbg = cv.createBackgroundSubtractorMOG2()
# method 3
# fgbg = cv.bgsegm.BackgroundSubtractorGMG()
# method 4
fgbg = cv.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    foreground_gmask = fgbg.apply(frame)
    # foreground_gmask = cv.morphologyEx(foreground_gmask, cv.MORPH_OPEN, kernel)
    cv.imshow('Frame', frame)
    cv.imshow('Foreground Mask Frame', foreground_gmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()