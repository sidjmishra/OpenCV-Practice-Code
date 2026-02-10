import cv2 as cv
import numpy as np

img = cv.imread(r'D:\Learning Notes and code\Opencv\images\pic1.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

# convert corners in int 
corners = np.int64(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x,y), 3, (0,255,0), -1)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()