import cv2 as cv
import numpy as np

img = cv.imread(r'D:\Learning Notes and code\Opencv\images\chessboard.png')

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# croner harris take image in float32 format
gray = np.float32(gray)

dst = cv. cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.02 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()