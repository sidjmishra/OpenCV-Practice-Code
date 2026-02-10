''' Countours are curves that join all the continuous points along a boundary that have the same color or intensity. 
They are used in image processing to detect and analyze the shape and structure of objects in an image. Contours can be used for 
various applications such as object detection, shape analysis, and image segmentation. In OpenCV, contours can be found using the 
findContours() function, which retrieves contours from a binary image. The contours can then be drawn on the original image using 
the drawContours() function. Contours can also be approximated to simpler shapes using the approxPolyDP() function, which reduces 
the number of points in the contour while preserving its shape. Overall, contours are a powerful tool for analyzing and 
understanding the structure of objects in images. '''

''' Countours is a python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"D:\Learning Notes and code\Opencv\images\opencv-logo.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 3)

cv.imshow("image", img)
cv.imshow("gray", imgray)

cv.waitKey(0)
cv.destroyAllWindows()