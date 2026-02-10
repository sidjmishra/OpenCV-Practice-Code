import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r"D:\Learning Notes and code\Opencv\images\Slow_Traffic_Small.mp4")

# take 1st frame of video
ret, frame = cap.read()

#setup initial location of window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# set Region of Interest for tracking
roi = frame[y:y+height, x: x+width]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, norm_type=cv.NORM_MINMAX)

# cv.imshow('ROI', roi)
#setup thr termination criteria, either 10 iteration or move by atleast 1 pt.
term_criteria = (cv.TermCriteria_EPS | cv.TermCriteria_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv.meanShift(dst, track_window, term_criteria)

        x, y, w, h = track_window
        final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 3)
        cv.imshow('frame', final_image)
        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break
    else:
        break